from recommend import db, tools
import flask_sqlalchemy


#基金交易账户表
class FundUserRelation(db.Model):
    __tablename__ = "SCR_TNAC"
    ID = db.Column(db.Integer,primary_key=True)
    SCR_TXN_ACCNO = db.Column(db.String(255))
    CST_ID = db.Column(db.String(255))
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))



#基金交易流水
class FundFlow(db.Model):
    __tablename__ = "SCR_TXNDN_INF"
    ID = db.Column(db.Integer,primary_key=True)
    TXN_CFM_DT = db.Column(db.String(255))
    FNDBGAMTRDMTNPCSGTPCD = db.Column(db.String(255))
    CFM_PCSG_TXNSRLNO = db.Column(db.String(255))
    CFM_TXNAMT = db.Column(db.String(255))
    SCR_TXN_ACCNO = db.Column(db.String(255))
    CST_SCRTACNO = db.Column(db.String(255))
    TXN_ITT_CHNL_CGY_CODE = db.Column(db.String(255))
    BYSLDRC_CD = db.Column(db.String(255))
    SYS_TX_CODE = db.Column(db.String(255))
    SCR_PD_ECD = db.Column(db.String(255))
    APLY_ID = db.Column(db.String(255))
    CFM_TXN_LOT = db.Column(db.String(255))
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))



#相似度矩阵
class Similarity(db.Model):
    __tablename__ = "SIMILARITY"
    ID = db.Column(db.Integer, primary_key=True)
    FUND_ID_FIRST = db.Column(db.String(255))
    FUND_ID_SECOND = db.Column(db.String(255))
    SCORE = db.Column(db.String(255))

    @staticmethod
    def insert(self):
        db.session.add(self)
        db.session.commit()


    @staticmethod
    def deleteAll():
        db.session.execute("truncate table SIMILARITY")
        db.session.commit()


    def batchInsert(data):
        list =  tools.classToDict(data)
        db.session.execute(RecommendData.__table__.insert(),list)


#日志
class TaskLog(db.Model):
    __tablename__ = "TS_TASK_INFO"
    TASK_ID = db.Column(db.Integer, primary_key=True)
    TASK_TABLE_MSG = db.Column(db.String(255))
    TASK_TABLE_BATCH_MSG = db.Column(db.String(255))
    TASK_RETURN_MESSAGE = db.Column(db.String(255))
    TASK_DATE = db.Column(db.String(255))
    TASK_RETURN_DATE = db.Column(db.String(255))
    TASK_BATCH = db.Column(db.String(255))
    CREATE_USER_ID = db.Column(db.String(255))
    CREATE_DATE = db.Column(db.String(255))
    TASK_STATUS = db.Column(db.String(255))

    #批量插入
    @staticmethod
    def insert(self):
        db.session.add(self)
        db.session.commit()



#推荐结果
class RecommendData(db.Model):
    __tablename__ = "TT_FUND_DATA"
    ID = db.Column(db.Integer, primary_key=True)
    USERID = db.Column(db.String(255))
    PROBILITY = db.Column(db.String(255))
    TASK_BATCH = db.Column(db.String(255))
    CREATE_DATE = db.Column(db.String(255))

    @staticmethod
    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def deleteAll():
        db.session.execute("truncate table TT_FUND_DATA")
        db.session.commit()

    #批量插入
    @staticmethod
    def batchInsert(data):
        list =  tools.classToDict(data)
        db.session.execute(RecommendData.__table__.insert(),list)






