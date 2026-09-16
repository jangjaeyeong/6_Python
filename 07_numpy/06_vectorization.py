from load_utils import load_dates, load_one_stock, load_codes
import numpy as np
dates = load_dates()
codes = load_codes()
prices = load_one_stock(0)

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
print(f"a : {a}\nb : {b}")
print(f" a * 2 = {a * 2}")
print(f" a + b = {a + b}")
print(f"a > 25 = {a > 25}")

x = np.array([1,4,9,16])
print(f" x : {x} \nnsqrt : {np.sqrt(x)}")

x = np.array([1.623423, 4.23423, 9.25234, 16.2356234])
intarr = np.round(x,0)
intarr = np.array(intarr, dtype="int64")
print(f"x: {x}\nround : {intarr}")