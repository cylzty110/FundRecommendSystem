from recommend import encode
import numpy as np


# 特征构建
class Feature:
    def __init__(self, types, bins=[]):
        self.type = types
        self.bins = bins

    # 获取特征向量
    def get_vector(self, data):
        if self.type is 'interval':
            result = encode.intervalencode(data, self.bins)
        elif self.type is 'onehot':
            result = encode.onehotencode(data)
        elif self.type is 'minmax':
            result = encode.minmaxencode(data)
        elif self.type is 'standardization':
            result = encode.standardization(data)
        elif self.type is 'normalization':
            result = encode.normalization(data)
        else:
            result = np.array(data)
        return result


def get_user():
    result = []
    bins = [0, 2000, 4000, 6000, 8000, 10000, 15000, 20000, 30000, 40000,
            50000, 100000, 200000, 300000, 400000, 500000, 1000000, 5000000, float('inf')]
    result.append(Feature('interval', bins))  # 账户余额

    bins = [0, 5000, 10000, 20000, 50000, 100000, 1000000, float('inf')]
    result.append(Feature('interval', bins))  # 账户活期存款余额

    bins = [0, 5000, 10000, 20000, 50000, 100000, 1000000, float('inf')]
    result.append(Feature('interval', bins))  # 账户定期存款余额

    bins = [0, 5000, 10000, 20000, 50000, 100000, 1000000, float('inf')]
    result.append(Feature('interval', bins))  # 账户存款月日均余额

    bins = [0, 5000, 10000, 20000, 50000, 100000, 500000, 1000000,
            5000000, 10000000, float('inf')]
    result.append(Feature('interval', bins))  # 投资理财产品月积数

    bins = [0, 5000, 10000, 20000, 50000, 100000, 1000000, float('inf')]
    result.append(Feature('interval', bins))  # 投资理财产品季积数

    bins = [0, 5000, 10000, 20000, 50000, 100000, 1000000, float('inf')]
    result.append(Feature('interval', bins))  # 投资理财产品年积数

    bins = [0, 5000, 10000, 20000, 50000, 100000, 1000000, float('inf')]
    result.append(Feature('interval', bins))  # 月累计发生份额

    bins = [0, 5, 10, 20, 50, 100, float('inf')]
    result.append(Feature('interval', bins))  # 月累计发生次数

    bins = [0, 5000, 10000, 20000, 50000, 100000, 1000000, float('inf')]
    result.append(Feature('interval', bins))  # 月日均余额

    bins = [0, 5, 10, 20, 50, 100, float('inf')]
    result.append(Feature('interval', bins))  # 基金余额

    bins = [0, 100, 500, 1000, 5000, 10000, 50000, 100000, float('inf')]
    result.append(Feature('interval', bins))  # 基金月日均数

    bins = [0, 100, 500, 1000, 5000, 10000, 50000, 100000, float('inf')]
    result.append(Feature('interval', bins))  # 客户时点AUM值

    bins = [0, 100, 500, 1000, 5000, 10000, 50000, 100000, float('inf')]
    result.append(Feature('interval', bins))  # 客户月均AUM值

    bins = [0, 100, 500, 1000, 5000, 10000, 50000, 100000, float('inf')]
    result.append(Feature('interval', bins))  # 客户年日均AUM值

    bins = [0, 18, 30, 50, 80]
    result.append(Feature('interval', bins))  # 年龄

    result.append(Feature('other'))  # 月收入

    result.append(Feature('onehot'))  # 学历

    result.append(Feature('onehot'))  # 客户平台状态

    bins = [0, 2000, 4000, 6000, 8000, 10000, 15000, 20000, 30000, 40000,
            50000, 100000, 200000, 300000, 400000, 500000, 1000000, 5000000, float('inf')]
    result.append(Feature('interval', bins))  # 交易金额
    return result


def get_fund():
    result = []
    bins = [0, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, float('inf')]
    result.append(Feature('interval', bins))  # 关注该基金人数

    result.append(Feature('minmax'))  # 基金首次销售服务费率

    result.append(Feature('minmax'))  # 基金销售服务费年费率

    result.append(Feature('other'))  # 基金风险等级代码

    bins = [0, 1, 3, 5, 10, 20, 50, 100, float('inf')]
    result.append(Feature('interval', bins))  # 单位基金分红金额

    bins = [0, 1, 3, 5, 10, 20, 50, 100, float('inf')]
    result.append(Feature('interval', bins))  # 本次基金单位分红金额

    bins = [0, 1, 3, 5, 10, 20, 50, 100, float('inf')]
    result.append(Feature('interval', bins))  # 年累计金额
    return result
