# 대입 연산자 +,=,*,/ => +=, -=, /=, *=
i = tot = 10 # 숫자 10을 먼저 tot에 tot를 i 에
print(i, tot)

i += 1 # i = i + 1
print(i)

i += 1
print(i)

i += 1 
print(i)

i *= 3
print(i)

i /= 2 # i = i / 2
print(i)

v1, v2 = 100, 200 # 스왑왑
print(v1, v2)

v1 , v2 = v2 , v1
print(v1, v2)

# 변수 : 단일 기억 장소
# 리스트 구조 : 여러 개의 데이터를 순차적으로 보관

list1 = [1,2,3,4,5]
print(list1, list1[0], list1[1], list1[2])

v1, *v2 = list1
print(v1, v2)

*v1, v2 = list1
print(v1, v2)



# # list1 = [1, 2, 3, 4, 5]

# # 첫 번째 값은 v1, 나머지는 v2
# v1, *v2 = list1
# print(v1)  # 출력: 1
# print(v2)  # 출력: [2, 3, 4, 5]

# # 첫 번째와 두 번째 값은 각각 v1, v2에 할당, 나머지는 v3
# v1, v2, *v3 = list1
# print(v1)  # 출력: 1
# print(v2)  # 출력: 2
# print(v3)  # 출력: [3, 4, 5]

# list1 = [1, 2, 3, 4, 5]

# # 첫 번째 값: v1, 마지막 값: v3, 나머지 값들: v2
# v1, *v2, v3 = list1
# print(v1)  # 출력: 1
# print(v2)  # 출력: [2, 3, 4]
# print(v3)  # 출력: 5