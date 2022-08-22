import dlib
import cv2
import os
import math
import numpy as np
import json

meta = []
labels = ['Rat', 'Cow', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
          'Horse', 'Sheep', 'Monkey', 'Chicken' ,'Dog', 'Pig']

for root, dirs, filenames in os.walk('Images'):
    for filename in filenames:
        path = os.path.join(root, filename)
        image = cv2.imread(path)
        if image is None:
            print("Error : ", path)
            continue
        cv2.imwrite(path, image)
        label = -1
        for index, name in enumerate(labels):
            if name in root:
                label = index
                break
        if label == -1:
            continue
        path = os.path.join(root, filename)
        meta.append((path, label))

# # print(len(meta))

count = 0
l_count = [0] * 12
features = ['face', 'eyebrow', 'eyebtween', 'low', 'philtrum', 'uplib', 'downlib', 'nosewidth', 'noseheight', 'eyesize', 'mouth']

def Median(p1, p2):
    result = p1 + p2 / 2
    return result[0], result[1]

def distance(x1, y1, x2, y2):
    result = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    return result

def area(p1, p2, p3, p4):
    d1 = distance(p1[0], p1[1], p2[0], p2[1])
    d2 = distance(p3[0], p3[1], p4[0], p4[1])
    return d1 / d2

# eb_list = [21, 22, 17, 26]
dic_f = {
    'l_face' : [0, 16, 19, 24, 8],
    'l_eyebrow' : [21, 22, 0, 16],
    'l_eyeb' : [39, 42, 0, 16],
    'l_low' : [57, 8, 19, 24, 8],
    'l_philtrum' : [33, 51, 19, 24, 8],
    'l_uplib' : [51, 62, 19, 24, 8],
    'l_downlib' : [66, 57, 19, 24, 8],
    'l_nosew' : [31, 35, 0, 16],
    'l_noseh' : [27, 33, 19, 24, 8],
    'l_lefteye' : [36, 39, 0, 16],
    'l_righteye' : [42, 45, 0, 16],
    'l_mouth' : [48, 54, 0, 16]
}

dic = {}

for i, l in meta:
    result = []
    count += 1

    image = cv2.imread(i)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    rects = detector(image[..., ::-1], 1)
    dst = image.copy()

    for rect in rects:
        shape = predictor(image[..., ::-1], rect)

    for k, v in dic_f.items():
        eyebrow = []
        for i in v:
            part = shape.part(i)
            p = (part.x, part.y)
            eyebrow.append(p)
        # print(eyebrow)
        if len(eyebrow) == 5:
            a = eyebrow[2]
            b = eyebrow[3]
            c = eyebrow.pop()
            eyebrow[2] = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
            eyebrow[3] = c
        # print(eyebrow)
        val = area(eyebrow[0], eyebrow[1], eyebrow[2], eyebrow[3])
        result.append((val, l))
    le = result[9]
    re = result[10]
    m = result.pop()
    result[9] = ((le[0] + re[0]) / 2, (le[1] + re[1]) / 2)
    result[10] = m
    for i in range(len(result)):
        dic['label'] = labels[int(result[i][1])]
        dic[features[i]] = result[i][0]
    
    # print(dic)
    for items in dic:
        with open(f'json/features_{count}.json', 'w') as f:
            json.dump(dic, f)

        # part = shape.part(21)
        # p1 = (part.x, part.y)
        # cv2.circle(dst, p1, 3, (0, 0, 255), -1)

        # part = shape.part(22)
        # p2 = (part.x, part.y)
        # cv2.circle(dst, p2, 3, (0, 0, 255), -1)
        
        # part = shape.part(17)
        # p3 = (part.x, part.y)
        # cv2.circle(dst, p3, 3, (0, 0, 255), -1)

        # part = shape.part(26)
        # p4 = (part.x, part.y)
        # cv2.circle(dst, p4, 3, (0, 0, 255), -1)

        # d1 = distance(p1[0], p1[1], p2[0], p2[1])
        # d2 = distance(p3[0], p3[1], p4[0], p4[1])
        # d.append(d1 / d2)

        
    # l_count[l] += 1
#     print("실행")
    # cv2.rectangle(dst, (x1, y1), (x2, y2), (255, 0, 0), 3)
#     cv2.imwrite(f'down/{labels[l]}_{l_count[l]}.jpg', dst)
# print(d)

    # count += 1
    # cv2.imwrite(f'down/{count}.jpg', dst)

        # part = shape.part(0)
        # p1 = (part.x, part.y)
        # cv2.circle(dst, p1, 3, (0, 255, 0), -1)

        # part = shape.part(8)
        # p2 = (part.x, part.y)
        # cv2.circle(dst, p2, 3, (0, 0, 255), -1)

        # part = shape.part(16)
        # p3 = (part.x, part.y)
        # cv2.circle(dst, p3, 3, (100, 100, 100), -1)
       
    # cv2.imshow('img', dst)
    # cv2.waitKey(1)
