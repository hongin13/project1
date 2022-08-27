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
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras import optimizers
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import BatchNormalization, Dropout
from sklearn.model_selection import train_test_split

tf.random.set_seed(42)
np.random.seed(42)
# def run():
final_x = pd.read_csv('csv/final_x.csv')
new_final_x = final_x.transpose()
new_final_x = new_final_x[1:]
final_x = new_final_x.transpose()
final_y = pd.read_csv('csv/final_y.csv')
new_final_y = final_y.transpose()
new_final_y = new_final_y[1:]
final_y = new_final_y.transpose()
final_to_y = to_categorical(final_y)
print(len(final_x))

tr_x, tt_x, tr_y, tt_y = train_test_split(final_x, final_to_y, random_state=42, test_size=0.2)
t_x, v_x, t_y, v_y = train_test_split(tr_x, tr_y, random_state=42, test_size=0.3)

# tr_x2, tt_x2, tr_y2, tt_y2 = train_test_split(final_x, final_y, random_state=42, test_size=0.2)
# t_x2, v_x2, t_y2, v_y2 = train_test_split(tr_x2, tr_y2, random_state=42, test_size=0.3)

es = EarlyStopping(patience=50, restore_best_weights=True)
mc = ModelCheckpoint('best_model5.h', save_best_only=True)

# m1 = Sequential()
# m1.add(BatchNormalization())
# m1.add(Dense(512, input_shape=(956,)))
# m1.add(BatchNormalization())
# m1.add(Activation('ELU'))
# m1.add(Dense(256))
# m1.add(BatchNormalization())
# m1.add(Activation('ELU'))
# m1.add(Dense(128))
# m1.add(BatchNormalization())
# m1.add(Activation('ELU'))
# m1.add(Dense(64))
# m1.add(BatchNormalization())
# m1.add(Activation('ELU'))
# m1.add(Dense(32))
# m1.add(BatchNormalization())
# m1.add(Activation('ELU'))
# m1.add(Dense(12))
# m1.add(Activation('softmax'))

# # m1 = Sequential()
# # m1.add(BatchNormalization())
# # m1.add(Dense(512, input_shape=(956,), activation='ELU'))
# # m1.add(BatchNormalization())
# # m1.add(Activation('sigmoid'))
# # m1.add(Dense(256, activation='ELU'))
# # m1.add(BatchNormalization())
# # m1.add(Activation('sigmoid'))
# # m1.add(Dense(128, activation='ELU'))
# # m1.add(BatchNormalization())
# # m1.add(Activation('sigmoid'))
# # m1.add(Dense(64, activation='ELU'))
# # m1.add(BatchNormalization())
# # m1.add(Activation('sigmoid'))
# # m1.add(Dense(32, activation='ELU'))
# # m1.add(BatchNormalization())
# # m1.add(Activation('sigmoid'))
# # m1.add(Dense(12, activation='softmax'))
# # m1.add(Activation('softmax'))

# m1.compile(loss = 'categorical_crossentropy', metrics = ['accuracy'])
# hy = m1.fit(t_x, t_y, batch_size=32, epochs = 1000, callbacks = [mc], validation_data=(v_x, v_y))
# plt.plot(hy.history['loss'])
# plt.plot(hy.history['val_loss'])
# # plt.legend(loc='best', ncol=2)
# plt.show()
# print(m1.evaluate(t_x, t_y))
# print(m1.evaluate(tt_x, tt_y))
# print(m1.evaluate(v_x, v_y))

# m2 = Sequential()
# m2.add(Dense(512), input_dim=(956,) activation='sigmoid')
# m2.add(Dense(256, activation='sigmoid'))
# m2.add(Dense(128, activation='sigmoid'))
# m2.add(Dense(64, activation='sigmoid'))
# m2.add(Dense(32, activation='sigmoid'))
# m2.add(Dense(12, activation='softmax'))

# m2.compile('adam', 'sparse_categorical_crossentropy', 'accuracy')
# hy2 = m2.fit(t_x2, t_y2, epochs=1000, batch_size=128, callbacks=[es, mc], validation_data=(v_x2, v_y2))
# plt.plot(hy2.history['loss'])
# plt.plot(hy2.history['val_loss'])

from keras.models import load_model
lm = load_model('best_model.h')
print(lm.evaluate(t_x, t_y))
print(lm.evaluate(tt_x, tt_y))
print(lm.evaluate(v_x, v_y))