class DatePro:
    # 클래스 멤버 변수 => 클래스이름, 변수로 접근이 가능 
    const = '날짜 처리 클래스' # 클래스 변수는 클래스 수준에서 선언된 변수로, 모든 객체가 공유유
                              # 클래스 이름 (DapePro.const) 으로 직접 접근 가능능
    def __init__(self, year, month, day):
        # 생성자에서 self.변수 => 객체.변수 => 객체이름.변수형식으로 접근
        self.year = year # 인스턴스 변수 초기화
        self.month = month
        self.day = day

    def display(self): # 인스턴스 메서드는 객체(date)를 통해 호출되며, 객체의 인스턴스 변수에 접근 가능능
        print(f"{self.year}-{self.month}-{self.day}")

    # 클래스 메서드, @classmethod 데코레이터와 cls를 사용해 정의, 클래스 자체 cls에 접근할 수 있으며, 인스턴스와 독립적으로 동작
    @classmethod
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")

date = DatePro(2025,1,18) # 생성자 __init__ 호출되어서 year month day 초기화화

# date 객체 이름으로 멤버 변수, 멤버 메서드(함수) 접근
print(date.year, date.month, date.day)
print(date.const) # 클래스 변수 const 에 접근
print()
date.display()
#-----------------------------------# 
# 클래스 이름으로 접근 불가능
#-----------------------------------# 
# DatePro.year
# DatePro.display()
# ----------------------------------#

# 클래스 멤버 : 클래스이름. 변수
print()
print(DatePro.const) # 클래스 이름으로 클래스 변수 const에 접근 
DatePro.date_string('20300118') # 클래스 메서드 date_string 호출, cls는 DatePro 클래스를 참조, dateStr 에서 연도 월 일을 분리하여 출력

# 클래스 변수, 메서드는 객체이름으로 접근이 가능
date.date_string('20300118') # 클래스 메서드는 객체를 통해서도 호출 가능
print(date.const)

# 요약
# 클래스 변수는 클래스와 객체 모두로 접근 가능하며, 모든 객체가 공유
# 클래스 메서드는 클래스 레벨에서 동작하며, 클래스 이름이나 객체로 호출 가능
# 객체로 클래스 멤버에 접근 가능하지만 ,명확성을 위해 클래스 이름으로 접근하는 것이 좋음
