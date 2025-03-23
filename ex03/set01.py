# 비순서 자료 구조 : set, dict
# set : 중복 불가. 순서가 없다. 색인이 없다(인덱스가 없다), 추가 삭제 집합 연산 가능

# s ={1,3,4,3,1}
# print(s, len(s), type(s)) # 중복이 없어지는 것을 볼 수 있다

# for d in s:
#     print(d, end =', ')

# print()

# # 집합 연산 (교집합, 차집합 등등)

# s2 = {3,6}
# print('s =', s, 's2 =', s2)
# print(s.union(s2)) # 합집합
# print(s.difference(s2)) # 차집합
# print(s.intersection(s2)) # 교집합

# # 추가
# s.add(10)
# print(s)

# # 삭제 
# s.discard(10)
# print(s)

# 중복 허용하는 리스트 객체
gender = ['남','여','남','여']

sgender = set(gender) # 리스트 구조를 set의 구조로 전환
print(sgender)

lgender = list(sgender) # set 구조에서 list 구조로 전환
print(lgender)

print(gender, lgender)