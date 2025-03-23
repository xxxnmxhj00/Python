# 사용자 정의 함수

# def 함수 이름():
#     수행할 내용

# 1. 기능 수행하는 단순 함수 : 매개 변수 없고, 반환 값 없는 형태
# 함수 선언

# def fun1():
#     print('-' * 20)
#     print('전달 받은 인자가 없고 반환 값 없는 함수')
#     print('Fun1()')
#     print('*' * 20)

# # 함수 호출(실행)
# fun1()

# 2. 기능 수행하는 단순 함수 : 매개변수 있고, 반환 값 없는 형태 
# 매개변수란 함수를 호출할 때 전달되는 입력값을 함수 내부에서 받기 위한 변수
# def fun2(name):
#     print('-'*20)
#     print('안녕하세요. ', name ,'님 !!!')
#     print('-'*20)

# fun2('홍길동')
# fun2('동순이')
# fun2('강감찬')

# 3. 기능 수행하는 단순 함수 : 매개 변수 있고, 반환 값 있는 형태

# def fun3(x,y): # 매개 변수
#     print('사칙연산 함수 수행')
#     tot = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     return tot, sub, mul, div (13, 7, 30, 3.333)
# 계산된 4개의 결과를 튜플 형태로 반환
# 반환된 튜플의 각 값을 변수 a b c d 에 할당 

# 함수 실행
# a,b,c,d = fun3(10,3)

# 피타고라스의 정의 함수 만들기
# def pytha(s,t):
#     a = s**2 - t**2
#     b = 2 + s * t
#     c = s**2 + t**2

#     print("3변의 길이: ", a, b, c)
#     return a,b,c # 튜플 (3,4,5) 반환

# a1, b1, c1 = pytha(2,1) # 반환값 저장 a1 = 3, b1 = 4, c1 = 5
# print('함수 반환값:',a1,b1,c1)

# def mysum(start, end):
#     sum = 0 
#     for i in range(start, end + 1):
#         sum += i

#         return sum
    
#     print(mysum(1,10))

# 오버로딩 기능 지원 문제 발생
def a():
    print('hello')
def a(name):
    print(name)
def a(n1,n2):
    print(n1,n2)