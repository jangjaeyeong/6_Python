def divide(data):
    try:
        ch = int(data)
        result = 100/ch

    except ValueError:
        print(f"{data} : 숫자 아님")
    except ZeroDivisionError:
        print(f"{data} : 0 나술수없음")
    except Exception as e:
        print(f"{data} : {e}")
    else:
        print(f"결과 : {result}")
    finally:
        pass

for t in ["100","-5","abc","0"]:
    divide(t)

print("="*60)

class NoBalanceError(Exception):
    """ 잔액 부족 예외 """
    def init(self, balance,amount):
        self.balance=balance
        self.amount = amount
        super().init(f"잔액 부족 : 현재 {balance} , 요청 : {amount}")

class InvalidAmountError(ValueError):
    """ 금액이 잘못된 경우 예외 """

class Account:
    """ 은행 계좌를 나타내는 클래스 """
    def __init__(self , owner , balance = 0):
        self.owner = owner
        self.balance=balance

    def withdraw(self, amount):
        """
            계좌에서 출금하는 메소드

            Args:
                amount (int) : 출금할 금액
        """
        if amount <= 0:
            raise InvalidAmountError("출금액은 0보다 커야 함")

        if amount > self.balance:
            raise NoBalanceError(self.balance,amount)

        self.balance -= amount
        return amount


acc = Account("김동주", 10000)
try:
    for amount in [5000,50000,-1000]:
        acc.withdraw(amount)
except Exception as e:
    print("이머전시!! 이머전시!! 삐 용 삐 용")
    print(e)