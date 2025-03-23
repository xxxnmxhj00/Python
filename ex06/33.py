import os
# 1. 텍스트 디렉터리 경로 지정
print(os.getcwd())
txt_data = './txt_data/'

# 2. 텍스트 디렉터리 목록 반환
sub_dir = os.listdir(txt_data)
print(sub_dir) # ['first','second']

# 3. 각 디렉터리의 텍스트 자료 수집 함수
def textPro(sub_dir):
    first_txt   = []
    second_txt  = []

    # 3.1 디렉토리 구성
    for sdir in sub_dir: #['first','second']
        dirname = txt_data + sdir # txt_data/first
        # print('하위 폴더(디렉토리) 확인:',dirname)

        file_list = os.listdir(dirname)
        # print(file_list)

        # 폴더에 있는 파일 목록
        for fname in file_list:
            # print(fname)
            file_path = dirname+"/"+fname

            if (os.path.isfile(file_path)):
                try:
                    file = open(file_path, mode='r', encoding='utf-8')
                    if  sdir == 'first':
                        first_txt.append(file.read())
                    else:
                        second_txt.append(file.read)
                except Exception as e:
                    print('error:', e)
                finally:
                    file.close()
            # end if
        # end for (inner for)
    # end for(outer for)

    return first_txt, second_txt
# end function
            
# 4. 함수 호출
first, second = textPro(sub_dir)
print('first_txt 길이=',len(first))
print('second_txt 길이=',len(second))