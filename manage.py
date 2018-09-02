from recommend import app, similarity, encode
from recommend.tools import getUserData, getFundData
from flask import render_template
from flask import request
import pandas as pd
import json
import numpy as np
import pandas as pd


#@app.route('/HuaTengProject/model/predictByNum',methods=['GET'])
#def predictByNum():
#    # result = CustomMessage.selectByEcifId("111111111111111000")
#    # json_str = tools.classToJson(result)
#    a = hierarchicalClustering()
#    a = pd.DataFrame(a)
#    return a

# a = predictByNum()
    

# data = getUserData()
# maxnum = data.max()
# dataArray = np.empty(shape=[len(data), 0])
# for i in range(21):
#     if i in [4,18,19]:
#         temp = encode.onehotencode(data[i])
#     else:
#         temp = encode.intervalencode(data[i], [0, maxnum.get(i)*0.25, maxnum.get(i)*0.5, maxnum.get(i)*0.75,maxnum.get(i)*1.01], ['0', '1', '2','3'])
#         temp = temp.ravel()
#         temp = temp.reshape((1000, 1))
#     dataArray = np.concatenate((dataArray, temp), axis=1)
# # cluster = AgglomerativeClustering(n_clusters=3, linkage='average', affinity='cosine').fit(dataArray)
# # label = cluster.labels_
# bandwidth = estimate_bandwidth(dataArray, quantile=0.2, n_samples=1000)
# cluster = MeanShift(bin_seeding=True, bandwidth=bandwidth)
# cluster.fit(dataArray)
# labels = cluster.labels_
# labels_unique = np.unique(labels)
# n_clusters_ = len(labels_unique)

# if __name__ == '__main__':
#     app.run()

data = getUserData()
result = getFundData()
