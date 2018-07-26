import numpy as np
import pandas as pd
from sklearn import preprocessing
from recommend import models, custom
from recommend.custom import CustomMessage
from sklearn.cluster import AgglomerativeClustering

# enc = preprocessing.OneHotEncoder()
# enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
# print(enc.n_values_)
# print(enc.transform([[0, 1, 3]]).toarray())
# print(enc.transform([[0, 1, 1]]).toarray())


# 层次聚类
def hierarchicalClustering():
    userList = models.FundUserRelation.selectAll()
    dataArry = []
    oneHotArry = []
    for userId in userList:
        customMessage = CustomMessage.selectByEcifId(userId.CST_ID)
        dataArry.append(getDataArray(customMessage))
        oneHotArry.append(getOneHotArray(customMessage))

    dataArry = np.array(dataArry)
    oneHotArry = np.array(oneHotArry)
    oneHotArry = oneHotEncode(oneHotArry)
    dataArry = np.column_stack(oneHotArry)

    print(dataArry)
    # label_encode = preprocessing.LabelEncoder()
    # label_encode.fit(oneHotArry)

    cluster = AgglomerativeClustering(n_clusters=2, linkage='average').fit(dataArry)
    label = cluster.labels_
    return label


def oneHotEncode(oneHotArray):
    result = []
    for i in range(len(oneHotArray[0])):
        colum = oneHotArray[:, i]  # 取第i列数据

        for i in range(len(colum)):
            if colum[i] is None:
                colum[i] = 'empty'

        label_encode = preprocessing.LabelEncoder()
        label_encode.fit(colum)
        print(label_encode.transform(colum))





def getDataArray(customMessage):
    result = []
    for item in customMessage.depositMessage:
        result.append(item.accountBalance)
        result.append(item.accountCurrent)
        result.append(item.accountRegular)
        result.append(item.accountAverage)

    for item in customMessage.investMessage:
        result.append(item.chmtpdMonthAcm)
        result.append(item.chmtpdSeasonAcm)
        result.append(item.chmtpdYearAcm)
        result.append(item.monthAcmHpnLot)
        result.append(item.monthAcmHpCnt)
        result.append(item.monthAverageBal)

    for item in customMessage.bankInfo:
        result.append(item.chmtPdBalance)
        result.append(item.fundBalance)
        result.append(item.monthFundNum)
        result.append(item.timePointAum)
        result.append(item.monthAverageAum)
        result.append(item.yearDailyAum)

    for item in customMessage.basicMessage:
        result.append(item.age)
        result.append(item.income)

    return result


def getOneHotArray(customMessage):
    result = []
    for item in customMessage.investMessage:
        result.append(item.categoryCode)
        result.append(item.typeCode)

    for item in customMessage.channelInfo:
        result.append(item.settleFeeType)

    for item in customMessage.basicMessage:
        result.append(item.workFlag)
        result.append(item.education)
        result.append(item.custStatus)

    return result



