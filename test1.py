# import xlrd
#
# workbook = xlrd.open_workbook('C:/Users/Think/Desktop/data.xlsx')
# sheet_names = workbook.sheet_names()
# result = ''
# for sheet_name in sheet_names:
#     sheet = workbook.sheet_by_name(sheet_name)
#     row1 = sheet.row_values(0)
#     row2 = sheet.row_values(1)
#     result += 'class ' + sheet_name + '(db.Model):\n'
#     result += "    __tablename__ = '" + sheet_name + "'\n"
#     result += "    ID = db.Column(db.Integer, primary_key=True)\n"
#     for index, value in enumerate(row1):
#         result += "    " + value.upper() + " = db.Column(db.String(255))"
#         result += "  # " + row2[index].replace('#', '') + '\n'
#     result += '\n\n'
# print(result)
# for sheet_name in sheet_names:
#     # print(sheet_name.lower() + " = None")
#     print("self." + sheet_name.lower() + " = " + sheet_name.upper() + "()")

from recommend.tools import getFundData, getUserData
from recommend import cluster, feature, encode
from recommend.tools import getAlphabet
import numpy as np
import pandas as pd

# data = getUserData()
# result = encode.normalization(data[0])
# result = result.reshape(len(data), 1)
# for index in range(1, 21):
#     if index not in [4, 18, 19]:
#         temp = encode.normalization(data[index])
#         temp = temp.reshape(len(data), 1)
#         result = np.hstack((result, temp))
# np.savetxt('C:/Users/Think/Desktop/data.csv', result, delimiter=',', fmt='%f')
# print("ok")
# labels1, label_num1, cluster_centers = cluster.MeanShift(result)
# labels2 = cluster.AgglomerativeClustering(result, 10)
# labels3 = cluster.MiniBatchKMeans(result, 10)
# labels4 = cluster.KMeans(result, 10)

user_data = getUserData()
user_feature = pd.DataFrame()

for index, item in enumerate(feature.get_user()):
    feature_vector = item.get_vector(user_data[index])  # 获取特征向量
    feature_vector = pd.DataFrame(feature_vector)  # 转换为dataframe
    feature_vector.rename(columns=lambda x: getAlphabet(index+1) + str(x), inplace=True)
    user_feature = pd.concat([user_feature, feature_vector], axis=1)
labels1, label_num1 = cluster.MeanShift(user_feature)

fund_data = getFundData()
fund_feature = pd.DataFrame()

for index, item in enumerate(feature.get_fund()):
    feature_vector = item.get_vector(fund_data[index])  # 获取特征向量
    feature_vector = pd.DataFrame(feature_vector)  # 转换为dataframe
    feature_vector.rename(columns=lambda x: getAlphabet(index+1) + str(x), inplace=True)
    fund_feature = pd.concat([fund_feature, feature_vector], axis=1)

