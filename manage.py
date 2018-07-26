from recommend import app, models, db, recommend,tools
from recommend.custom import CustomMessage
from recommend.cluster import hierarchicalClustering
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

a = hierarchicalClustering  ()
a = pd.DataFrame(a)
data12 = np.array(a[0].T, dtype=np.float)
bins = [0, 2000, 8000, 20000, 50000, 100000]

labels = ['究极贫困人口', '一般贫困人口', '普通人口', '较富有人口', '富有人口']

data = pd.cut(data12, bins,right= False, labels = labels)
adwq = data


# if __name__ == '__main__':
#     app.run()
