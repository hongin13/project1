import dlib
import cv2
import os
import math

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
result = []
d = []

def distance(x1, y1, x2, y2):
    result = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    return result

def eyebrow(p1, p2, p3, p4):
    d1 = distance(p1[0], p1[1], p2[0], p2[1])
    d2 = distance(p3[0], p3[1], p4[0], p4[1])
    return d1 / d2

def nose(p1, p2, p3, p4):
    d1 = distance(p1[0], p1[1], p2[0], p2[1])
    d2 = distance(p3[0], p3[1], p4[0], p4[1])
    return d1 / d2

# eb_list = [21, 22, 17, 26]
face = [0, 16, 19, 8]
eyebrow_list = [21, 22, 0, 16]
eyeb_list = [39, 42, 0, 16]
low_list = [57, 8, (19, 24), 8]
philtrum_list = [33, 51, (19,24), 8]
uplib_list = [51, 62, (19,24), 8]
downlib_list = [66, 57, (19,24), 8]
nosew_list = [31, 35, 0, 16]
noseh_list = [27, 33, (19,24), 8]
lefteye_list =[36, 39, 0, 16]
righteye_list = [42, 45, 0, 16]
mouth_list = [48, 54, 0, 16]


for i, l in meta:
    # print(i, l)
    # print(items[0], items[1])
    count += 1
    # print(f"{i, l}, {count}")

    image = cv2.imread(i)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    rects = detector(image[..., ::-1], 1)

    dst = image.copy()

    for rect in rects:
        # x1 = rect.left()
        # x2 = rect.right()
        # y1 = rect.top()
        # y2 = rect.bottom()
        shape = predictor(image[..., ::-1], rect)
        
        
        
        # for i in range(68):         # .dat 파일이 68개의 점을 가지고 있음
        #     part = shape.part(i)
        #     p = (part.x, part.y)
        #     cv2.circle(dst, p, 3, (255, 0, 0), -1)
        
        # b = []
        # for i in face:
        #     part = shape.part(i)
        #     p = (part.x, part.y)
        #     b.append(p)
        # cv2.rectangle(dst, (b[0][0], b[2][1]), (b[1][0], b[3][1]), (255, 0, 0), 3)

        res = []
        for i in eyebrow_list:
            part = shape.part(i)
            p = (part.x, part.y)
            cv2.circle(dst, p, 3, (0, 0, 255), -1)
            res.append(p)
            # print(p)
        
        # ns = []
        # for i in ns_list:
        #     part = shape.part(i)
        #     p = (part.x, part.y)
        #     cv2.circle(dst, p, 3, (0, 255, 0), -1)
        #     ns.append(p)

        eyebrow_val = eyebrow(res[0], res[1], res[2], res[3])
        # ns_val = nose(ns[0], ns[1], ns[2], ns[3])
        result.append((eyebrow_val, l, count))
    #     print(x1, x2, y1, y2)
    # cv2.rectangle(dst, (x1, y1), (x2, y2), (0, 0, 255), 3)
    # cv2.imshow('dst', dst)
    print(result)
    # print(eb_val)
    # print(ns_val)
    # print(eb)
    # cv2.waitKey(0)

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

        # print(p, l)
        # print(items[0], items[1])

# image = cv2.imread('down/Chicken_1.jpg')
# # label = l
# # print(label)
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# rects = detector(image[..., ::-1], 1)
# rects

# dst = image.copy()
# for rect in rects:
#     x1 = rect.left()
#     x2 = rect.right()
#     y1 = rect.top()
#     y2 = rect.bottom()
#     shape = predictor(image[..., ::-1], rect)
#     for i in range(68):         # .dat 파일이 68개의 점을 가지고 있음
#         part = shape.part(i)
#         p = (part.x, part.y)
#         cv2.circle(dst, p, 3, (255, 0, 0), -1)
    

#     part = shape.part(21)
#     p1 = (part.x, part.y)
#     cv2.circle(dst, p1, 3, (0, 0, 255), -1)
    
#     part = shape.part(22)
#     p2 = (part.x, part.y)
#     cv2.circle(dst, p2, 3, (0, 0, 255), -1)
    
#     part = shape.part(17)
#     p3 = (part.x, part.y)
#     cv2.circle(dst, p3, 3, (0, 0, 255), -1)

#     part = shape.part(26)
#     p4 = (part.x, part.y)
#     cv2.circle(dst, p4, 3, (0, 0, 255), -1)

#     d1 = distance(p1[0], p1[1], p2[0], p2[1])
#     d2 = distance(p3[0], p3[1], p4[0], p4[1])
#     print(d1 / d2)
#     cv2.rectangle(dst, (x1, y1), (x2, y2), (255, 0, 0), 3)

# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# # cv2.imshow('img', rect)

#  이미지별로 약 5개 이상의 수치들을 뽑아냄
#  