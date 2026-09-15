import random
"""
    1번 문제
"""
def bmi () :
    weight = float(input("몸무게를 입력하세요(kg) : "))
    height = float(input("키를 입력하세요(cm) : "))

    height = round(height, 2) / 100

    print(f"BMI : {round(weight / (height * height),2)}")


"""
    2번 문제
"""
def avg() :    
    sum, i = 0, 0
    while True:
        n = input("숫자 입력 (q 입력 시 종료) : ")
        if n == "q":
            break
        sum += int(n)
        i+=1
        
    if sum == 0 :
        print("---> 값이 없습니다.")
    else :
        print(f"---> 평균: {round(sum / i , 2)}") 

"""
    3번 문제
"""
def word() :
    str = input("문장을 입력하세요: ")
    str = str.lower().split(" ")
    strDict = {}
    
    print(str)

    for word in str :
       if word in strDict:
            strDict[word] +=1
       else :
           strDict[word] = 1
           
    print("단어 빈도 수 결과")
    for key, value in strDict.items() :
        print(f"- {key} : {value}회")

"""
    4번 문제
"""
def lotto() :
    lotto = []
    tried = int(input("구매할 로또 게임 수를 입력하세요: "))
    print("[로또 번호 발급 결과]")
    for i in range(0, tried) :
        for _ in range(0, 6) :
            rand = random.randint(1, 45)
            lotto.append(rand)
            lotto.sort()
        print(f"{i}게임: {lotto}")
        lotto.clear()

"""
    5번 문제
"""

def student() :
    student = {
    "홍길동": 85,
    "이순신": 96,
    "강감찬": 72,
    "유관순": 91
    }
    
    
# bmi()
# avg()
# lotto()
# word()

