import pandas as pd
import numpy as np
from sklearn import preprocessing
from recommend.cluster import hierarchicalClustering


# 要求传输的是一个列向量 类型为pd.DataFrame
def intervalencode(data, bins, labels):
    data = np.array(data, dtype=np.float)
    result = pd.cut(data, bins, right=False, labels=labels)
    return result


# 要求传输的是一个列向量 类型为pd.DataFrame
def onehotencode(data):
    data = pd.get_dummies(data)
    result = np.array(data)
    return result


