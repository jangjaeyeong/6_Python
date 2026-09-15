"""
    클래스와 객체
    -기본 형태-
    class 클래스명:
        #생성자
        def __init__(self):
        self.필드명 = 값
        
        #메서드
        def 메서드명(self):
            pass #실행할 내용
"""

class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount) :
        self.balance += amount
        return self.balance
    
acc = Account("김동주", 10000)

print(f"owner: {acc.owner}")
print(f"balance : {acc.balance}")

print(f"deposit : {acc.deposit(7000)}")

print("="*60)

#인스턴스 변수 vs 클래스 변수

class Member:
    team_name = "리센느"
    count = 0
    
    def __init__(self, name):
        self.name = name
        Member.count+=1
        
m1 = Member("원이")
m2 = Member("미나미")

print(f"m1.name : {m1.name}")
print(f"m2.name : {m2.name}")


print(f"m1.name : {m1.team_name}")
print(f"m1.name : {m2.team_name}")
        
print(f"count: {Member.count}")

m1.team_name = "RESCENE"
print(f"m1.name : {m1.team_name}")
print(f"Member.team_name : {Member.team_name}")