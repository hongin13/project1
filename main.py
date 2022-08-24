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
for root, dirs, filenames in os.walk('json5'):
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
m1 = DecisionTreeClassifier(random_state=42)
m1.fit(x_data, y_data)
print(m1.score(x_data, y_data), m1.score(tt_x, tt_y))
print(m1.predict(tt_x[:5]))
print(list(tt_y[:5]))

# %%
from sklearn.linear_model import LogisticRegression
m2 = LogisticRegression()
m2.fit(x_data, y_data)
print(m2.score(x_data, y_data), m2.score(tt_x, tt_y))
print(m2.predict(tt_x[:5]))
print(list(tt_y[:5]))

# %%
from sklearn.ensemble import RandomForestClassifier
m3 = RandomForestClassifier()
m3.fit(x_data, y_data)
print(m3.score(x_data, y_data), m3.score(tt_x, tt_y))
print(m3.predict(tt_x[:5]))
print(list(tt_y[:5]))

#%%
from sklearn.ensemble import VotingClassifier
ec = VotingClassifier([('m1', m1), ('m2', m2), ('m3', m3)], voting='hard')

# %%
from sklearn.model_selection import cross_val_score
print(cross_val_score(m1, X, y, cv=5).mean())
print(cross_val_score(m2, X, y, cv=5).mean())
print(cross_val_score(m3, X, y, cv=5).mean())
print(cross_val_score(ec, X, y, cv=5).mean())

# %%
data.to_csv('data7.csv')
# %%
print(x_data.iloc[0])
# %%
