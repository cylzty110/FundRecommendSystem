import pandas as pd
import numpy as np
from sklearn import preprocessing

# 返回值类型统一为numpy.ndarray


# 连续值离散化
def intervalencode(data, bins):
    data = np.array(data, dtype=np.float)
    length = len(bins)
    labels = []
    for i in range(length-1):
        labels.append(i)
    data = pd.cut(data, bins, right=False, labels=labels)
    result = np.array(data.tolist())
    return result


# one-hot编码
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
def standardization(data):
    data = np.array(data, dtype=np.float)
    result = preprocessing.scale(data, axis=0, with_mean=True, with_std=True)
    return result


# 数据正则化
def normalization(data):
    data = np.array(data, dtype=np.float)
    result = preprocessing.normalize(data, norm='l2')
    return result