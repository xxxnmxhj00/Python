# 함수 클로저란?
# **클로저(Closure)**는 **"함수와 그 함수가 선언된 환경(context)"**을 함께 저장하는 개념
# Python에서 내부 함수가 외부 함수의 변수를 기억하고 사용할 수 있는 함수를 클로저
# 특히, 외부 함수의 실행이 끝난 뒤에도 내부 함수가 외부 함수의 변수에 접근할 수 있다는 점이 특징

# 핵심 개념
# 1. 내부 함수는 외부 함수의 변수에 접근할 수 있다
# 2. 외부 함수가 종료되어도, 내부 함수는 외부 함수의 변수를 기억하고 계속 사용할 수 있다
# 3. 클로저는 함수와 그 함수가 정의될 당시의 환경(변수상태)를 묶어서 저장

# 클로저의 구조
# 3가지로 구성된다
# 1. 외부 함수 : 내부 함수를 감싸는 함수. 내부 함수가 사용할 변수를 선언
# 2. 내부 함수 : 외부 함수 내부에 정의된 함수로, 외부 함수의 변수를 참조
# 3. 변수 환경 : 내부 함수가 외부 함수의 변수를 캡처하여 저장

# 클로저의 동작 원리
# 1. 외부 함수가 호출되면 내부함수가 정의됨, 내부 함수는 외부 함수의 변수 환경을 캡처함
# 2. 외부 함수가 종료되면 외부 함수의 변수는 일반적으로 사라지지만, 내부 함수가 참조하고 있기 때문에 메모리에서 유지
# 3. 내부 함수는 외부 함수에서 정의된 변수 환경을 계속 사용할 수 있음

# 클로저의 장점
# 1. 상태유지, 외부 함수의 변수를 클로저를 통해 유지할 수 있으므로, 상태를 저장하고 관리하는데 유용
# 2. 데이터 은닉, 외부 함수의 변수를 내부 함수에서만 접근할 수 있으므로, 외부로부터 변수 접근을 차단하는 캡슐화가 가능
# 3. 재사용성 증가, 클로저를 통해 동적으로 생성된 함수를 사용하여 유연한 프로그래밍이 가능



data = list(range(1,101))
print(data)

def out_func(data):
    dataSet = data

    def tot(): # 합계를 계산하는 내부 함수
        tot_val = sum(dataSet)
        return tot_val
    
    def avg(tot_val): # 평균을 계산하는 내부 함수
        avg_val = tot_val / len(dataSet)
        return avg_val
    
    return tot, avg # 내부 함수 tot, avg 의 주소를 반환

# 외부 함수 호출(실행)
total, average = out_func(data)
# out_func(data)가 호출되면서, 입력된 data가 dataset에 저장, 내부함수 tot, avg 주소를 반환
# 반환된 주소는 각각 total, average에 저장, total 은 tot함수처럼, average는 avg 함수 처럼럼

tot_data = total() # tot 함수 실행
print('tot=', tot_data)

avg_data = average(tot_data) # 전달된 tot_val을 바탕으로 평균계산해서 avg_val 반환환
print('avg=', avg_data)

# 실행순서 요약

# 데이터 data가 dataSet에 저장.
# 내부 함수 tot, avg의 주소 반환.
# 반환된 함수는 total과 average로 저장.
# total() 호출:

# tot() 실행 → 데이터 합계 계산 → 결과 반환.
# average(tot_data) 호출:

# avg(tot_val) 실행 → 데이터 평균 계산 → 결과 반환.


def double(x):
    return 2 * x

def func_with_print(f) : # f에는 double() 함수 주소
    def new_func(x):
        y = f(x) # 전달된 함수(f)를 호출하여 결과를 y에 저장
        print(y) # 계산된 y 값을 출력

        return y # y 값을 반환
    return new_func
# func_with_print(f)는 매개변수로 전달된 함수(f)를 사용하여, 새로운 기능을 추가한 내부함수 new_func 반환
# new_func(x)는 입력값 x를 전달받아, 함수 f(x)를 호출
# 결과값 y 를 출력
# 결과값 y 를 반환

new_double = func_with_print(double)
# func_with_print(double) 매개변수 f로 double 함수가 전달됨
# 내부함수 new_func가 정의됨, 내부함수 new_func의 주소가 반환되고 변수 new_double에 저장됨
# new_double 은 new_func 처럼 동작

print(new_double(5))
# new_func(5)를 호출하는 것과 동일


# 획득자와 지정자(getter, setter)
def main_func(num):
    num_val = num # 변수 선언하고 매개변수 num 받음음

    def getter():
        return num_val # 외부함수 num_val 참조조
    
    def setter(value):
        nonlocal num_val # nonlocal은 내부 함수에서 외부 함수에 선언된 변수 num_val 을 수정할 수 있도록 해줌, 사용하지 않으면 내부에서 새로운 지역변수를 생성성
        num_val = value

    return getter, setter

getter , setter = main_func(100) # 반환된 getter setter을 변수 getter setter 에 저장

# 추가 정리: nonlocal의 역할
# nonlocal 키워드 없이 setter 함수에서 num_val = value를 실행하면, num_val은 지역 변수로 생성되고 외부 변수와는 독립적으로 동작합니다.
# 하지만 nonlocal 키워드를 사용함으로써 외부 함수(main_func)의 변수를 공유하고 수정할 수 있게 됩니다.

# getter () 함수 실행

print(getter())

# setter() 함수 실행
setter(300) # setter 호출하여 num_val 의 값을 300으로 변경경
print(getter())