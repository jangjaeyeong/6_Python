

class Loggable:
    def lig(self, message) :
        return f"[LOG] {message}"
    
class Serializable:
    def to_dict(self) :
        return self.__dict__
    
class Product(Loggable, Serializable):
    def _init_(self, name, price):
        self.name = name
        self.price = price
        
        
p = Product("커피", 2000)

print(f"{p.log('상품을 생성했습니다.')}")
print(f"dict --> {p.to_dict()}")