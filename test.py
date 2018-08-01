import numpy as np
from recommend.tools import getUserData
from recommend import encode
from recommend import cluster
import pandas as pd

count = 0
df = getUserData()
data = np.array(df)
feature = []
feature = pd.DataFrame(feature)

# 区间编码中的区间与标签
account_bins = [0, 2000, 6000, 10000, 15000, 50000, 200000, float('inf')]
account_label = [0, 1, 2, 3, 4, 5, 6]
#对用户数据的第一列(账户余额)进行区间编码
feature = pd.DataFrame(encode.intervalencode(df[0], account_bins, account_label).tolist())

#对用户数据的第二列(账户活期存款余额)进行区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[1], account_bins, account_label).tolist()), lsuffix='A', rsuffix='B')

##对用户数据的第三列(账户定期存款余额)进行区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[2], account_bins, account_label).tolist()))
#
##对用户数据的第四列(账户存款月日均余额)进行区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[3], account_bins, account_label).tolist()), lsuffix='C', rsuffix='D')
#
##对用户数据的第五列(投资理财产品类型码)进区间编码
feature = feature.join(pd.DataFrame(encode.onehotencode(df[4])))
#
##对用户数据的第六列(投资理财产品月积数)进区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[5], account_bins, account_label).tolist()), lsuffix='E', rsuffix='F')
#
##对用户数据的第七列(投资理财产品季积数)进区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[6], account_bins, account_label).tolist()))
#
##对用户数据的第八列(投资理财产品年积数)进区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[7], account_bins, account_label).tolist()), lsuffix='G', rsuffix='H')
#
##对用户数据的第九列(月累计发生份额)进区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[8], account_bins, account_label).tolist()))
#
feature = feature.join(df[9])

#对用户数据的第十一列(月累计发生份额)进区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[10], account_bins, account_label).tolist()), lsuffix='I', rsuffix='J')
#
##对用户数据的第十二列(基金余额)进区间编码
feature = feature.join(df[11])
#
##对用户数据的第十三列(基金月日均数)进区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[12], account_bins, account_label).tolist()))
#
##对用户数据的第十四列(客户时点AUM值)进区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[13], account_bins, account_label).tolist()), lsuffix='M', rsuffix='N')
#
##对用户数据的第十五列(基金月日均数)进区间编码
feature = feature.join(df[14])
#
##对用户数据的第十六列(客户年日均AUM值)进区间编码
feature = feature.join(pd.DataFrame(encode.intervalencode(df[15], account_bins, account_label).tolist()))
#
##年龄
feature = feature.join(pd.DataFrame(df[16]))
#
##月收入
feature = feature.join(pd.DataFrame(df[17]))
#
##学历
feature = feature.join(pd.DataFrame(encode.onehotencode(df[18])), lsuffix='AA', rsuffix='BB' )
#
##客户平台状态
feature = feature.join(pd.DataFrame(encode.onehotencode(df[19])), lsuffix='CC', rsuffix='DD' )
#
##交易金额
feature = feature.join(pd.DataFrame(encode.intervalencode(df[20], account_bins, account_label).tolist()), lsuffix='S', rsuffix='T')

a_labels = cluster.AgglomerativeClustering(feature, 5)
b_labels = cluster.KMeans(feature, 5)
c_labels = cluster.MiniBatchKMeans(feature, 5)
d_labels = cluster.MeanShift(feature, 0.02)
e_labels = cluster.Bitch(feature, 5)

feature.to_csv('D:\user\Cui\result.csv')
##"""Birch
#cluster = cluster.Birch(n_clusters=7)
#cluster.fit_predict(data)
#labels = cluster.labels_
##"""
#for index, type in enumerate(labels):
#    if type+1 == realType[index]:
#        count = count + 1
#print(count / len(labels))


