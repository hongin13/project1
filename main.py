import cv2
import os
import math
import numpy as np
import pandas as pd
import json

l_json = []
for root, dirs, filenames in os.walk('json'):
    for filename in filenames:
        path = os.path.join(root, filename)
        with open(path, 'r') as f:
            json_data = json.load(f)
            l_json.append(json_data)
        # print(json.dumps(json_data))

df = pd.DataFrame(l_json)
print(df)
