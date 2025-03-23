# 함수의 객체화(주소 개념)

def mul(a,b):
    return a * b

mul2 = mul # mul 주소를 mul2에 저장
print(id(mul2), id(mul))
print(mul2(3,4))

print()

# 매개변수 -> 인자값 (데이터), 함수식(함수의 주소)도 전달 가능

def func01(f): # f 라는 매개 변수를 받아 동작
    print("f(2,3)={}".format(f(10,20))) # f를 호출하여 f(10,20)의 결과를 출력력

def func02(a,b): # 두 매개변수 a, b를 받아 곱셈 결과 반환
    return a*b

# 실행순서로는 fun01 fun02 가 먼저 정의됨, 이 단계에서는 함수의 정의만 이루어지고 호출되거나 실행되지 않음
# r1에서 fun02가 호출되면서 a = 10, b = 20 전달되고 결과 200반환 후 변수 r1에 저장장
# r2 는 fun02 함수의 메모리 주소를 저장 
r1 = func02(10,20) # 여기는 fun02가 호출 되는 것 200 저장
r2 = func02 # 함수의 메모리 주소를 저장

print(r1, r2(100,200), id(func02), id(r2)) # 200 20000 id둘이 같음

def func03():
    def new_func03(a,b): # (1) 내부 함수 정의
        return a * b # a와 b를 곱한 결과를 반환 
    
    return new_func03 # new_func03()함수를 종료 # 내부함수 new_func03을 반환
    # func03은 new_func03을 반환하는 구조로 설계, fun03 호출 시 내부 함수 new_func03 자체를 반환환

m = func03() # new_func03(a, b) 함수가 정의되지만 실행되지는 않습니다.
             # (3) fun03 호출, 반환된 new_func03이 m에 저장
             # m은 이제 new_func03 함수처럼 동작
             # fun03은 new_func03 함수의 주소를 반환

print(m(10,20)) # (4) m(10, 20) 호출 및 결과 출력
