# 단어 빈도수 구하기 

charset = ['abc', 'code','band','band','abc']

wc = {} # set, dict , wc는 딕셔너리로 가정됨

for key in charset: # 리스트 객체
    print(key, wc.get(key), wc.get(key,0)) # wc.get(key,0) 은 기본값은 무시하고 뒤의 값만
    wc[key] = wc.get(key,0) + 1 # 딕셔너리 wc를 사용하여 단어의 등장 횟수를 세는 로직직
    print(wc)

print('-' * 40)

test = {}
print(test.get('name')) # None 반환

test['name'] = 1 # name 키가 없으면 키를 추가하고 1을 설정
test['name'] = test.get('name', 0)
print(test)

test['name'] = test.get('name',0) + 1 # name 에 반환 값이 있으면 거기다가 1더하고 가면됨
print(test)

test['name'] = test.get('name',0) + 1
print(test)