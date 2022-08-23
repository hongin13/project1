#%%
import os
import numpy as np
import pandas as pd
import json
import tensorflow as tf
from tensorflow import keras

labels = ['Rat', 'Cow', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
 'Horse', 'Sheep', 'Monkey', 'Chicken', 'Dog', 'Pig']

l_json = []
for root, dirs, filenames in os.walk('json2'):
    for filename in filenames:
        path = os.path.join(root, filename)
        with open(path, 'r') as f:
            json_data = json.load(f)
            l_json.append(json_data)
        # print(json.dumps(json_data))

#%%
data = pd.DataFrame(l_json)
print(data)
print(data.shape)
# print(data.isnull().sum() / len(data))

#%%
X = data.drop(['label'], axis=1)
y = data['label']
print(X.shape, y.shape)

from sklearn.model_selection import train_test_split
x_data, tt_x, y_data, tt_y = train_test_split(X, y, random_state=42, test_size=0.1)
print(x_data.shape, tt_x.shape, y_data.shape, tt_y.shape)

#%%
from sklearn.tree import DecisionTreeClassifier
dt1 = DecisionTreeClassifier()
dt1.fit(x_data, y_data)
print(dt1.score(x_data, y_data), dt1.score(tt_x, tt_y))
print(dt1.predict(tt_x[:5]))
print(list(tt_y[:5]))

# %%
