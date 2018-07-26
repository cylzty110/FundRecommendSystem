from recommend import app, models, db, recommend,tools
from recommend.custom import CustomMessage
from recommend.cluster import hierarchicalClustering
from flask import request
import json



@app.route('/HuaTengProject/model/predictByNum',methods=['POST'])
def predictByNum():
    #data = request.get_data()
    #recommend.calculate('als')
    #print(data)
    # result = CustomMessage.selectByEcifId("111111111111111000")
    # json_str = tools.classToJson(result)
    hierarchicalClustering()
    return 'N'



if __name__ == '__main__':
    app.run()
