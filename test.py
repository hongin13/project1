import pandas as pd
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import BatchNormalization, Dropout
from sklearn.model_selection import train_test_split

import facemesh_test
import prep_test

facemesh_test.run()
prep_test.run()

final_data = pd.read_csv('csv/test_final.csv')
new_final_data = final_data.transpose()
new_final_data = new_final_data[1:]
final_data = new_final_data.transpose()
final_y = pd.read_csv('csv/final_y.csv')
new_final_y = final_y.transpose()
new_final_y = new_final_y[1:]
final_y = new_final_y.transpose()
final_to_y = to_categorical(final_y)

from keras.models import load_model
l_m = load_model('best_model.h')

y_pred = l_m.predict(final_data)
# l_m.evaluate(final_data, final_y)