# 튜플(tuple) : 읽기 전용 (수정, 삭제 불가)
# 색인, 슬라이싱, 연결, 반복, 요소검사 등 가능
# 리스트 보다 처리 속도가 빠르다

# lst = [], lst[1], lst = [1,2,2,3,32] 
# 하나 넣든 두개 넣든 상관이 없음

# 1개인 경우
# t = (10) # 괄호 안에 숫자 하나만 있으면 정수로 해석
# t = (10,)
# print(t, type(t))

t2 = (1,2,3,4,5,3,3,3,3,3)
# print(t2, t2[0], t2[4], t2[1:4], t2[1:-6])
# # 수정 불가
# # t2[0] = 100 # error 

# for i in t2:
#     print(i, end = ' ')
# print(100 in t2)
# print(100 not in t2)

# 형 전환
r = range(1,5+1) # 이렇게 하면 range만 나옴, 식만 나옴옴
print(r, type(r))

r = list(range(1,5+1))
print(r, type(r))

t3 = tuple(r)
print(t3, type(t3))

# tuple에 있는 요소 중 특정 데이터 개수
print(t3.count(3), t2.count(3), t2.index(3))
# index(값) , 첫 번째로 등장하는 위치를 반환

