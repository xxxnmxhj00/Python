# 상속
# 상속은 객체지향 프로그래밍의 주요 개념 중 하나로, 기존 클래스(부모 클래스, 슈퍼 클래스)의 속성과 메서드를 자식 클래스(하위 클래스, 서브 클래스)가 물려받는 것을 의미
# 상속의 주요 특징
# 1. 코드의 재사용성:
# 부모클래스에서 정의한 속성과 메서드를 자식 클래스가 그대로 사용할 수 있음, 중복 코드를 줄이고 유지보수 용이
# 2. 확장성:
# 자식 클래스는 부모 클래스의 기능을 확장하거나, 자신만의 고유한 속성과 메서드를 추가할 수 있음
# 3. 다형성:
# 동일한 메서드를 부모와 자식 클래스에서 다른 방식으로 정의(오버라이딩) 하여 호출된 객체의 타입에 따라 다르게 동작하게 만듬

# 부모 클래스(슈퍼클래스, 상위클래스) : 공통 기능을 가진 클래스
# 자식 클래스(하위 클래스, 파생 클래스) : 공통 기능을 확장하는 클래스

# 부모 클래스 (공통 기능)
class Super: # 부모 클래스로 name, age 속성을 가짐
    def __init__(self, name, age): # __init__ 생성자가 객체가 생성될 때 실행되며 속성을 초기화
        print('부모 클래스 생성자 호출')
        self.name = name
        self.age = age

    def display(self): # display() 메서드는 name, age 를 출력하는 기능을 가짐
        print(f"name: {self.name}, age: {self.age}")

# 부모 클래스로 객체 생성
sup = Super('부모 클래스', 55)
# 호출해서 객체 sup을 생성, __init__() 실행하고 " 부모 클래스 생성자 호출 출력력"
# self.name '부모 클래스', self.age 55 메모리에 저장
sup.display() # name : 부모 클래스, age : 55 출력

print('-' * 20)

# 하위 클래스(공통 기능 확장)
class Sub(Super): # 클래스(부모클래스 이름) => 상속 개념, Super 클래스를 상속받아 Sub 클래스를 생성
    gender = None # 

    def __init__(self, name, age, gender):
        # 상위 클래스 멤버 변수 초기화 : 생성자 호출 => Super()
        super().__init__(name, age)
        print('자식 클래스 생성자 호출')

        # gender 자식 클래스의 자원 
        self.gender = gender # gender 속성을 차가하여 부모 클래스 보다 확장된 기능을 가짐

    # 오버라이딩(상속 받은 메서드 재정의)
    def display(self):
        print(self.name, self.age, self.gender)

# 자식 클래스 객체 생성
sub = Sub('자식 클래스', 25, '여자')
# 객체 sub 생성 시작, 자식 클래스의 __init__() 실행 -> super().__init__(name, age) 실행
# super().__init__(name, age) 실행되면서 부모 클래스의 생성자가 먼저 실행됨.
# 부모 클래스의 print("부모 클래스 생성자 호출") 출력됨.
# 부모 클래스의 __init__() 종료 후, 다시 자식 클래스의 __init__() 실행됨.
# "자식 클래스 생성자 호출"이 출력됨.
print('--sub display()')
sub.display() # sub.display() 실행 → 자식 클래스의 display()가 실행됨.


print('--- sub 클래스 멤버 변수')
print(sub.name, sub.gender, sub.age)