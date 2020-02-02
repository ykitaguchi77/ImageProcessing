import glob
import shutil
import os
import csv

'''
フォルダ分けされている全てのファイルを、別の1つのフォルダ内にまとめるスクリプト
「元画像フォルダ名-ファイル番号」という名前になる

変換前
-----1-----abc.jpg
   |    |--def.jpg
   |
   |-2-----ghi.jpg     
        |--jkl.jpg

変換後
---------1.jpg
   |  |--2,jpg        
   |  |--3.jpg
   |  |--4.jpg
   |-----image_list.csv(対応表）    
       
'''
#元画像フォルダ
#in_path = 'C://Users//Yoshi//仕事用Drive//進行中//データ取り中//AI眼位写真//眼位写真'
in_path = 'C://Users//Yoshi//Desktop//ii//ii1'
#保存先フォルダ
#out_path = 'C://Users//Yoshi//仕事用Drive//進行中//データ取り中//AI眼位写真//眼位写真2'
out_path = 'C://Users//Yoshi//Desktop//ii//ii2'

#CSVファイルのフォルダ
#csv_path = 'C://Users//Yoshi//仕事用Drive//進行中//データ取り中//AI眼位写真//眼位写真2//image_list.csv'
csv_path = 'C://Users//Yoshi//Desktop//ii//ii2//image_list.csv'


def main():

    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)

        m=1
        directory = os.listdir(in_path)
        for i in directory:  #フォルダ数の分だけ
            file = os.listdir(in_path + '//' + i)
            l=0
            for j in file:
                print(in_path + '//' + i + '//' + j)
                shutil.copy(in_path + '//' + i + '//' + j, out_path + '//'+ str(m+1) + '.jpg')
                l+=1

                #対応表の作成
                writer.writerow([str(m), i, j,])
                m+=1




if __name__ == '__main__':
        main()
