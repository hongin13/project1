import pandas as pd
import numpy as np
from keras.utils.np_utils import to_categorical

import facemesh_test
import prep_test

def run():
    labels = {
        0 : 'Dragon', 1 : 'Monkey', 2 : 'Snake', 3 : 'Rabbit', 4 : 'Tiger', 5 : 'Sheep', 6 : 'Pig', 7 : 'Cow', 8 : 'Horse', 9 : 'Dog', 10 : 'Rooster', 11 : 'Mouse'
    }
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
    # print(y_pred)
    max_index = np.argmax(y_pred)
    return labels[max_index]


# l_m.evaluate(final_data, final_y)