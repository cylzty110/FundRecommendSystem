import pandas as pd
import numpy as np
from sklearn import preprocessing


# 连续值离散化
def intervalencode(data, bins, labels):
    data = np.array(data, dtype=np.float)
    result = pd.cut(data, bins, right=False, labels=labels)
    return result


# 独热编码
def onehotencode(data):
    data = pd.get_dummies(data)
    result = np.array(data)
    return result


# 区间缩放
def minmaxencode(data):
    data = np.array(data, dtype=np.float)
    Max = np.max(data)
    Min = np.min(data)
    for index, num in enumerate(data):
        data[index] = (num - Min) / (Max - Min)
    return data


# 数据标准化
def normalization(data):
    result = preprocessing.scale(data, axis=0, with_mean=True, with_std=True)
    return result




