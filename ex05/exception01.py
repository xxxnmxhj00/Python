# # try ~ except ~ : 시스템에 Error가 발생 시 정상적인 종료
# # 예외 발생 코드

# print("프로그램 시작하기!!!")

# x = [10, 30, 25.2, 'num', 14, 15]

# for i in x:
#     try: # 예외가 발생할 가능성이 있는 코드
#         print(i)
#         y = i ** 2  # 들여쓰기를 4칸 공백으로 맞춤
#         print('y=', y)
#     except: # 예외가 발생했을 때 실행할 코드
#         print('숫자 아님: ', i)

# print('프로그램 종료하기!!!')

# 비 정상적인 종료를 막기 위해 예외 처리를 해줌

print("-" * 20)
print("다중 예외 처리 프로그램 시작!!!")
list1 = [10,20,30]

try:
    div = 1000 / 2.25 # 0으로 나눌 경우 예외 발생
    print('div = % 5.2f'%(div)) 
    # 숫자를 소수점 2자리까지 출력하며, 전체 최소 너비가 5칸 
    # 123.45 12.3 이면 ( 12.30)

    print(list1[100]) # indexerror 100은 범위 초과
    # 여기서 indexerror가 발생해서 try 블록의 남은 코드는 실행되지 않음
    
    f = open('c:\\test.text') # 파일 열기 에러 발생
    # 파일이 없거나 경로가 잘못되면 **FileNotFoundError**가 발생합니다.
    num = int(input('숫자 입력:'))

except ZeroDivisionError as e :
    print('산술적 예외 처리 발생')
    print('오류 정보: ', e)
except FileNotFoundError as e :
    print('파일 열기 예외 처리 발생생')
    print('오류 정보: ', e)    
except IndexError as e : 
    print('인덱스범위 예외 처리 발생')
    print('오류 정보: ', e)
except Exception as e:
    print('기타  예외 처리 발생')
    print('오류 정보: ', e)

    
print("프로그램 정상 종료하기")