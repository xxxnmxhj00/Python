# 딕트(dict) : 키 중복 불가, 값은 중복가능, 키를 통해 값을 호출
# list = [1,2,3] - 리스트, tuple = (12.3.3), set = {1,2,3}
# 딕트 = {'a' : '1',...}

# 1. 생성자를 통해 값 설정 : 키 = 값
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic,type(dict))

# 2. 초기값 설정 : 키 : 값,
person = {'name' : '홍길동', 'age' : 35, 'addr' : '부산시'}
print(person, type(person))

# 3. key로 value를 호출(참조)
print(person['name'], person.get('age'))

# person['name']
# 딕셔너리에서 'name' 키의 값을 직접 가져옵니다.
# 키가 존재하지 않을 경우 에러(KeyError)가 발생합니다

# person.get('age')
# 딕셔너리에서 'age' 키의 값을 가져옵니다.
# 키가 존재하지 않을 경우 None을 반환합니다.
# **기본값(default value)**을 제공할 수도 있습니다

# 4. 추가 / 수정
person['name'] = '동순이' # 수정
person['age'] = 10
person['gender'] = '여자'
print(person)

# # # 5. 삭제
del person['gender']
print(person)

# # 6 유무 체크
print('age' in person, 'gender' in person)

# 7. 반복 
for key in person.keys(): # 키만 추출
    print(key, person.get(key))
for value in person.values(): # 값만 추출
    print(value)

for item in person.items(): # 키와 값 추출
    print(item, item[0],item[1]) # 튜플 형식으로 키와 값 구성성

print(person.keys(), person.values())
print(type(person.keys()), type(person.values()))

# dict 구조 : 값 호출 => dict 객체['키이름']
# dict 객체.get('키이름'), dict 객체.get('키이름',키가 없을 경우 설정할 값)

print(person)
print(person['name'], person.get('age'), person.get('gender','없다고'))