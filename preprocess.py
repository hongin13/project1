import pandas as pd
import numpy as np
import os
import cv2

def run():
    data = pd.read_csv('csv/data.csv')
    data = data.drop(['Unnamed: 0'], axis=1)
    name = data['name']

    x = data.drop(['name'], axis=1)

    x_list = []
    y_list = []
    for i in range(478):
        x_list.append(x[f'x{i}'])
        y_list.append(x[f'y{i}'])

    x_list = np.array(x_list)
    y_list = np.array(y_list)
    x_data = pd.DataFrame(x_list)
    y_data = pd.DataFrame(y_list)
    x_data = x_data.transpose()
    y_data = y_data.transpose()

    x_max = x_data.max(axis = 1, numeric_only = True)
    x_min = x_data.min(axis = 1, numeric_only = True)
    y_max = y_data.max(axis = 1, numeric_only = True)
    y_min = y_data.min(axis = 1, numeric_only = True)
    x_max_data = pd.concat([x_max] * 478, axis=1)
    x_min_data = pd.concat([x_min] * 478, axis=1)
    y_max_data = pd.concat([y_max] * 478, axis=1)
    y_min_data = pd.concat([y_min] * 478, axis=1)

    pre_x_data = (x_data - x_min_data) / (x_max_data - x_min_data)
    pre_y_data = (y_data - y_min_data) / (y_max_data - y_min_data)
    pre_x_data.columns = [f'X{i}' for i in range(478)]
    pre_y_data.columns = [f'Y{i}' for i in range(478)]
    final_data = pd.concat([pre_x_data, pre_y_data], axis=1)

    from sklearn.cluster import KMeans
    # km_l = []
    # label = [i for i in range(12)]
    # for i in range(1, 13):
    #     km = KMeans(n_clusters=i, random_state=42)
    #     km.fit(final_data)
    #     km_l.append(km.inertia_)
    # plt.plot(label, km_l)

    km = KMeans(n_clusters=12, random_state=42)
    km.fit(final_data)
    label = pd.DataFrame(km.labels_, columns=['label'])

    name_data = pd.concat([label, name], axis=1)
    name_data.to_csv('csv/name.csv')

    final_x = final_data
    final_y = label
    final_x.to_csv('csv/final_x.csv')
    final_y.to_csv('csv/final_y.csv')

    # dic = {}
    # name = name_data['name']
    # label = name_data['label']
    # for i in range(len(name_data)):
    #     dic[name[i]] = label[i]

    # for root, dirs, filenames in os.walk('C:/Users/aischool/Desktop/All_Images'):
    #     for filename in filenames:
    #         first, last = os.path.splitext(filename)
    #         new_filename = first + '.jpg'
    #         path = os.path.join(root, new_filename)
    #         image = cv2.imread(path)
    #         if new_filename in dic.keys():
    #             cv2.imwrite(f'C:/Users/aischool/Desktop/labels/{dic[new_filename]}/{new_filename}', image)
