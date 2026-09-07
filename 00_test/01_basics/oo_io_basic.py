"""

"""
print("="*60)
print("기본 출력 확인")
print("="*60)
print("hello, python!")
print('반가워, 파이썬!')

print(100)
print(3.14)
print(10+20)

print("="*60)
print("여러 값을 동시에 출력")
print("="*60)

print("장재영", 25, "빨강")
# 구분자를 지정하여 출력 : sep 옵션 사용 (default : space)
print("2026", "09", "07", sep="-")

# 마지막 출력 문자 지정: end 옵션 사용 (default : 개행)
print("첫번째 줄", end=" ")
print("두번째 줄")


print("=" * 60)
print("이스케이프 문자")
print("=" * 60)

print("이번 줄 다음에 출력하겠습니다. \n 한 줄 개행" )
print("집에 갈게요")

name = "김동주"
age = 25
height = 172.1

print("이름: {}, 나이: {}, 키: {}".format(name, age, height))

print(f"이름: {name}, 나이: {age}, 키: {height}")
print(f"내년에는 {age + 1}살이 됩니다.")

print(f"[{name:<10}]")
print(f"[{name:>10}]")
print(f"[{name:^10}]")

print("="*60)
print("입력 받아보기")
print("="*60)


age_str = input("나이 입력: ")
print(f"입력값: {age_str}, 타입: {type(age_str)}")

age = int(age_str)

print(f"입력값: {age} 타입: {type(age)}")
print(f"내년 나이: {age + 1}")