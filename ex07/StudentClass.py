# 학생
# __init__, 클래스의 생성자로 사용되는 메서드
# 인스턴스로 만들어질 때 자동으로 호출
# 주로 객체가 생성될 때 초기값을 설정하거나 필요한 작업을 수행함
# class MyClass:
#     def __init__(self, arg1, arg2):
#         self.arg1 = arg1  # 인스턴스 변수 초기화
#         self.arg2 = arg2

# # 객체 생성, myclass 클래스의 인스턴스 생성
# obj = MyClass('value1', 'value2')  # __init__ 자동 호출

# 인스턴스란 클래스를 사용해서 생성된 실제 객체
# 클래스는 설계도, 인스턴스는 그 설계도를 기반으로 만들어진 구체적인 실체
# 생성자란 인스턴스를 생성할 때 자동으로 호출되는 메서드


class Student:
    # 생성자 : 멤버변수 초기값 설정
    def __init__(self, name, kor, mat, eng, sci): # 생성자 메서드
        self.name = name
        self.kor = kor
        self.mat = mat
        self.eng = eng
        self.sci = sci
# self 는 생성된 인스턴스를 참조하며, 각 속성을 객체에 저장

    # 기능 수행 함수 선언
    def total(self):
        return self.kor + self.mat + self.eng + self.sci

    def average(self):
        return self.total() / 4

    def to_string(self):
        return "{}\t{}\t{:.2f}".format(self.name, self.total(), self.average())

    # 특수 함수

    def __str__(self):
        return "{}\t{}\t{:.2f}".format(self.name, self.total(), self.average())


if __name__ == "__main__": # 메인 실행 블록 : 이 코드는 현재 파일에서 실행될 때만 동작
    students =[
        Student("홍길동", 100,100,100,100),
        Student("동순이",80,75,65,85),        
        Student("길순이",90,75,65,60),
    ]

    print("이름\t총점\t평균")
    for st in students:
        print(str(st))

# 파이썬에서 클래스의 메서드는 클래스 블록 내부에 정의해야만 해당 클래스의 인스턴스에서 사용할 수 있습니다.
