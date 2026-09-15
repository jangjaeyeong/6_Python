
class Account :
    bank_name = "KH 은행"
    MIN_DEPOSIT = 1000
    
    def __init__(self, owner, balance = 0):
      self.owner = owner
      self.balance = balance
    
    def deposit(self, amount) :
        self.balance += amount
        return self.balance
    
    @classmethod
    def from_dict(cls, data) :
        """
            딕셔너리로부터 객체를 생성하는 메서드
        """
        return cls(data["owner"], data["balance"])
    
    # 메소드 : 객체, 클래스와 무관한 기능을 담당하는 메소드(유틸리티) @staticmethod 지정.
    
    @staticmethod
    def is_valid_amount(amount) :
        return amount >= Account.MIN_DEPOSIT
    
acc = Account("김동주", 10000)
print(f"deposit --> {acc.deposit(3000)}")
    
acc2 = Account.from_dict({"owner": "이동주", "balance" : 10000})
print(f"owner: {acc2.owner}, balance: {acc2.balance}")