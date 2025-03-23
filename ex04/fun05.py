# 가변 인자 함수
# '*', '**' 기호를 붙여 사용
# *매개변수, 위치 기반 인자를 여러 개 받을 때 사용, 전달된 값은 튜플형태저장
# **매개변수, 키워드 인자를 여러 개 받을 때 사용
# 전달된 값은 딕셔너리 형태로 저장
# '*매개변수' => tuple, '**매개변수' => dict

def fun1(name, *names):
    print(name) # 첫 번째 매개변수 name 출력
    print(names) # 가변 인자 names 출력 (튜플 형태)
    for n in names: # 안에 있는거 반복
        print(n)

fun1('홍길동','홍길순','동길이','강감찬','이순신')

# names* 나머지 모든 위치 기반 인자를 받고 이 값들은 튜플로 저장

# 첫번째 인자는 n1, 나머지 인자는 n2에 전달(tuple 구조)
# default => 전달받은 값이 없을 경우 기본값으로 설정
def mysum(n1 = 0, *n2): # n1에 값을 제공하지 않을 경우에만 n1 = 0 사용
    sum = 0 # 합계를 저장할 변수 초기화
    sum += n1

    for n in n2:
        sum += n

    print('mysum=', sum)

mysum(1,2,3)
mysum(1,2)
mysum(1,2,3,4,5)

def mycalc(num1 = 100, num2 = 200):
    print(num1, num2)

mycalc()
mycalc(1000)
mycalc(1,2)

# 딕트형 가변 인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)
    print('-' * 10)
    print(other['addr'], other['height'], other['weight'])

    for k in other:
        print(other.get(k)) # 객체.get(key) => value값 호출출


emp_func('홍길동', 35, addr ='서울', height = 178, weight = 65)