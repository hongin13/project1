import dlib
import cv2
import os
import math
import mtcnn

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

count = 0
l_count = [0] * 12

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
eb_list = [21, 22]
ns_list = [31, 35, 27, 33]
le_list = [37, 41, 36, 39]
re_list = [44, 46, 42, 45]



for i, l in meta:
    count += 1
    print(f"{i, l}, {count}")

    image = cv2.imread(i)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    rects = detector(image[..., ::-1], 1)

    dst = image.copy()
    for rect in rects:
        x1 = rect.left()
        x2 = rect.right()
        y1 = rect.top()
        y2 = rect.bottom()
        shape = predictor(image[..., ::-1], rect)
        for i in range(68):
            part = shape.part(i)
            p = (part.x, part.y)
            cv2.circle(dst, p, 3, (255, 0, 0), -1)
        
        eb = []
        for i in eb_list:
            part = shape.part(i)
            p = (part.x, part.y)
            cv2.circle(dst, p, 3, (0, 0, 255), -1)
            eb.append(p)
        
        # ns = []
        # for i in ns_list:
        #     part = shape.part(i)
        #     p = (part.x, part.y)
        #     cv2.circle(dst, p, 3, (0, 255, 0), -1)
        #     ns.append(p)

        eb_val = eyebrow(eb[0], eb[1], eb[2], eb[3])
        # ns_val = nose(ns[0], ns[1], ns[2], ns[3])
    #     print(x1, x2, y1, y2)
    # cv2.rectangle(dst, (x1, y1), (x2, y2), (0, 0, 255), 3)
    cv2.imshow('dst', dst)
    print(eb_val)
    # print(ns_val)
    cv2.waitKey(0)