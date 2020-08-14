import random
import glob
import os
import shutil

"""
フォルダ内のファイルから規定数を無作為に抽出し、別フォルダにコピーするスクリプト

実行前
----orig_path------1.jpg
               |---2.jpg
               |---3.jpg
               |---
               |---100.jpg

実行後
----orig_path------1.jpg
  |            |---2.jpg
  |            |---3.jpg
  |            |---...
  |            |---100.jpg
  |
  |--dest_path-----2.jpg
               |---5.jpg
               |---13.jpg
               |---...
               |---89.jpg
               
"""

orig_path = "C:\\Users\\ykita\\OneDrive\\デスクトップ\\Control_photo"
dst_path = "C:\\Users\\ykita\\OneDrive\\デスクトップ\\Control_photo_random"#フォルダ名
if not os.path.exists(dst_path):#ディレクトリがなかったら
    os.mkdir(dst_path)#作成したいフォルダ名を作成
copy_num = 333 #移動したいファイルの数

files = glob.glob(orig_path + "\\*")
print(files)
sample_files = random.sample(files, copy_num) #規定数のファイルを無作為に選択

for p in sample_files: #選択したファイルを目的フォルダにコピー
    shutil.copy(p, dst_path)





