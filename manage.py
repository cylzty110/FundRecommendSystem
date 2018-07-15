from recommend import app, models, db
from flask import request


@app.route('/HuaTengProject/model/predictByNum',methods=['POST'])
def predictByNum():
    data = request.get_data()
    print(data)
    newobj = models.FundUserRelation(SCR_TXN_ACCNO="1")
    db.session.add(newobj)
    db.session.commit()
    return 'N'


if __name__ == '__main__':
    app.run()
