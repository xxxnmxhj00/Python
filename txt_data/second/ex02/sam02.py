# 제어문 : 프로그램 흐름을 제어
# if while for

# 단순 if, if else, elif 문
# num = 10
# if num > 10:
#     print('num :',num)
#     print('조건이 참인 경우 처리되는 문장')

# print("다음 문장")

# num1 = input("정수: ")
# num1 = int(num1) # 문자형 -> 정수형

# # 단순 if
# if num1 % 2 == 0:
#     print(num1, '짝수')

# if num1 % 2 == 1:
#     print(num1, "홀수")

# 2. if else 문
# if num1 % 2 == 0:
#     print(num1, "짝수")
# else:
#     print(num1, "홀수")

# 3. elif 문
# score = int(input('점수 입력 :')) # 점수 입력
# grade = '' # 점수에 따른 등급

# if score >=85 and score <=100:
#     grade = '우수'
# elif score >= 70: # 85미만 70 이상
#     grade = '보통'
# else : # 70미만
#     grade = '저조'

# print(grade)

# 점수 입력
# 90이상 : A, 80이상 : B, 70 이상 : C, 60 이상 : D, 60 미만 :F

# if 90 <= score <=100:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else :
#     grade ="F"

# print("당신의 점수는 {}이고 학점은 {}입니다.".format(score, grade))
# print(f"당신의 점수는 {score}이고 학점은 {grade}")

# 삼항 연산자 : 변수 = 참인 경우 처리할 내용 if 조건식 else 거짓인 경우 처리할 내용
num = 9
result = 0

if num >=5:
    result = num*2
else:
    result = num+2

result = num*2 if num >=5 else num + 2

print(f"result={result}")