# 문자열 색인 => 리스트 구조 형식
#   "012345"
#   "-6-5-4-3-2-1"
s = "PYTHON"
print(s)
print(s[0], s[1], s[2], s[3], s[4], s[5])
print(s[-6], s[-5], s[-4], s[-3], s[-2], s[-1])

# 잘라서 범위를 줄 수 있는 것이 슬라이싱(slicing)
# 문자열 [인덱스 번호], 문자열 [시작 : 끝 번호 : 증감값]

print('문자열 길이 :', len(s))
print(s[0:4]) # start, end - 1
print(s[:4])
print(s[:])
print(s[::2])

# 반대방향, 우측 기준
print(s[-1],s[-2])
print(s[-6:-1])
print(s[-6:])

## 지금 부터 cmd 들어가서 python 하고 import keyword
#print(keyword.kwlist) 안에 있는 단어들은 기억장소 용도로는 쓰지 못한다. 즉 키워드, 식별자라고 얘기한다.
# Microsoft Windows [Version 10.0.19045.5131]
# (c) Microsoft Corporation. All rights reserved.

# C:\Users\605>python
# Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import keyword
# >>> print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# (f-search `')

# 숫자 영자 언더바를 혼용해서 변수 이름을 지정 할 수 있다 a_10
# 숫자를 첫 단으로는 사용하지 못한다

print('-'*20)
list1 = [100,200,300]
list2 = ['홍길동', '홍길순']
list3 = list1 + list2
# list4 = [1,2,3] + 100 # 타입이 리스트랑 int랑 안맞아서 아에 안됨
# 리스트와 정수간의 덧셈은 지원하지 않음
# 리스트와 리스트끼리만 덧셈이 가능함

list4 = [1,2,3] + [100]
print(list4)  # 출력: [1, 2, 3, 100]
print(list3)

list4 = [1,2,3] + [100]
print(list4)

list5 = [1,2,3,[100,200],[10,20],['a','b']]
print(list5)

print(list5[0])
print(list5[1])
print(list5[2])
print(list5[3])
print("=" * 50)
print(list5[3][0])
print(list5[3][1])
print(list5[3][0], list5[3][1])
print("=" * 50)
print(list5[4])
print(list5[4][0],list5[4][1])
# # append 메서드 사용
# list6 = [1, 2, 3]
# list6.append(100)
# print(list6)