# 클래스 멤버 : 클래스 이름으로 호출할 수 있는 클래스 변수, 클래스 메서드
# 클래스 멤버는 클래스 자체를 통해 접근하거나 호출할 수 있으며, 인스턴스(객체)를 거치지 않아도 사용 가능
# 클래스 메서드는 'cls' 기본 인수 사용, @classmethod 라는 함수 장식자 사용

# 1. 클래스 변수 : 클래스 변수는 클래스 내부에서 선언된 변수로, 클래스 전체에서 공유됨
# 특징, 모든 인스턴스(객체)가 공유한느 변수, 클래스 이름으로 직접 접근 가능, 인스턴스에서도 접근 가능하지만 값 변경 시 주의가 필요

class MyClass:
    class_var = '클래스 변수' # 클래스 변수 선언

# 클래스 이름으로 접근
print(MyClass.class_var)

# 인스턴스를 통해 접근
obj = MyClass()
print(obj.class_var) 

# 2. 클래스 메서드 : 클래스 메서드는 클래스 자체를 다루기 위한 메서드로, 클래스 전체에 영향을 미치는 작업을 수행할 때 사용
# 특징, @classmethod 함수 장식자를 사용해 정의, 첫 번째 매개변수로 클래스 자체를 나타내는 cls를 받는다, 클래스 이름으로 호출할 수 있으며, 인스턴스에서도 호출 가능

class Myclass:
    class_var = 0 # 클래스 변수
    
    @classmethod
    def class_method(cls, value): # cls가 클래스를 나타냄
        cls.class_var = value # 클래스 변수 값 변경
        print(f"클래스 변수 값이 {cls.class_var}로 변경되었습니다.")

# 클래스 이름으로 호출, 호출방식이 클래스 이름 또는 인스턴스로 호출
Myclass.class_method(100) # 출력 : 클래스 변수 값이 100으로 변경

# 클래스 변수 확인 
print(Myclass.class_var)