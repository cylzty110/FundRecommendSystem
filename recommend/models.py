from recommend import db


class FundUserRelation(db.Model):
    __tablename__ = "SCR_TNAC"
    ID = db.Column(db.Integer,primary_key=True)
    SCR_TXN_ACCNO = db.Column(db.String(255))
    CST_ID = db.Column(db.String(255))
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


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


class Similarity(db.Model):
    __tablename__ = "SIMILARITY"
    ID = db.Column(db.Integer, primary_key=True)
    FUND_ID_FIRST = db.Column(db.String(255))
    FUND_ID_SECOND = db.Column(db.String(255))
    SCORE = db.Column(db.String(255))


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


class RecommendData(db.Model):
    __tablename__ = "TT_FUND_DATA"
    ID = db.Column(db.Integer, primary_key=True)
    USERID = db.Column(db.String(255))
    PROBILITY = db.Column(db.String(255))
    TASK_BATCH = db.Column(db.String(255))
    CREATE_DATE = db.Column(db.String(255))

