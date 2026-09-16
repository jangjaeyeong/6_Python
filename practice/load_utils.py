"""
    실습 데이터 불러오는 기능을 담은 모듈
"""

import numpy as np
from pathlib import Path

CSV_PATH = Path(__file__).with_name("prices.csv")

N_DAYS = 750   # 거래일수


_COLUMNS = {
    "code": 0,
    "date": 1,
    "open": 2,
    "high": 3,
    "low": 4,
    "close": 5,
    "volume": 6,
    "change": 7,
    "changeRate": 8
}


# 한 번 읽은 열(데이터)을 저장하는 용도
_cache = {}


def _read(col, dtype):
    """
        csv에서 하나의 열만 읽어서 1차원 배열로 리턴
    """
    key = (col, str(dtype))

    if key not in _cache:
        if not CSV_PATH.exists():
            raise FileNotFoundError(f"{CSV_PATH} 파일을 찾을 수 없습니다.")

        _cache[key] = np.loadtxt(
            CSV_PATH,
            dtype=dtype,
            delimiter=",",
            usecols=_COLUMNS[col],
            skiprows=1,
            encoding="utf-8-sig"
        )

    return _cache[key].copy()


def load_close_flat():
    """
        종가 데이터만 1차원 배열로 리턴
    """
    return _read("close", "int64")


def load_one_stock(idx=0):
    """
        한 종목의 종가만 1차원 배열로 리턴
    """
    close_arr = load_close_flat()

    start = idx * N_DAYS
    end = start + N_DAYS

    return close_arr[start:end]


def load_dates():
    """
        거래일 정보를 날짜형식으로 리턴 (1차원 배열)
    """
    dates = _read("date", str)
    return dates[:N_DAYS].astype("datetime64[D]")


def load_codes():
    """
        종목 코드 배열 리턴
    """
    codes = _read("code", str)

    # 중복을 제거하면서 등장 순서 유지
    return np.unique(codes)


def load_matrix():
    """
        종가 행렬을 반환
        행: 종목 / 열: 날짜

        현재 CSV에서 각 종목의 데이터를 확인하여
        (종목 수, 750) 형태의 행렬을 만든다.
    """

    codes = load_codes()
    close = load_close_flat()

    matrix = np.full((len(codes), N_DAYS), np.nan)

    for i, code in enumerate(codes):
        code_arr = _read("code", str)

        stock_close = close[code_arr == code]

        days = min(len(stock_close), N_DAYS)

        matrix[i, :days] = stock_close[:days]

    return matrix


def load_column(name):
    """
        열 데이터를 행렬로 반환
    """

    if name in ("code", "date"):
        raise KeyError("기존 함수를 사용하세요.")

    if name not in _COLUMNS:
        raise KeyError("찾을 수 없는 열입니다.")

    dtype = "float64" if name == "changeRate" else "int64"

    data = _read(name, dtype)

    codes = load_codes()

    matrix = np.full((len(codes), N_DAYS), np.nan)

    code_arr = _read("code", str)

    for i, code in enumerate(codes):
        stock_data = data[code_arr == code]

        days = min(len(stock_data), N_DAYS)

        matrix[i, :days] = stock_data[:days]

    return matrix


_NAN_IDX = np.array([
    37, 88, 142, 199, 242, 301,
    358, 412, 470, 537, 618, 703
])

_OUTLIER_IDX = np.array([
    33, 61, 215, 488, 724
])

_OUTLIER_SCALE = np.array([
    6.2, 5.4, 7.8, 5.9, 7.1
])


def load_dirty():
    """
        결측, 이상치용 데이터

        첫 종목의 종가 데이터에 결측 12개, 이상치 5개
    """

    arr = load_one_stock(0).astype("float64")

    arr[_NAN_IDX] = np.nan

    arr[_OUTLIER_IDX] = (
        arr[_OUTLIER_IDX] * _OUTLIER_SCALE
    )

    return arr, np.sort(_NAN_IDX), np.sort(_OUTLIER_IDX)