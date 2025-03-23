import os.path # 파일 경로와 디렉토리 경로를 처리하기 위한 유용한 함수들을 포함함
# 경로의 유효성 검사, 경로 결합, 디렉토리명/파일명 추출 등이 가능
# 주로 파일/폴더 작업을 할 때 사용됨

# 현재 경로 확인 
# path = os.getcwd()
# print('현재 위치 :', path)

# # 경로 변경
# os.chdir('ex06/data')
# print('변경된 위치 :', os.getcwd())

# 절대 경로, 파일이나 디렉토리의 위치를 루트 디렉토리에서부터 시작하여 나타내는 전체 경로를 말함
# 루트 디렉토리 : 파일 시스템의 가장 최상위 디렉토리 ex) c:\ or D:\
# 특징은 파일이나 디렉토리의 유일한 위치를 나타냄, 경로는 루트 디렉토리에서부터 시작하므로 항상 완전한 형태로 표현

# 상대경로는 현재 작업 디렉토리 기준으로 경로를 나타냄
abspath = os.path.abspath('ex06/data/appendfile.txt')
print(abspath)

# # # 파일 유무 체크
isfile = os.path.isfile('test01.txt')
print('파일 유무 체크', isfile)
print('파일 유무 체크', os.path.isfile('test02.txt'))

# 폴더 유무 체크
print(os.path.isdir('ex06'))

path_split = os.path.split('ex06/data.appendfile.txt')
print('경로와 파일 분리:', path_split, path_split[-1])
# os.path.split()는 경로를 마지막 구분자(/ 또는 \)를 기준으로 나눕니다.

file_size = os.path.getsize('ex06/file01.py')
print('파일 크기:', file_size/1024, 'kB')