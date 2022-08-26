import mediapipe as mp
import cv2
import os
import math
import pandas as pd
import json

def run():
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

    def resize_and_show(image):
        h, w = image.shape[:2]
        if h < w:
            img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
        else:
            img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
        cv2.imshow('img', img)
        cv2.waitKey(0)

    def load_json(x):
        with open(f'json_all/features_{count}.json', 'w') as f:
            json.dump(x, f)

    # for root, dirs, filenames in os.walk('C:/Users/aischool/Desktop/High'):
    for root, dirs, filenames in os.walk('C:/Users/aischool/Desktop/All_Images'):
        for filename in filenames:
            path = os.path.join(root, filename)
            image = cv2.imread(path)
            if image is None:
                print("Error : ", path)
                continue
            resize(image)
            first, last = os.path.splitext(filename)
            path = os.path.join(root, first + '.jpg')
            meta.append((path))

    images = {}
    for i in range(len(meta)):
        images[i] = cv2.imread(meta[i]), meta[i]

    mp_face_mesh = mp.solutions.face_mesh
    # help(mp_face_mesh.FaceMesh)

    mp_drawing = mp.solutions.drawing_utils 
    mp_drawing_styles = mp.solutions.drawing_styles

    with mp_face_mesh.FaceMesh(static_image_mode=True, refine_landmarks=True, max_num_faces=2, min_detection_confidence=0.5) as face_mesh:
        for count, data in images.items():
            points = {}
            image = data[0]
            filename = data[1].split('\\')[-1]

            # Convert the BGR image to RGB and process it with MediaPipe Face Mesh.
            results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Draw face landmarks of each face.
            print(f'Face landmarks of {count}:')
            
            # face_mesh
            if not results.multi_face_landmarks:
                continue
            annotated_image = image.copy()  

            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(image=annotated_image, landmark_list=face_landmarks)
                # mp_drawing.draw_landmarks(image=annotated_image, landmark_list=face_landmarks, connections=mp_face_mesh.FACEMESH_TESSELATION,
                #  landmark_drawing_spec=None, connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
                # mp_drawing.draw_landmarks(image=annotated_image, landmark_list=face_landmarks, connections=mp_face_mesh.FACEMESH_CONTOURS,
                #  landmark_drawing_spec=None, connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
                # mp_drawing.draw_landmarks(image=annotated_image, landmark_list=face_landmarks, connections=mp_face_mesh.FACEMESH_IRISES,
                #  landmark_drawing_spec=None, connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())

                for id, lm in enumerate(face_landmarks.landmark):
                    h, w, c = annotated_image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    points['name'] = filename
                    points[f'x{id}'] = cx
                    points[f'y{id}'] = cy

            load_json(points)

    l_json = []
    for root, dirs, filenames in os.walk('json_all'):
        for filename in filenames:
            path = os.path.join(root, filename)
            with open(path, 'r') as f:
                json_data = json.load(f)
                l_json.append(json_data)

    data = pd.DataFrame(l_json)
    data.to_csv('csv/data.csv')


