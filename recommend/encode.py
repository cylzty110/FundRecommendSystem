import pandas as pd
import numpy as np
from sklearn import preprocessing
from recommend.cluster import hierarchicalClustering

# 要求传输的是一个列向量 类型为pd.DataFrame
def intervalencode(data):

    data = np.array(data.T, dtype=np.float)
    bins = [0, 2000, 8000, 20000, 50000, 100000]
    labels = ['0', '1', '2', '3', '4']
    data = pd.cut(data, bins, right=False, labels=labels)
    result = np.array(data)
    return result

# 要求传输的是一个列向量 类型为pd.DataFrame
def onehotencode(data):
    data = pd.get_dummies(data)
    result = np.array(data)
    return result


