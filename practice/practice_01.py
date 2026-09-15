

# name = input("이름 입력: ")
# gender = input("성별(M/F) 입력: ")
# age = int(input("나이 입력: "))
# height = float(input("키 입력: "))

# print(f"이름: {name}, 성별: {gender}, 나이: {age}, 키: {height}cm")


# ch = input("영문 소문자를 입력하세요: ")
# print(ch.upper())


# x = int(input("첫 번째 정수를 입력하세요: "))
# y = int(input("첫 번째 정수를 입력하세요: "))

# print(f"합: {x + y}")
# print(f"차: {x - y}")
# print(f"곱: {x * y}")
# print(f"몫: {x // y}")
# print(f"나머지: {x % y}")


# x = int(input("첫 번째 정수를 입력하세요: "))
# y = int(input("첫 번째 정수를 입력하세요: "))

# print(f"{x}의 제곱: {x * x}")
# print(f"{y}의 제곱근: {int(y ** 0.5)}")


# score = int(input("점수를 입력하세요 (0 ~ 100): "))

# if score >= 90 :
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# for i in range(1, 101) :
#     if i % 2 == 0 :
#         print(i)
    

result  = 0
for i in range(1, 101) :
    if i % 3 == 0 and i % 5 != 0 :
        result += i

print(result)
