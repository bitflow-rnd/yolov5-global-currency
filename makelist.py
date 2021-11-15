# -*- coding: utf-8 -*-
import glob

# 리스트를 txt파일로 생성
f1 = open('./datasets/global-currency/train.txt', 'w')
f2 = open('./datasets/global-currency/val.txt', 'w')
f3 = open('./datasets/global-currency/test.txt', 'w')

f1.truncate(0)
f2.truncate(0)
f3.truncate(0)

i = 1

# 이미지들의 주소 리스트로 만들어줌
for jpg_path in sorted(glob.glob('./datasets/global-currency/**/*.jpg')):
    jpg_path = jpg_path.split('\\', 1)[1].replace('\\', '/')
    if i < 9:
        f1.write(jpg_path + '\n')
    elif i < 10:
        f2.write(jpg_path + '\n')
    else:
        f3.write(jpg_path + '\n')
        i = 0
    i = i + 1

f1.close()
f2.close()
f3.close()
