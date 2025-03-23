# builtin 내장 함수

# print(abs(10), abs(-10))

# 모든 요소가 True => True => and 유사 기능
# all(iterable): 주어진 iterable의 모든 요소가 참(Truthy)이면 True를 반환하고, 하나라도 거짓(Falsy)이면 False를 반환
# print(all([1, True, 10, -15.2])) # -15.2 음수 이지만 0이 아니라 True

# print()

# False 인 데이터 : "",[],{},0
# all**은 함수인데, 함수 호출 시 괄호 ()를 사용해야 하기 때문입니다. 대괄호 []를 사용하면 Python이 함수가 아니라 잘못된 객체 접근으로 해석
# print(all([1,True,10,-15.2,0]))
# print(all([1,True, 10, -15.2, ""]))
# print(all([1,True, 10, -15.2, []]))

# 하나 이상의 요소가 True => True : OR 유사
print(any([0, "", [], {}]))
print(any([0, "", [], {10}]))

print(10, bin(10), hex(10), oct(10)) # 2진수, 16진수, 8진수
print(eval("10+20")) # eval(expression) 함수는 **문자열로 주어진 표현식(expression)을 평가(evaluate)**하여 실행하고, 그 결과를 반환

# 문자의 아스키코드 번호
print(ord('A'), ord('a'))

print([pow(3,2)]) # 리스트 형태의 3의 2승
print(sorted([1,-3,5,4], key = abs)) # key 매개변수를 사용하면 정렬 기준을 지정
# 정렬 기준은 절댓값이지만, 리스트 요소의 원래 값을 유지하여 반환

# Python에서 문자열 비교는 대문자 → 소문자 순서로 처리
# 기본 정렬은 ASCII 값에 따라 정렬 A(65) ~ Z(90), a(97) ~ z(122)

names = ['BANANA', "GRAPE", "apple"]
print(sorted(names))
print(sorted(names, key = lambda x:x.lower())) # 정렬 기준을 문자열을 소문자로 변환한 값으로 지정
# 소문자 변환 결과: ['banana', 'grape', 'apple']

nums = [[500,6], [10,20,30]]
print(max(nums, key = len)) # len 으로 비교해서 더 긴 부분 출력
print(max(nums, key = sum))

n1 = [1,2,3]
n2 = ['one','two','three']
# n3 = 'abc' # n3[0], n3[1], n3[2]
n3 = 'abcdefg'

# n1, n2 각각 요소를 튜플 방식으로 묶어줌
# zip() 함수는 주어진 반복 가능한 객체들(예: 리스트, 튜플 등)을 병렬로 묶어 튜플 형태로 반환
# 첫 번째 요소를 묶음: n1[0], n2[0], n3[0] → (1, 'a', 10)
for item in zip(n1, n2, n3): # item 튜플 요소로 출력
    print(item)

print('-'*40)

names2 = ['홍길동','홍길동','동길이']
for n in names2:
    print(n)
# enumerate(iterable, start=0): 반복 가능한 객체(iterable)**를 받아서 **인덱스와 해당 값을 함께 반환하는 객체(iterator)**를 생성
# iterable의 각 요소에 대해 인덱스와 값을 반환합니다.
# 기본적으로 인덱스는 0부터 시작하지만, start 값을 지정하면 해당 값부터 시작합니다.

for i, n in enumerate(names2, 100): # i: 인덱스 값 (100부터 시작), n: names2의 요소 값.
    print(i, n)

chars = ['*','+','#','&']
for i, c in enumerate(chars,1):
    print(c*i)

# 객체 타입 판별
# isinstance(object, class_or_tuple)
# object: 확인하고자 하는 값 또는 객체.
# class_or_tuple: 확인하고자 하는 클래스(데이터 타입) 또는 클래스들의 튜플.

print(isinstance(100,int), isinstance(10.2, int))
print(isinstance(100,float),isinstance(10.2,float))
print(isinstance(100,str), isinstance("10.2", str))
print(isinstance([1,2],list), isinstance((1,2),list))
print(isinstance([1.2],tuple), isinstance((1,2), tuple))
print(isinstance([1,2], dict), isinstance({'name':'hoing'}, dict))
print(type('abc'), type([]), type({1,2}), type((10,)), type({"age":10}))