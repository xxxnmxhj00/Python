# lib 안에 json 모듈이랑 이런거
# 파이썬 : 모듈과 패키지 형태로 라이브러리를 제공
# 모듈은 다수의 함수나 클래스(class)를 묶어서 파일형식(*py)으로 제공

# 함수 : 특정 기능을 수해하는 단위 프로그램
# 내장함수 : builtins 라는 모듈

# 형식
# 1. import 모듈명 : import random 구분 없이 원하는 내용 다 불러와서 사용
# 2. from 모듈명 import 함수면1,... 특정한 함수만 불러와서 사용

# builtins 모듈에 있는 함수
dataset = list(range(1,6))
print(dataset)

# len, sum, max, min ... 내장함수는 import 과정 생략
print(f"len={len(dataset)}")
print(f"sum={sum(dataset)}")
print(f"max={max(dataset)}")
print(f"min={min(dataset)}")

# import가 필요한 함수(builtins 모듈에 없는 함수)
# print("평균 =",mean(dataset)) # mean은 안들어간 함수라서 안됨

import statistics # 수학적 통계 연산을 수행할 수 있는 다양한 함수들을 제공
print("평균 =", statistics.mean(dataset))
print("중위수 =",statistics.median(dataset))
print("표본 분산 =",statistics.variance(dataset))
print("표본 표준편차=",statistics.stdev(dataset))

print()

# 두번째 방법
from statistics import variance,stdev # 모듈안에 함수 지칭
print("표본분산 =", statistics.variance(dataset)) # statistics를 쓸 필요가 없음
print("표본 분산 =", variance(dataset))
print("표본 표준편차=", stdev(dataset))
