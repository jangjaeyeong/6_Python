"""
    리스트 (list)
"""

colors = ["red", "green", "blue"]

print(f"colors -> {colors}")

print(f"{colors[0:2]}")

mixed = [100, "Hello", True, [1,2,3]]
print(f"mixed : {mixed}")

temp = []

print(f"mixed --> {bool(mixed)}")
print(f"temp --> {bool(temp)}")

numbers = [5,1,2,7,9,4,1]

print(f"numbers에 7이 있는지? {7 in numbers}")
print(f"numbers에 7이 있는지? {numbers.index(7)}")


print(f"numbers에 3이 있는지? {3 in numbers}")
# print(f"numbers에 7이 있는지? {numbers.index(3)}")

print(f"리스트 길이: {len(numbers)}")

print(f"{numbers}")
# 해당 리스트의 값을 변경
print(f"sort -> {numbers}")
numbers.sort(reverse=True)
print(f"sort(reverse=True) -> {numbers}")

numbers.sort()

fruits = ["banana", "cherry", "apple"]
fruits.sort()
print(f"문자열 정렬 -> {fruits}")
# 해당 리스트를 역순으
print(f"reverse() -> {fruits}")

fruits.reverse()
print(f"reverse() -> {fruits}")

print("=" * 60)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"(1, 1) -> {matrix[1][1]}")
print()

for row in matrix:
    for value in row :
        print(value, end=" ")
    print()

