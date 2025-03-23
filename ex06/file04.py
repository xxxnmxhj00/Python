# with 블럭과 인코딩

try:
    # with 블럭을 벗어나면 자동으로 open 한 객체는 소멸됨
    with open('ex06/test.py', mode = 'w', encoding='utf-8') as ftest:
        ftest.write('파이썬 파일 자석 연습')
        ftest.write('\n 파이썬 파일 쓰기 테스트2')

    with open('ex06/test/py', mode = 'r', encoding= 'utf-8') as ftest2:
        print(ftest2.read())

except Exception as e:
    print('Error 발생', e)

finally:
    print('무조건 수행하는 구간')
    print('자원 해제할 때 사용')