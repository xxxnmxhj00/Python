# 실수 -> 정수 : int(실수형형)
a = int(10.5)
b = int(20.42)
add = a + b
print('add =',add) # print()는 문자열로 표시

# 정수 -> 실수 : fload(정수)
a1 = float(10)
b1 = float(20)
add1 = a1 + b1
print('add1 =', add1)

# 논리형 -> 정수 boolean
print(int(True), int(False)) # 0일때만 False, True는 1

# 문자형 -> 정수
st ='10' # 문자, 문자 10이랑 숫자 3이 연산이 안됨
print(int(st) + 3)