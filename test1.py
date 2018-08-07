from recommend.tools import getFundData, getUserData
from recommend.tools import getAllFundData, getAllUserData
from recommend import cluster, feature, models
from recommend.classification import SVM, LR
from recommend.tools import getAlphabet
from recommend import app, similarity
import pandas as pd
import numpy as np


# 聚类
user_data, user_list = getAllUserData()
user_feature = pd.DataFrame()

for index, item in enumerate(feature.get_user()):
    feature_vector = item.get_vector(user_data[index])  # 获取特征向量
    feature_vector = pd.DataFrame(feature_vector)  # 转换为dataframe
    feature_vector.rename(columns=lambda x: getAlphabet(index+1) + str(x), inplace=True)
    user_feature = pd.concat([user_feature, feature_vector], axis=1)
labels, label_num = cluster.MeanShift(user_feature)


# 根据聚类标签生成用户聚类簇
user_cluster = [[0 for col in range(0)] for row in range(label_num)]  # 用户聚类簇
for index, label in enumerate(labels):
    cst_id = user_list[index]
    user_cluster[label].append(cst_id)


# 分类
fund_data, fund_list = getAllFundData()
fund_feature = pd.DataFrame()
for index, item in enumerate(feature.get_fund()):
    feature_vector = item.get_vector(fund_data[index])  # 获取特征向量
    feature_vector = pd.DataFrame(feature_vector)  # 转换为dataframe
    feature_vector.rename(columns=lambda x: getAlphabet(index+1) + str(x), inplace=True)
    fund_feature = pd.concat([fund_feature, feature_vector], axis=1)

cls_list = []  # 分类器

# 对于每个聚类簇
for cluster_id in range(label_num):
    y = []  # 标签
    # 对于每款基金
    for fund_id in fund_list:
        data = models.FundFlow.selectByFundId(fund_id)  # 购买这款基金全部人的集合
        count = 0  # 计算聚类簇中购买基金的人数
        # 对于聚类簇内的用户
        for cst_id in user_cluster[cluster_id]:
            if cst_id in data:
                count = count + 1
        percent = count / len(user_cluster[cluster_id])  # 占比
        if percent > 0.05:
            y.append(1)
        else:
            y.append(0)
    # 构造分类器
    cls = SVM(fund_feature, y)
    cls_list.append(cls)

# 推荐
fund_id = '000693'  # 推荐基金的基金号
fund_info = getFundData(fund_id)
fund_feature = []  # 基金特征向量
dic = similarity.calculate('als', fund_id)  # 字典{user:score}
for index, item in enumerate(feature.get_fund()):
    data = list(fund_data[index])
    size = len(data)
    data.append(fund_info[index])
    vector = item.get_vector(data)
    if item.type == 'onehot':
        for num in vector[size]:
            fund_feature.append(num)
    else:
        fund_feature.append(vector[size])
fund_feature = np.array(fund_feature)

recommend_list = dict()  # 推荐列表
# 将基金属性放入分类器预测
for index, cls in enumerate(cls_list):
    label = cls.predict(fund_feature)
    if label == 1:
        for cst_id in user_cluster[index]:
            score = dic.get(cst_id)
            if score is not None:
                recommend_list[cst_id] = score


# 输出结果(按score降序排列)
recommend_list = sorted(recommend_list.items(), key=lambda x: x[1], reverse=True)
for user, score in recommend_list:
    print(user, score)


# @app.route('/HuaTengProject/model/predictByNum', methods=['POST'])
# def predict():
#
#     pass
#
#
# if __name__ == '__main__':
#     app.run()









