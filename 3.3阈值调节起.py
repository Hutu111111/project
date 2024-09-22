# -*- coding: utf-8 -*-
'''
@author: zhanmging
@software: 
@file: 3.3阈值调节起.py
@time: 2021/9/16 7:14
'''
import cv2
import numpy as np

# 添加新窗口
cv2.namedWindow('image')

#filename = './image/coin.png'
# filename = './image/xingtai/card9.png'
# filename ="./image/huofu.png"
# filename="./image/credit_card_04.png"
filename="./image/hand/five.jpg"
#filename="./image/PCB.jpg"
img= cv2.imread(filename, 0)
img=cv2.resize(img,(600,600))

# 创建滑块,注册回调函数 lambda x: None没有滑动时
cv2.createTrackbar('num', 'image', 0, 255, lambda x: None)

while (1):
    num = cv2.getTrackbarPos("num", "image")
    ret, thresh1 = cv2.threshold(img, num, 255, cv2.THRESH_BINARY)
    cv2.imshow('image', thresh1)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
