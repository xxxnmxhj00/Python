# while 조건식 => 참인 동안 반복 수행
# 처리할 냉ㅇ

# cnt = tot = 0 # 변수 초기화
# while cnt <5: # cnt가 5보다 작으면 반복처리
#     cnt += 1
#     print(cnt, end = ' ') # cnt값 출력

# print()
# print('while end')

# 무한 반복
# while True:
#   pass

# 1번도 수행 안됨
# while False:
#     pass

# 1-100사이 3의 배수 합과 원소 추출 
# count = 0 
# tot = 0
# dataset = []

# while count < 100:
#     count += 1 # 1, 2, 3... 100

# # 3으로 나눈 나머지가 0이면 3의 배수로 판단
#     if count % 3 == 0:
#         tot += count # 3의 배수면 누적적
#         print(count, tot) # +3, +6, +9,...

#         dataset.append(count)

# print(dataset)

while True : # 참인동안 반복 수행
    num = int(input("숫자:"))

    if num == 0:
        break

    print(f"입력된 숫자는{num}")