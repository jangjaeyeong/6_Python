import numpy as np

arr = np.arange(12)
print(f"arr : {arr}")

arr_2d = arr.reshape(3, 4)

arr_2d_2 = arr.reshape(2, 6)
print(f"(12,)->(2,6) :\n{arr_2d_2}")

# -1 지정 : 자동 계산
arr_2d_3 = arr.reshape(4, -1)
print(f"(12,)->(4,-1):\n{arr_2d_3}")

arr_2d_4 = arr.reshape(-1, 6)
print(f"(12,) -> (-1, 6) : \n{arr_2d_4}")

print('-' * 60)

arr_3d = arr.reshape(2,2,3)
print(f"shape : {arr_3d}")