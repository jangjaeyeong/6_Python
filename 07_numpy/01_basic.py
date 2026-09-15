
import numpy as np

data_list = [1, "이", 3.0, [4]]
print(f"data_list : {data_list}")
print(f"각 요소 별 타입 : {[type(x).__name__ for x in data_list]}")

data_list2 = [10, 20, 30, 40]

print('-' * 60)

# for d1, d2 in zip(data_list, data_list2) :
#     print(f"{d1} + {d2} = {d1 + d2}")
# print('-' * 60)
    
    
arr = np.array([1 ,2, 3, 4])
print(f"arr : {arr}")
print(f"배열 타입 : {arr.dtype}")

arr2 = np.array([5, 6, 7, 8])
print(f"arr2 : {arr2}")

"""
for d1, d2 in zip(arr, arr2):
    print(f"{d1} + {d2} = {d1 + d2}")
"""

print(f"arr + arr2 = {arr + arr2}")


arr_0d = np.array(42)
print(f"0차원 배열: {arr_0d}, 차원: {arr_0d.ndim}, 형태 : {arr_0d.shape}")

arr_1d = np.array([1,2,3])
print(f"1차원 배열: {arr_1d}, 차원: {arr_1d.ndim}, 형태 : {arr_1d.shape}")

arr_2d = np.array([[1,2,3], [4,5,6]])
print(f"2차원 배열: \n{arr_2d}\n, 차원: {arr_2d.ndim}, 형태: {arr_2d.shape}")

print("=" * 60)

n = 100_000
print(f"n : {n}")