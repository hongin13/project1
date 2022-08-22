import dlib
import cv2
import os
import math
import numpy as np
import json

meta = []

for root, dirs, filenames in os.walk('C:\\Users\\aischool\\Desktop\\image'):
    for filename in filenames:
        path = os.path.join(root, filename)
        # print(path)
        image = cv2.imread(path)
        if image is None:
            print("Error : ", path)
            continue
        cv2.imwrite(path, image)
        first, last = os.path.splitext(filename)
        path = os.path.join(root, first + '.jpg')
        meta.append((path))

features = ['face', 'eyebrow', 'eyebtween', 'low', 'philtrum', 'uplib', 'downlib', 'nosewidth', 'noseheight', 'eyesize', 'mouth']

def distance(x1, y1, x2, y2):
    result = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    return result

def area(p1, p2, p3, p4):
    d1 = distance(p1[0], p1[1], p2[0], p2[1])
    d2 = distance(p3[0], p3[1], p4[0], p4[1])
    return d1 / d2

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

for i in meta:
    # print(i)
    result = []

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    image = cv2.imread(i)

    rects = detector(image[..., ::-1], 1)
    dst = image.copy()

    for rect in rects:
        shape = predictor(image[..., ::-1], rect)

    for k, v in dic_f.items():
        eyebrow = []
        for val in v:
            part = shape.part(val)
            p = (part.x, part.y)
            eyebrow.append(p)
        print(eyebrow)
    #     if len(eyebrow) == 5:
    #         a = eyebrow[2]
    #         b = eyebrow[3]
    #         c = eyebrow.pop()
    #         eyebrow[2] = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    #         eyebrow[3] = c
    #     # print(eyebrow)
    #     val = area(eyebrow[0], eyebrow[1], eyebrow[2], eyebrow[3])
    #     result.append(val)
    # # print(result)
    # le = result[9]
    # # print(le)
    # re = result[10]
    # m = result.pop()
    # result[9] = (le[0] + re[0]) / 2
    # result[10] = m
    # # print(result[:10])
    # for i in range(len(result)):
    #     dic[features[i]] = result[i]

    
    # print(dic)
