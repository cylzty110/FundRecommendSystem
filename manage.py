from recommend import app, models, db, recommend,tools
from recommend.custom import CustomMessage
from flask import request
import json



@app.route('/HuaTengProject/model/predictByNum',methods=['POST'])
def predictByNum():
    #data = request.get_data()
    #recommend.calculate('als')
    #print(data)
    result = CustomMessage.selectByEcifId("111111111111111000")
    json_str = tools.classToJson(result)
    return json_str



if __name__ == '__main__':
    app.run()
