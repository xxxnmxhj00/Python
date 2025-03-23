# 자료 구조 복제 : 얕은 복사, 깊은 복사
# 얕은 복사는 기존 객체의 메모리 주소를 복사하여 새로운 변수가 같은 객체를 참조하도록 만드는 방식입니다.
# 즉, 원본 객체와 복사된 객체는 동일한 메모리 위치를 참조합니다.
print("-- 객체 주소 복사")
print("1. 얕은 복사 : 주소복사")

name = ['홍길동','이순신','강감찬']
print(f"name={name}")

# name2에 name이 담고 있는 객체 주소를 저장
name2 = name
print(f"name2 = {name2}")

print(f"name 주소 : {id(name)}, name2주소:{id(name2)}")

# 복사본을 수정
# name과 name2는 같은 객체를 가리키므로, name2를 수정하면 name도 영향을 받습니다.
name2[0] = "길순이"
print(f"name={name}")
print(f"name2={name2}")

# 깊은 복사 
# 깊은 복사는 원본 객체의 데이터 구조를 그대로 복제하여 새로운 객체를 생성합니다.
# 복사된 객체는 원본 객체와 다른 메모리 주소를 가지며, 서로 완전히 독립적입니다.
# 원본 객체의 변경이 복사된 객체에 영향을 미치지 않습니다(또는 그 반대도 마찬가지).import copy
import copy
print("2. 깊은 복사")
name3 = copy.deepcopy(name)

print(f"name={name}, name3 ={name3}")
print(f"name주소 = {id(name)}, name3주소 ={id(name3)}")

name3[0] ='동순이김'
print(f"name={name}, name3={name3}")