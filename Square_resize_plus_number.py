import numpy as np
import matplotlib.pyplot as plt
import time
import os
import copy
import pandas as pd
import csv
from random import randint
from time import sleep
import math

import glob
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import cv2


#元画像フォルダ
in_path = 'C:\\Users\\ykita\\OneDrive\\デスクトップ\\Gravcont'

#保存先フォルダ
out_path = 'C:\\Users\\ykita\\OneDrive\\デスクトップ\\Gravcont_2'
if not os.path.exists(out_path):
    os.mkdir(out_path)


#処理するDirectoryの設定
file = os.listdir(in_path)
print(len(file))

#ここにフォルダ番号を記載する (ex. [0:999])
processing_file = file[0:5]
print(processing_file)
len(processing_file)



def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width-height)//2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, (0, (height - width) // 2))
        return result

    # 処理時間の計測
    start = time.time()

    l = 0
    for i in processing_file:
        img = Image.open(in_path + '/' + i)
        img_new = expand2square(img, (0, 0, 0)).resize((1000, 1000))
        #img_new.save(out_path +'/'+ str(i))
        print(out_path + '/' + str(i))

        # 切り取った画像を表示
        plt.imshow(np.asarray(img_new))
        plt.show()

    print('Process done!!')
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")


# 処理時間の計測
start = time.time()

l = 0
for i in processing_file:
    img = Image.open(in_path + '/' + i)
    img_new = expand2square(img, (0, 0, 0)).resize((1000, 1000))

    # 切り取った画像を表示
    # plt.imshow(np.asarray(img_new))
    # plt.show()

    #Patient idを図に記入する
    draw = ImageDraw.Draw(img_new)  # im上のImageDrawインスタンスを作る
    font_path = 'C:\Windows\Fonts\meiryo.ttc'  # Windowsのフォントファイルへのパス
    font_size = 100 # フォントサイズ
    font = ImageFont.truetype(font_path, font_size)  # PILでフォントを定義
    draw.text((10, 10), str(i), font=font)

    img_new.save(out_path + '/' + i)
    print(out_path + '/' + i)

print('Process done!!')
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")