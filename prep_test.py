import pandas as pd
import numpy as np
import os
import json

def run():
    l_json = []
    for root, dirs, filenames in os.walk('test_json'):
        for filename in filenames:
            path = os.path.join(root, filename)
            with open(path, 'r') as f:
                json_data = json.load(f)
                l_json.append(json_data)

    j_data = pd.DataFrame(l_json)
    j_data.to_csv('csv/test.csv')

    data = pd.read_csv('csv/test.csv')
    data = data.drop(['Unnamed: 0'], axis=1)

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
    final_data.to_csv('csv/test_final.csv')