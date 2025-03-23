# 이진 파일 (이미지, 동영상, 음원, ....)

import os
from glob import glob

print("현재 경로:", os.getcwd())

# 1. image 파일 경로

img_path = 'img\\' # img 라는 폴더를 가리킴
# 단순 경로 설정, 디렉터리 실제 존재 확인 x
img_path_copy = os.getcwd() + '/ex06/imgcopy/' # 이게 타겟이라고 먼저 생성

if os.path.exists(img_path):
    print('원본 이미지 폴더가 존재합니다.')

    # image 파일 저장, 이동
    images = []
    # print(img_path_copy)
    # print(os.path.exists(img_path_copy), not(os.path.exists(img_path_copy)) )

    # 이동할 이미지 폴더가 없으면
    if not (os.path.exists(img_path_copy)):
        os.mkdir(img_path_copy)
    else: # 이동할 이미지 폴더가 있으면
        # image 검색
        for pic_path in glob(img_path + '*.gif'):
            print('원본 이미지 경로:', pic_path)
    # for pic_path in glob(img_path + 'apple0[3-4].gif')           

    print(pic_path)