# 표준 입력 장치 (키보드), 표준 출력 장치 (모니터)
# 키보드를 통해 숫자를 받아서 전송로를 통해서 숫자를 메모리 기억 장소에 넣어줌
# 외부 장치로 부터 넘어온 자료는 스트림 구조
# num = input('숫자 입력:') # 숫자를 넣어주면 된다
# print(num, num*3, type(num))
# print(int(num) * 3) # 정수 문자형 -> 정수형 변환환
# print(float(num)) # 실수 문자형 -> 실수형 변환

print('n1 =',10, 100+20)
print('010','1234','5678', sep =',') # 앞의 3개 사이를 콤마로 구분하겠다
print('010','1234','5678', sep='\n') # 앞의 3개 사이를 띄워쓰기로 구분
print('010','1234','5678', sep='-')
print('-' * 50)

# 1. format() : 형식이 있는 출력을 하고자 할 때 : %f, $%d, %o, %x, %s, $c
print('원주율 =', format(3.14159, "8.2f"))
print('금액 =',format(10000,"10d"))
# 10 은 출력할 전체 자리수(너비)를 10칸으로 설정
# 숫자가 10자리 보다 작으면 오른쪽 정렬을 기본으로 하고 , 왼쪽에 공백을 추가
#'d' 정수를 나타냄
print('금액 =', format(10000,"3,d")) 
# 최소 출력 너비를 3칸으로 설정, 숫자가 3칸보다 크더라도 전체 값은 그대로출력
# , 숫자를 1000단위로 쉽표를 삽입해 가독성을 높임

# # GPT 예시
# # 숫자가 너비를 초과 , 공백 없이 그대로 출력
# print(format(1234567890, "5d"))  # 출력: "1234567890" (너비 초과)
# # 왼쪽 정렬
# print(format(123, "<10d"))  # 출력: "123       " (왼쪽 정렬)
# print(format(123, '10d'))
# # 공백 대신 0으로 채우기
# print(format(123,"010d")) # 출력: "0000000123" (총 10칸, 앞에 0으로 채움)
# # 음수처리
# print(format(-123, "10d"))  # 출력: "       -123" (총 10칸, 음수 부호 포함)

# # format 함수의 활용
# # 실수 포맷팅
# print(format(123.456, "10.2f"))  # 출력: "    123.46" (10칸, 소수점 2자리)
# # 문자열 포맷팅
# print(format ('python', '10s')) # 문자열은 왼쪽 정렬되고 남은 4칸은 공백으로 채원짐 

# 2. 
name = '홍길동'
age = 35
price = '125.456'

# print('당신의 이름은 %s이고, 나이는 %d세 이다. 가진 돈은 %.2f원 입니다' %(name, age, price))

# 3.
print("이름 : {}, 나이 : {}세, 가진 돈은 {}원".format(name, age, price))
print("이름 : {2}, 나이 : {1}세, 가진 돈은 {0}원".format(name, age, price))

# 4. 
str1 = f"이름 : {name}, 나이 : {age}, 금액 : {price}"
print(str1)

str2 =f"이름 : {price}, 나이 : {name}, 학력 : {age}"
print(str2)

# 여러 텍스트를 쳐야될 때,
m = """this is
multi line
string"""

print(m) # 줄바꿈 기능 안 넣더라도 쭉쭉 나옴

m = """
this is
multi line
string
"""

print(m)

# 유지하면서 줄바꿈도 안하고 싶다?

m ="""\
this is
multi line
string\
"""

print(m)