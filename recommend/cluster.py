import numpy as np
from sklearn import preprocessing

from recommend import models
from recommend.custom import CustomMessage


# enc = preprocessing.OneHotEncoder()
# enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
# print(enc.n_values_)
# print(enc.transform([[0, 1, 3]]).toarray())
# print(enc.transform([[0, 1, 1]]).toarray())


# 层次聚类
def hierarchicalClustering():
    userList = models.TBL_CUST_ID_CONV.selectAll()
    dataArry = []
    oneHotArry = []
    for userId in userList:
        customMessage = CustomMessage.selectByEcifId(userId.ECIF_CST_ID)
        dataArry.append(getDataArray(customMessage))
        oneHotArry.append(getOneHotArray(customMessage))

    dataArry = np.array(dataArry)
    oneHotArry = np.array(oneHotArry)
    print(dataArry)
    oneHotArry = oneHotEncode(oneHotArry)
    # dataArry = np.column_stack(oneHotArry)

    return dataArry
    # label_encode = preprocessing.LabelEncoder()
    # label_encode.fit(oneHotArry)

    # cluster = AgglomerativeClustering(n_clusters=2, linkage='average').fit(dataArry)
    # label = cluster.labels_
    # return label


def oneHotEncode(oneHotArray):
    result = []
    for i in range(len(oneHotArray[0])):
        colum = oneHotArray[:, i]  # 取第i列数据

        for i in range(len(colum)):
            if colum[i] is None:
                colum[i] = 'empty'


        label_encode = preprocessing.LabelEncoder()
        label_encode.fit(colum)
        #print(label_encode.transform(colum))


def getDataArray(customMessage):
    result = []
    result.append(customMessage.depositMessage.accountBalance)
    result.append(customMessage.depositMessage.accountCurrent)
    result.append(customMessage.depositMessage.accountRegular)
    result.append(customMessage.depositMessage.accountAverage)

    result.append(customMessage.investMessage.chmtpdMonthAcm)
    result.append(customMessage.investMessage.chmtpdSeasonAcm)
    result.append(customMessage.investMessage.chmtpdYearAcm)
    result.append(customMessage.investMessage.monthAcmHpnLot)
    result.append(customMessage.investMessage.monthAcmHpCnt)
    result.append(customMessage.investMessage.monthAverageBal)

    result.append(customMessage.bankInfo.chmtPdBalance)
    result.append(customMessage.bankInfo.fundBalance)
    result.append(customMessage.bankInfo.monthFundNum)
    result.append(customMessage.bankInfo.timePointAum)
    result.append(customMessage.bankInfo.monthAverageAum)
    result.append(customMessage.bankInfo.yearDailyAum)

    result.append(customMessage.basicMessage.age)
    result.append(customMessage.basicMessage.income)

    return result


def getOneHotArray(customMessage):
    result = []
    result.append(customMessage.investMessage.categoryCode)

    result.append(customMessage.channelInfo.settleFeeType)

    result.append(customMessage.basicMessage.workFlag)
    result.append(customMessage.basicMessage.education)
    result.append(customMessage.basicMessage.custStatus)

    return result



