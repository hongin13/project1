import enum
import zipfile
import os
import cv2
import numpy as np

# -----------------------------------------------------------------------------
# 압축 풀기
# root = "C:\\Users\\aischool\\Desktop\\가족\\데이터"
# root1 = "C:\\Users\\aischool\\Desktop\\가족\\데이터\\Train\\원천데이터\\"
# root2 = "C:\\Users\\aischool\\Desktop\\가족\\데이터\\Valid\\image\\"

# for root, dirs, filenames in os.walk(root1):
#     for filename in filenames:
#         with zipfile.ZipFile(root1 + filename, 'r') as unzip:
#             unzip.extractall('C:/Users/aischool/Desktop/Unzip/Train')

# for root, dirs, filenames in os.walk(root2):
#     for filename in filenames:
#         with zipfile.ZipFile(root2 + filename, 'r') as unzip:
#             unzip.extractall('C:/Users/aischool/Desktop/Unzip/Valid')
# ----------------------------------------------------------------------------
# 사진 저장
for root, dirs, filenames in os.walk('C:\\Users\\aischool\\Desktop\\Unzip'):
    for filename in filenames:
        path = os.path.join(root, filename)
        
        # # cv2.imwrite(path, image)
        first, last = os.path.splitext(filename)
        if "IND" in first:
            first = first
            if first.split("_")[-2] == '0':
                final = first + '.jpg'
                path = os.path.join(root, final)
                image = cv2.imread(path)

                if image is None:
                    print("Error : ", path)
                    continue
                
                dst = image.copy()
                cv2.imwrite('IND/' + final, image)

