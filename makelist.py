# -*- coding: utf-8 -*-
from glob import glob

# 이미지들의 주소 리스트로 만들어줌
train_img_list = glob('./datasets/global-currency/img/**/*.jpg')

# 리스트를 txt파일로 생성
with open('./datasets/global-currency/train.txt', 'w') as f1:
with open('./datasets/global-currency/val.txt', 'w') as f2:
with open('./datasets/global-currency/test.txt', 'w') as f3:

for img_url in train_img_list
    f1.write('\n'.join(train_img_list) + '\n')
    f2.write('\n'.join(train_img_list) + '\n')
    f3.write('\n'.join(train_img_list) + '\n')
