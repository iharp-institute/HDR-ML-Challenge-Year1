import numpy as np


class Model:
    def __init__(self):
        print("Model initialized")

    def predict(self, x):

        return np.random.randint(2, size=(1, 12))
        # return np.zeros((1, 12))
        # return np.ones((1, 12))
