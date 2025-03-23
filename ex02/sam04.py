# # for

# str ="홍길동홍길순동길이" # 스트링은 기본적으로 리스트 구조
# print(str)

# for name in str:
#     print(name, end = " ")

# nums = [1,2,3,4,5,6,7,8,9,10]

# for n in nums: # 순차적으로 불러오는 것
#     if n % 5 == 0: # 5의 배수가 아니면 다시 위로
#         print(n, end = ' ')

# for, range : 숫자 발생 객체
# n1 = range(5)  # 리스트는 아닌데 리스트 형태의 구조가 나온다
# for n in range(5):
#     print(n)
# for n in range(1,5+1):
#     print(n, end = " ")

# for n in range(1,10+1,2):
#     print(n, end = " ")

# print(n) # 이건 줄바꿈을 얘기하는것

# 난수 발생 모듈 임포트

# import random

# list1 = []
# for i in range(10): # 0~9 반복 횟수
#     r = random.randint(1,10) # 아무 숫자나 만들어주는 것 난수 발생

# # 난수 발생 후 저장소에 유무 체크

#     list1.append(r) # 리스트에 저장
#     print(r, end = " ")

# 처음 r에 난수 발생되고 while로 내려와서 값이 없으면 false가 되서 밑으로 
# 총 10개의 난수가 다 채워질 때 까지 반복

# import random 
# list1 = [[],[],[],[],[]] # 2차원 리스트로 5개의 빈 리스트를 포함함

# for out in range(5): # 바깥쪽 반복문으로, 5개의 리스트(list1[0], list1[1], ..., list1[4])에 각각 난수를 저장하기 위해 5번 반복

#     for i in range(6): # 안쪽 반복문으로, 각 리스트에 6개의 난수를 생성하고 저장하기 위해 6번 반복
#         r = random.randint(1,45)

#         while r in list1 : # r값이 list1에 있으면 반복 수행
#             r = random.randint(1,45)

#         # 난수 발생 후 저장소에 유무 체크
#         list1[out].append(r) # 리스트에 저장
#         print(r, end = " ")