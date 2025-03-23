# 산술 연산자 : +,-,*, 나누기 : /, 나머지 : %, 목 : //, **(누승)

n1 = 100
n2 = 20

add = n1 + n2
sub = n1 - n2
mul = n1 * n2

div = n1 / n2
div2 = n1 % n2
div3 = n1 // n2 # 몫

print('add :', add, ',', 'sub :', sub, ',','mul :', mul)
print('div :', div, 'div2 :', div2, 'div3 :', div3)
# python 에서 int 타입에서 int 타입을 나누면 float으로 나옴

print(3**2, 3*2, '홍길동'*2)
print('-'*30)

# 관계 연산자
print(5>2, 5>=2, 5<2, 5<=2, 5==2, 5!=2)

# 논리 연산자
print('- 논리 연산(and,or,not)')
print(5>2 and 3>2 and 4>2) # 모두 True => True
print(5>2 , not(5>2))

# 관계 연산자 논리연산자 둘다 boolean 타입으로 표현


