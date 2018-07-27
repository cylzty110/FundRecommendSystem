from recommend import app, recommend, encode
from recommend.custom import CustomMessage
from recommend.cluster import AgglomerativeClustering
from recommend.tools import getData
from flask import render_template
from flask import request
import pandas as pd
import json
import numpy as np


#@app.route('/HuaTengProject/model/predictByNum',methods=['GET'])
#def predictByNum():
#    # result = CustomMessage.selectByEcifId("111111111111111000")
#    # json_str = tools.classToJson(result)
#    a = hierarchicalClustering()
#    a = pd.DataFrame(a)
#    return a

# a = predictByNum()
    
import pandas as pd
from recommend.cluster import hierarchicalClustering



# a = hierarchicalClustering  ()
# a = pd.DataFrame(a)
# data12 = np.array(a[0].T, dtype=np.float)
# bins = [0, 2000, 8000, 20000, 50000, 100000]
#
# labels = ['究极贫困人口', '一般贫困人口', '普通人口', '较富有人口', '富有人口']
#
# data = pd.cut(data12, bins,right= False, labels = labels)
# adwq = data
data = getData()
maxnum = data.max()
dataArray = np.empty(shape=[len(data), 0])
for i in range(24):
    if i in [4, 17, 18, 21, 22]:
        temp = encode.onehotencode(data[i])
    else:
        temp = encode.intervalencode(data[i], [0, maxnum.get(i)/2, maxnum.get(i) + 1], ['0', '1'])
        temp = temp.ravel()
        temp = temp.reshape((1000, 1))
    dataArray = np.concatenate((dataArray, temp), axis=1)
cluster = AgglomerativeClustering(n_clusters=3, linkage='average').fit(dataArray)
label = cluster.labels_

# if __name__ == '__main__':
#     app.run()
