"""
    반복문
"""

print("=" * 60)
print("for문 --> 항상 for-each")
print("=" * 60)

members = ["임수진", "오범영", "이우진"]

for m in members :
    print(f"{m}님 환영합니다.")
print()

for c in "HAPPY" :
    print(c, end=" ")
print()

print("=" * 60)
print("range 내장 함수 사용")
print("=" * 60)

print(f"range(5) -> {list(range(5))}")
print(f"range(1, 6) ->{list(range(1, 6))}")


n = 1

while True:
    if n > 3 :
        break
    print(f"n : {n}")
    n+=1


print("=" * 60)
print("break / contineu / for-else")
print("=" * 60)

print("1 ~ 10 범위에서 홀수만 출력, 단 7을 넘으면 중단")
for n in range(1, 11) :
    if n % 2 == 0 :
        continue
    if n > 7 :
        break
    print(n, end=" ")
print()

#for-else : 반복문 정상 종료 시 else 블록 실행
print(f"{members}")

for m in members:
    if m == "임수진" :
        print("찾았습니다.")
        break
