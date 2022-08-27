import os

def run():
    filepath = "C:/Users/aischool/Desktop/project/model/test"
    for root, dirs, filenames in os.walk(filepath):
        for filename in filenames:
            print(filename)
            path = os.path.join(root, filename)
            if os.path.exists(path):
                os.remove(path)

    filepath2 = "C:/Users/aischool/Desktop/project/model/test_json"
    for root, dirs, filenames in os.walk(filepath2):
        for filename in filenames:
            print(filename)
            path = os.path.join(root, filename)
            if os.path.exists(path):
                os.remove(path)

        