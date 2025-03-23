# 일급함수와 함수 클로저

# 특징 1. 함수를 변수에 할당할 수 있다.
# - Python 에서는 함수를 변수에 저장할 수 있다
# - 이 변수는 이후 함수처럼 호출될 수 있다
def greet(): # 함수 greet 정의
    print("Hello, world!")

# 함수를 변수에 할당
say_hello = greet

# 변수로 함수 호출
say_hello()  # 출력: Hello, world!

# 특징 2. 함수를 다른 함수의 인자로 전달할 수 있다.
# 함수는 다른 함수의 매개변수로 전달될 수 있다
# 이를 통해 고차함수를 구현할 수 있다
def square(x): # x 제곱을 반환하는 함수
    return x ** 2

def apply_function(func, value): # 매개변수로 func, value를 받는다다
    return func(value)

# 특징 3. 함수 square를 다른 함수에 인자로 전달
result = apply_function(square, 5) # square 함수가 func로 전달, square라는 함수가 apply_function 함수에 입력값을 전달된다는 뜻뜻
print(result)  # 출력: 25 func(value)는 square(5) 가 전달되어 25를 반환

# applty_function(square, 5)에서 square 함수가 func로 전달
# func(value)는 square(5)가 되어 결과 25를 반환

# 함수를 다른 함수의 반환값으로 사용할 수 있다.
def outer_function():
    def inner_function():
        print("This is the inner function!")

    return inner_function

# outer_function을 호출하면 내부에서 inner_function 함수가 정의됩니다.
# 이 함수는 실행되지 않고, 메모리에 저장된 함수 객체가 생성
# return inner_function:
# 이 구문은 **inner_function 함수 객체의 참조값(주소)**를 반환

# 함수 호출 
returned_function = outer_function()
# outer_function 을 호출하면 inner_function 의 주소가 반환되어 returned function에 저장

returned_function()
# 이제 inner_function 처럼 동작하며, 이를 호출하면 inner_function 의 동작이 실행



# 1. 일급함수
def a():  # outer function
    print('a()함수: outer function')

    def b():  # inner function
        print('b()함수 : inner function')

    print('a()함수 종료 시 b()함수의 주소를 반환')
    return b  # 내부 함수 b의 주소 반환

f1 = a()  # a() 호출, b 함수의 주소 반환되어 f1에 저장
# 일단 a() 에서 print하고 b 주소값 저장
f1()  # f1() 호출, 즉 b() 실행
# a() 호출 시 내부 함수 b()는 정의만 되고 실행되지 않음
# 그래서 함수가 정의된 이후 print 문이 실행되는 것

# b()가 실행될 때는 이미 a() 함수는 종료된 상태이기 때문에 마지막 print를 실행하지 않음

