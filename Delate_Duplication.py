import csv
import numpy as np

'''重複したIDを削除するスクリプト'''

data = np.loadtxt("DiseaseInfo.csv",       # 読み込みたいファイルのパス
                  delimiter=",", dtype="unicode")  # ファイルの区切り文字

#print(data)

for i in range(1, data.shape[0]):
    temp = data[i, 2]  # 病名番号(1~)を参照

    for j in range(2, 64):
        if temp == str(j):
            data[i-j+1, j+2] = data[i, 3]


#print(data)
data = np.delete(data, np.where(data[:, 2] != '1')[0], axis=0)

np.savetxt('DiseaseInfo_modified.csv', data, delimiter=',', fmt='%s')

