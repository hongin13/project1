import cv2
import os
import numpy as np

DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480
for root, dirs, filenames in os.walk('Images'):
    for filename in filenames:
        first, last = os.path.splitext(filename)
        path = os.path.join(root, first + '.jpg')
        # print(path)
        image = cv2.imread(path)
        dst = image.copy()
        dst = cv2.resize(dst, (480, 480))
        # print(dst.shape)
        cv2.imwrite(f"resize/{first}.jpg", dst)
