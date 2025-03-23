import os
# 1. 텍스트 디렉토리 경로 지정
print(os.getcwd())
txt_data = './txt_data' # 현재 디렉토리 아래에 있는 txt_data 폴더를 가리킴킴
print('1번','-'*50)

# 2. 텍스트 디렉토리 목록 반환
sub_dir = os.listdir(txt_data) # os.listdir(path): 주어진 경로(txt_data)에 있는 모든 파일과 하위 폴더의 이름을 리스트로 반환
print(sub_dir) # ['first','second']
print('2번','-'*50)
# 3. 각 디렉토리의 텍스트 자료 수집 함수
def textPro(sub_dir): # 텍스트 데이터를 분류/수집하기 위해 정의된 함수
    first_txt = [] # first 폴더에서 텍스트 데이터를 수집하기 위한 리스트
    second_txt = [] # second 폴더에서 텍스트 데이터를 수집하기 위한 리스트

    # 3.1 디렉토리 구성
    for sdir in sub_dir:
        dirname = os.path.join(txt_data , sdir)
        print('하위 폴더(디렉토리) 확인:', dirname)
        print('3번','-'*50)

        file_list = os.listdir(dirname)
        print(file_list)

    # 폴더에 있는 파일 목록
    for fname in file_list:
        print(fname)
        file_path = dirname + "/" + fname

        if (os.path.isfile(file_path)):
            try:
                file = open(file_path, mode='r', encoding='utf-8')

                if sdir == 'first':
                    first_txt.append(file.read())
                else:
                    second_txt.append(file.read())
            except Exception as e:
                print('error:', e)
            finally:
                file.close()      

    return first_txt, second_txt  
