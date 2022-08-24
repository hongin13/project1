import mediapipe as mp
import cv2
import os
import math
import numpy as np
import json

meta = []
labels = ['Rat', 'Cow', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
          'Horse', 'Sheep', 'Monkey', 'Chicken', 'Dog', 'Pig']

DESIRED_HEIGHT = 1280
DESIRED_WIDTH = 1280
def resize(image):
    h, w = image.shape[:2]
    if h < w:
        img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
    else:
        img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
    return img
    # cv2.imshow('img', img)
    # cv2.waitKey(0)

def resize_and_show(image):
    h, w = image.shape[:2]
    if h < w:
        img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
    else:
        img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
    cv2.imshow('img', img)
    cv2.waitKey(0)

def load_json(x):
    with open(f'json7/features_{count}.json', 'w') as f:
        json.dump(x, f)

for root, dirs, filenames in os.walk('Images'):
# for root, dirs, filenames in os.walk('C:/Users/aischool/Desktop/1'):
# for root, dirs, filenames in os.walk('C:/Users/aischool/Desktop/image'):
    for filename in filenames:
        path = os.path.join(root, filename)
        image = cv2.imread(path)
        if image is None:
            print("Error : ", path)
            continue
        resize(image)
        # label = -1
        # for index, name in enumerate(labels):
        #     if name in root:
        #         label = index
        #         break
        # if label == -1:
        #     continue
        first, last = os.path.splitext(filename)
        path = os.path.join(root, first + '.jpg')
        meta.append((path))

print(len(meta))
images = {}
for i in range(len(meta)):
    # print(meta[i][0])
    images[i] = cv2.imread(meta[i]), meta[i]
    # images[i] = cv2.imread(meta[i][0]), meta[i][1], meta[i][0]
# print(images[814])

# images = {label : cv2.imread(path) for path, label in meta}
# for label, image in images.items():

# for count, data in images.items():
#     image = data[0]
#     label = data[1]
#     print(label, image)

mp_face_mesh = mp.solutions.face_mesh
# mp_face_detection = mp.solutions.face_detection
# help(mp_face_mesh.FaceMesh)

mp_drawing = mp.solutions.drawing_utils 
mp_drawing_styles = mp.solutions.drawing_styles

# face detection
# with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
#     for count, data in images.items():
#         # points = {}
#         image = data[0]
#         label = data[1]
#     # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
#         result = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

with mp_face_mesh.FaceMesh(static_image_mode=True, refine_landmarks=True, max_num_faces=2, min_detection_confidence=0.5) as face_mesh:
    for count, data in images.items():
        image = data[0]
        # label = data[1]
        # filename = data[2].split('\\')[-1]
        # print(image, label, filename)
        points = {}
        # Convert the BGR image to RGB and process it with MediaPipe Face Mesh.
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Draw face landmarks of each face.
        print(f'Face landmarks of {count}:')
        # face_detection
        # if not result.detections:
        #     continue
        # annotated_image = image.copy()
        # for detection in result.detections:
        #     print('Nose tip:')
        #     print(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
        #     mp_drawing.draw_detection(annotated_image, detection)
        
        # face_mesh
        if not results.multi_face_landmarks:
            continue
        annotated_image = image.copy()  
        # cv2.imshow('img', annotated_image)
        # cv2.waitKey(0)
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(image=annotated_image, landmark_list=face_landmarks)
            # mp_drawing.draw_landmarks(image=annotated_image, landmark_list=face_landmarks, connections=mp_face_mesh.FACEMESH_TESSELATION,
            #  landmark_drawing_spec=None, connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
            # mp_drawing.draw_landmarks(image=annotated_image, landmark_list=face_landmarks, connections=mp_face_mesh.FACEMESH_CONTOURS,
            #  landmark_drawing_spec=None, connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
            # mp_drawing.draw_landmarks(image=annotated_image, landmark_list=face_landmarks, connections=mp_face_mesh.FACEMESH_IRISES,
            #  landmark_drawing_spec=None, connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())
            x_list = []
            y_list = []
            for id, lm in enumerate(face_landmarks.landmark):
                # print(lm)
                h, w, c = annotated_image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # if id == 10:
                #     cv2.circle(annotated_image, (cx, cy), 3, (255, 0, 0), -1)
                #     print(w, h, cx, cy)
                #     continue
                # if id == 447:
                #     print(cx, cy)
                #     continue
                
                x_list.append(cx)
                y_list.append(cy)
                max_cx = max(x_list)
                max_cy = max(y_list)
                min_cx = min(x_list)
                min_cy = min(y_list)
            
            # print(max_cx, max_cy, min_cx, min_cy)
                wx = max_cx - min_cx
                hy = max_cy - min_cy
                if wx == 0 or hy == 0:
                    points[id] = 0
                    points[id + 478] = 0
                # print([i for i in range(478) if wx == 0])
                # print([i for i in range(478) if hy == 0])
                # if wx == 0:
                #     print(id)
                #     break
                else:
                    points[id] = (cx - min_cx) / wx
                    points[id + 478] = (cy - min_cy) / hy

                # points['label'] = label
                # points[id] = ((cx / w) + (cy / h)) / 2
                # points['filename'] = filename
        #         print(f"{id} : {cx, cy}")
        #         points[id] = cx
        #         points[id + 478] = cy
        #         # for i in range(id):
        #         #     cv2.circle(annotated_image, (cx, cy), 3, (255, 0, 0), -1)

        load_json(points)
        # resize_and_show(annotated_image)


