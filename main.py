# import cv2
# import os
# import numpy as np
# import pandas as pd
# import json
# import tensorflow as tf
# from tensorflow import keras

# # labels = ['Rat', 'Cow', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
# #  'Horse', 'Sheep', 'Monkey', 'Chicken', 'Dog', 'Pig']

# l_json = []
# for root, dirs, filenames in os.walk('json'):
#     for filename in filenames:
#         path = os.path.join(root, filename)
#         with open(path, 'r') as f:
#             json_data = json.load(f)
#             l_json.append(json_data)
#         # print(json.dumps(json_data))

# data = pd.DataFrame(l_json)
# # print(df)

# print(data.isnull().sum() / len(data))

# X = data.drop(['label'], axis=1)
# y = data['label']

# from sklearn.model_selection import train_test_split
# x_data, tt_x, y_data, tt_y = train_test_split(X, y, random_state=42, test_size=0.1)

# from sklearn.tree import DecisionTreeClassifier
# dt1 = DecisionTreeClassifier()
# dt1.fit(x_data, y_data)
# print(dt1.score(x_data, y_data), dt1.score(tt_x, tt_y))
# print(dt1.predict(tt_x[:5]))
# print(list(tt_y[:5]))

# model = keras.layers.Sequential([
#     keras.layers.Dense()
# ])

# ll_json = []
# for root, dirs, filenames in os.walk('test_json'):
#     for filename in filenames:
#         path = os.path.join(root, filename)
#         with open(path, 'r') as f:
#             json_test_data = json.load(f)
#             ll_json.append(json_test_data)

# val_data = pd.DataFrame(ll_json)
# print(dt1.predict(val_data))

# # import matplotlib.pyplot as plt
# # from sklearn.tree import plot_tree
# # plot_tree(dt1)
# # plt.show()