"""
    튜플 (tuple)
"""

point = (10, 20)
point2 = 50, 60

single = (10,)
single2 = (10)


print(f"point : {point} {type(point)}")
print(f"point2 : {point2} {type(point2)}")

print(f"single : {single} {type(single)}")
print(f"single2 : {single} {type(single)}")

x, y = 2, 6


x, *rest = (1,2,3,4,5)
print(f"x: {x}, rest: {rest}")


locations = {
    (35.5451, 126.9750): "서울역",
    (30.5401, 124.9050) : "부산역"
}