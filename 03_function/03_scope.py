"""
    스코프
    
    - 전역변수 : 함수 외부에 선언된 변수
    - 지역변수 : 함수 내부에 선언된 변수. 해당 함수 내에서만 접근 가능
"""

count = 0
data = '--전역--'

def increase1() :
    count = 10
    print(f"conut: {count}")
    
def increase2() :
    global count
    count+=1
    print(f"conut: {count}")
    
    
increase1()
increase2()
print(f"conut: {count}")


def outer():
    data = '--바깥 함수(outer)--'
    def inner() :
        data = '--안쪽 함수(inner)--'
        print(f" ** inner :: data - {data}")
    
    inner()
    print(f" ** outer :: data - {data}")
    
outer()
print(f" ** 전역에서 확인 :: data - {data}")