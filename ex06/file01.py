# 텍스트 파일 : 텍스트 자료를 읽어온 자료를 처리하고, 처리 결과를 파일에
# 파일 생성, 파일 읽기 가능
# open(file, mode(r,w,x,a,b), encoding)

# 현재 디렉토리
import os # 시스템과 관련된 명령어를 처리할 수 있는 모듈, os모듈듈
print(f"현재 경로: {os.getcwd()}")

# 예외 처리 # 출발위치는 현재 python 01

try:
    # 파일 열기
    # ftest1 = open('test01.txt, mode = 'r', encoding = 'utf-8')
    ftest1 = open('C:\python01\ex01\sam01.py', mode = 'r', encoding= 'utf-8')
    #print(ftest1.read())
# 닫아주고 열고 해야되니까 여기서 한번 read한걸 닫아주고 그 다음 다시 가서 ftest2 에서 read를 실행하면
# sam02 파일에 복사가 되서 내용이 그대로 전달됨

    # 파일 쓰기(저장)
    ftest2 = open('ex06/data/sam02.py', mode = 'w', encoding='utf-8')
    # ftest2.write('파일 저장하기')
    ftest2.write (ftest1.read())

    # 파일쓰기 , 없으면 생성하고 있으면 기존 인덱스를 계속 추가
    ftest3 = open('ex06/data/appendfile.py', mode = 'a', encoding= 'utf-8')
    ftest3.write('Hello Python!!!!\n')

except Exception as e:
    print('Error 발생 : e')