# inch 단위 => cm 단위로 변경
# 키보드로 부터 inch 단위 입력

# inch = int(input('inch 단위와 숫자를 입력해주세요 : '))
# cm = inch * 2.54

# print(inch, '=>', cm)

# 지방(fat), 탄수화물(carbohydrate), 단백질(protein) 칼로리의 합계를 계산
# 지방, 탄수화물, 단백질의 그램을 키보드로 입력
# 총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4

# fat = int(input('지방 : '))
# carbohydrate = int(input('탄수화물 :'))
# protein = int(input('단백질 : '))

# carlories = ((fat * 9) + (carbohydrate * 4) + (protein * 4))
# print(fat, carbohydrate, protein, carlories)

# split

exp = "X + Y + Z = 12"
l = exp.split('=')
print(l)

v = l[0].split("+")
print(v)