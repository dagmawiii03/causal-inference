import sys
import os
import unittest
import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler
import pickle

sys.path.insert(0, '../scripts/')
sys.path.append(os.path.abspath(os.path.join('scripts')))

from pre_process import Process

df = pd.DataFrame({'numbers': [2, 4, 6, 7, 9], 'letters': ['a', 'b', 'c', 'd', 'e'],
                   'floats': [0.2323, -0.23123, np.NaN, np.NaN, 4.3434]})


class TestCases(unittest.TestCase):

    def __init__(self):
        pass

    def test_custome_normalizer(self, df):
        return (df - df.mean()) / (df.std())

    def test_normalizer(self, df, columns):
        norm = Normalizer()
        return pd.DataFrame(norm.fit_transform(df), columns=columns)

    def test_scaler(self, df, columns):
        minmax_scaler = MinMaxScaler()
        return pd.DataFrame(minmax_scaler.fit_transform(df), columns=columns)

    def test_scale_and_normalize(self, df, columns):
        return self.normalizer(self.scaler(df, columns), columns)
    
    


if __name__ == '__main__':
    unittest.main()