# 캡슐화: 클래스 내부의 변수와 메서드를 외부에서 직접 접근하지 못하도록 보호하고, 메서드를 통해 안전하게 접근하도록 설계하는 것을 의미

# 캡슐화의 특징
# 정보은닉 : 클래스 내부 변수에 접근하지 직접 접근하지 못하도록 제한
# __(밑줄 두개)를 변수나 메서드 이름 앞에 붙이면, private(비공개) 속성으로 설정
# 접근 메서드 제공 : 변수를 getter setter 메서드를 통해 안전하게 접근하거나 변경할 수 잇음
# getBalance(getter), deposit, withdraw(setter)

class Account:
    # private 멤버변수
    __balance = 0 # 잔액
    __accName = None # 예금주
    __accNo = None # 계좌번호

    test = 'hong'

    # 생성자 : 멤버 변수 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no
    # 생성자 밑의 def 메서드들: 객체가 수행할 수 있는 기능(동작).
    # 간단히 말해, 객체의 "행동"을 정의한 것으로 보면 됨
    # 메서드는 클래스 내부에서 정의된 함수로, 객체가 수행할 수 있는 행동을 정의
    # 메서드는 이 객체가 할 수 있는 행동이다 라고 생각
    # 계좌 정보 확인
    def getBalance(self):
        return self.__balance, \
               self.__accName, \
               self.__accNo, \
               self.test
    
    # 입금하기(setter)
    def deposit(self,money):
        if money<0:
            print('금액 확인')
            return
        
        self.__balance += money

    # 출금하기(settter)
    def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return
        self.__balance -= money

acc = Account(1000, '홍길동', '111-123-1234-12')
bal = acc.getBalance()
print(bal, type(bal))

    # acc-__balance # Error: private 외부에서 접근 불가능 
acc.test # public 외부에서 접근 가능

    # 메서드를 통해 멤버변수 값을 설정 
acc.deposit(10000)
bal = acc.getBalance()
print(bal, type(bal))

acc.withdraw(10000)
bal = acc.getBalance()
print(bal, type(bal))

acc.withdraw(10000) # 잔액 부족
acc.deposit(-10)