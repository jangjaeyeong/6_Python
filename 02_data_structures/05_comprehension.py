nums = []

for n in range(1,5) :
    nums.append(n)

print(f"nums : {nums}")

nums = [n * n for n in range(1, 6)]
print(f"nums (컴프리헨션) : {nums}")

# 조건에 해당하는 데이터만 포함 할 때 -> [표현식 for 변수 in 반복대상 if 조건]

nums = [1, 2, 3, 4, 5, 6]
print(f"짝수만 -> {[n for n in nums if n % 2 == 0]}")
print(f"3의 배수만 -> {[n for n in nums if n % 3 == 0]}")

print("=" * 60)

# 딕셔너리 컴프리헨션 => {키_표현식: 밸려_표현식 for 변수 in 반복대상 if 조건}
menus = ["갈비탕", "돈가스", "제육", "더블QFC"]

message = 'No Pain, No Gain'

unique_char = {ch for ch in message}
print(f"'{message}' 의 고유 문자: {unique_char}")

unique_char = {ch for ch in message if ch != ',' and ch != ' '}
print(f"'{message}' 의 고유 문자: {unique_char} / ({len(unique_char)})")