# 클래스 : 메서드(함수) + 멤버변수(속성)
# 함수(메서드) : 기능수행
# 멤버변수(속성) : 상태 : 데이터 저장소

# 사용자가 원하는 특정한 기능을 가지는 자료형 설계
# 객체 재사용(상속), 객체 캡슐화(정보은닉), ....

# 함수와 클래스 비교
# 클로저와 관련된 예제
# def calc_func(a,b): # 두 개의 매개변수 a, b를 받아서 x, y 에 저장
#     x = a
#     y = b
# # x, y 는 내부함수에서 참조하는 외부함수의 지역변수
# # 지역변수는 특정 함수나 블록 내부에서 선언되고 사용되는 변수, 해당 함수나 블록이 실행되는 동안에만 유효효
#     def plus():
#         add = x + y # x,y는 외부함수 calc_func의 지역 변수이지만, 내부 함수에서 사용가능, 클로저 덕분분
#         return add

#     def minus() :
#         sub = x - y
#         return sub
    
#     return plus, minus # calc_func는 두 개의 내부함수 plus, minus 를 반환환
#                        # 반환된 함수는 외부함수가 종료된 후에도 외부함수 지역변수에 접근 가능능

# # 함수 호출 내부함수를 실행
# p, m = calc_func(10,20) # a, b에 전달하면 x=10, y=20으로 초기화

# print('== 함수 실행 결과 ==')
# print(p(), m()) # 함수는 호출(실행)

# # 클래스

# class Calc_class:
#     # 클래스 안에 선언된 변수 -=> 속성, 상태, 값을 유지
#     # 기본설정 값 : public => 공개형 => 외부에서 접근이 가능
#     x = y = 0

#     # 생성자(특수 함수) : 생성자 키워드 => '__init__'
#     def __init__(self,a,b):
#         self.x = a
#         self.y = b

#     # 메서드
#     def plus(self):
#         p = self.x + self.y
#         return p
#     def minus(self):
#         m = self.x - self.y
#         return m
    
# # 클래스 (객체를 생성하는 구조도) => 생성 => 객체(인스턴스, 참조형)

# # 객체 or 참조형 or 인스턴스 = 클래스()
# myCalc = Calc_class(10,20) # 생성자 호출
# print('== 클래스로 생성된 객체 ==')
# print(myCalc.x, myCalc.y)
# print(myCalc.plus(), myCalc.minus())

print('-' * 100)

# 자동차 구조 설계(클래스)
class Car: # 클래스 수준에서 선언된 변수로, 클래스 전체에서 공유, 이 부분에서 cc= 0 이런건 그냥 초기값 을 설정해 놓은 것이라고 보면 됨
    cc = 0
    door = 0
    carType = None

    # __init__ 생성자 => 객체가 생성되는 시점에 자동 호출해서 값을 초기화
    def __init__(self, cc=0, door=0, carType=None): #매개변수 초기화
        print('생성자 수행합니다')
        # 속성에 초기값 설정
        self.cc = cc
        self.door = door
        self.carType = carType

    # 소멸자(생성자 반대 역할) : 프로그램 종료 시점에 자동 호출
    def __del__(self): # __del__ 객체가 삭제되거나 프로그램이 종료될 때 호출, 자원정리의 역할로 프로그램 종료 시점에 객체의 속성을 정리하거나 메모리 해제 가능
                       # self 는 호출된 객체 car1을 참조, 객체 자신을 참조하는 변수
        print('소멸자 수행합니다')
        print(self.cc)

        # 변수 무효화
        del self.cc
        print(self.cc)

    # 메서드
    def display(self):
        print('자동차는 %d cc이고, 문짝은 %d개, 타임은 %s' %(self.cc, self.door, self.carType))
    
# 객체 생성 : 객체.변수, 객체.메소드()
car1 = Car(2000, 4, '승용차')
# car 클래스의 객체 car1을 생성
# __init__을 호출 , cc = 2000, door = 4, carType ='승용차' 전달되고 self에 저장
# 출력메시지 출력
# car1 은 Car 클래스의 인스턴스로 생성된 구체적인 실체이므로 객체의 속성은 car1을 통해 접근해야 한다.
# 속성은 객체에 저장되며, 객체를 통해서만 접근할 수 있으므로 car1.cc, car1.door, car1.carType으로 
print(car1.cc, car1.door, car1.carType)
car1.display()

car2 = Car(3000, 2, '승용차')
car2.display()

car3 = Car()
car3.display()

print(f"car1 주소 : {id(car1)}, car2 주소 : {id(car2)}, car3 주소 : {id(car3)}")