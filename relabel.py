import pandas as pd
import cv2
import os

data = pd.read_csv('csv/name.csv')
# print(data)

dic = {}
name = data['name']
label = data['label']
for i in range(len(data)):
    dic[name[i]] = label[i]

for root, dirs, filenames in os.walk('C:/Users/aischool/Desktop/All_Images'):
    for filename in filenames:
        first, last = os.path.splitext(filename)
        new_filename = first + '.jpg'
        path = os.path.join(root, new_filename)
        image = cv2.imread(path)
        if new_filename in dic.keys():
            cv2.imwrite(f'C:/Users/aischool/Desktop/labels/{dic[new_filename]}/{new_filename}', image)
