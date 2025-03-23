# 특정 글자 수 반환
str1 = 'this is one line string'
print('길이 :', len(str1))
print('t 글자수 :', str1.count('t'))
# str1.은 str1 객체의 메서드나 속성을 호출하겠다는 의미
# Python은 str1이 문자열 객체임을 확인합니다.
# 문자열 객체가 가지고 있는 count 메서드를 호출합니다.
# count('t')는 문자열에서 't'의 개수를 세어 반환합니다

# 특정 문자 비교 판단
# startswith() 메서드는 문자열이 특정 문자나 문자열로 시작하는지 여부를 확인하는 데 사용됩니다. 
# 결과는 항상 True 또는 **False**로 반환
print(str1. startswith('this')) # True
print(str1.startswith('that')) # False 

# 특정 문자 교체
print(str1.replace('this','that'))
print(str1.replace(' ','')) # 공백 제거

# 문자열 분리 
str2 = """\
홍길동
여러줄을 사용하기
길순이 동길이\
"""
print(str2)
sent = str2.split('\n') # 특정 문자기준으로 분리해서 리스트 구조저장장
print('sent =', sent)

sent2 = ','.join(sent)
print(sent2)

print("홍길동\t홍길순\t동\\길이")


# \', \", \\ : c:\abc\ttt.txt
print("홍길동\t홍길순\t동\\길이")
# sent = str2.split(' ')
# print(sent)

# 특정문자 포함여부 판별
print("안녕" in "안녕하세요")
print("Hello" in "안녕하세요")
print(1 in [1,2,4,5] )  # True
print([1] in [1,2,4,5]) # False
print([1] in [1,2,4,5, [1] ]) # True

# 이거 다시 보기 나중에 