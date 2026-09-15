"""
    BeautifulSoup
        :HTML 및 XML 문서에서 원하는 데이터를 쉽게 추출할 수 있도록 해주는 스크래핑 라이브러리
        
        1. requests로 요청 후 문자열 (html, xml)을 응답 받음
        2. bs4의 find, select를 활용해서 특정 텍스트를 추출
"""

import requests
from config import BASE, TIMEOUT, HEADERS
from bs4 import BeautifulSoup

resp = requests.get(f"{BASE}/stocks", headers=HEADERS, timeout = TIMEOUT)

html = resp.text
print(f"{BASE}/stocks       [{resp.status_code}] {len(html)}자")

print("-" * 60)

soup = BeautifulSoup(html, 'lxml')

print(f"title --> {soup.title.text}")

rows_select = soup.select("tr.stock-row")
print(f"tr.stock-row )개수 : {len(rows_select)}")

first = soup. select_one("tr.stock-row")
price_tag = first.select_one("td.col-price")
print(f"td.col-price text : {price_tag.text}")

for sel in ["td.col-code", "td.col-name a", "td.col-sector",
"td.col-price", "td.col-change", "td.col-volume",
"td.col-market span"] :
    tag = first.select_one(sel)
    value = tag.get_text(strip=True) if tag else "없음"
    print(f"{sel:<20} {value}")
    
    
