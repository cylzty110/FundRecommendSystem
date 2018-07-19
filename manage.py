from recommend import app, models, db
from flask import request


@app.route('/HuaTengProject/model/predictByNum',methods=['POST'])
def predictByNum():
    data = request.get_data()
    print(data)
    return 'N'


if __name__ == '__main__':
    app.run()
