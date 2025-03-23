# 함수 장식자 : 데코레이터(decorator)
# 함수 장식자는 다른 함수를 감싸서 그 함수의 동작을 확장하거나 수정할 수 있는 특별한 함수
# 기존 함수를 꾸며서 새로운 기능을 추가하는 도구, 함수 장식자는 주로 재사용, 가독성, 유지보수성을 높이는데 사용

# 함수의 기능을 변경하거나 확장할 경우

# def my_decorator(func):
#     def wrapper():
#         print("함수 실행 전에 이 메시지가 출력됩니다!")
#         func()  # 원래 함수 실행
#         print("함수 실행 후에 이 메시지가 출력됩니다!")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello, world!")

# say_hello()

# @my_decorator 를 사용하면 say_hello 함수가 my_decorator 함수에 전달
# say hello = my_decorator(say_hello) 가 실행된거랑 동일

# 1 say_hello() 호출 시 동작 
# wapper() 함수가 실행돼서 첫 번째 줄에서 메시지가 출력

# 2. 원래 함수 func 실행
# func()는 원래의 say_hello() 본래 내용 메시지 출력

# 레퍼 함수
def wrap(f):
    def new_decorated():
        print('방가워요') # 시작 부분
        f() # hello() 함수를 지칭
        print('잘가요') # 종료 부분

    return new_decorated # return 하면서 new_decorated() 자동 호출

# 함수 장식 적용
@wrap
def hello():
    print('hello !!!!','홍길동')

hello()

print('-' * 20)

def func_with_print(f): # double() 함수 주소 전달 
    def new_func(x):
        print('double()함수 실행 전 처리하는 내용')
        y = f(x) # y= double(x)
        print(y)
        print('double() 함수 실행 후 처리하는 내용')
        return y
    return new_func

@func_with_print # double 함수를 데코레이터로 감쌈
def double(x):
    return 2 * x

r1 = double(5)
print(r1)