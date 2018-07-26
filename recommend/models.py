from recommend import db, tools
import flask_sqlalchemy


# 基金交易账户表
class FundUserRelation(db.Model):
    __tablename__ = "SCR_TNAC"
    ID = db.Column(db.Integer,primary_key=True)
    SCR_TXN_ACCNO = db.Column(db.String(255))
    CST_ID = db.Column(db.String(255))
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))



# 基金交易流水
class FundFlow(db.Model):
    __tablename__ = "SCR_TXNDN_INF"
    ID = db.Column(db.Integer, primary_key=True)
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

    @staticmethod
    def selectAll():
        result = db.session.query(FundUserRelation.CST_ID,FundFlow.SCR_PD_ECD).\
            filter(FundUserRelation.SCR_TXN_ACCNO == FundFlow.SCR_TXN_ACCNO).all()
        return result


# 相似度矩阵
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


# 日志
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


# 推荐结果
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


# 个人客户存款产品持有
class ADS_CUST_HOLD_DEPOSIT(db.Model):
    __tablename__ = "ADS_CUST_HOLD_DEPOSIT"
    ID = db.Column(db.Integer, primary_key=True)
    DATA_DT = db.Column(db.String(255))
    ECIF_CST_ID = db.Column(db.String(255))
    DEP_TPCD = db.Column(db.String(255))
    DEP_TPDS = db.Column(db.String(255))
    CCYCD = db.Column(db.String(255))
    DEP_ACC_NUM = db.Column(db.String(255))
    ACBA = db.Column(db.String(255))
    CNVR_CNY_ACBA = db.Column(db.String(255))
    YR_INNR_ACM = db.Column(db.String(255))
    CNVR_CNY_YR_INNR_ACM = db.Column(db.String(255))
    SSN_INNR_ACM = db.Column(db.String(255))
    CNVR_CNY_SSN_INNR_ACM = db.Column(db.String(255))
    MO_INNR_ACM = db.Column(db.String(255))
    CNVR_CNY_MO_INNR_ACM = db.Column(db.String(255))
    RCTLY12MO_DEP_BAL_ACM = db.Column(db.String(255))
    CNVRCNYR12MODEPBALACM = db.Column(db.String(255))
    MO_ACM_DBT_TXNAMT = db.Column(db.String(255))
    CNVRCNYMOACMDBTTXNAMT = db.Column(db.String(255))
    MO_ACM_DBT_TDNUM = db.Column(db.String(255))
    MO_ACM_CR_TXNAMT = db.Column(db.String(255))
    CNVRCNYMOACMCR_TXNAMT = db.Column(db.String(255))
    MO_ACM_CR_TDNUM = db.Column(db.String(255))
    ACC_TMDEP_BAL = db.Column(db.String(255))
    CNVRCNY_ACC_TMDEP_BAL = db.Column(db.String(255))
    ACC_DMDDEP_BAL = db.Column(db.String(255))
    CNVRCNYACC_DMDDEP_BAL = db.Column(db.String(255))
    ACC_TMDEP_MO_DABAL = db.Column(db.String(255))
    CNVRCNYACCTDEPMODABAL = db.Column(db.String(255))
    ACC_DMDDEP_MO_DABAL = db.Column(db.String(255))
    CNVRCNYACCDDEPMODABAL = db.Column(db.String(255))
    ACC_DEP_MO_DABAL = db.Column(db.String(255))
    CNVRCNYACCDEPMO_DABAL = db.Column(db.String(255))



# 客户理财产品持有信息
class ADS_CUST_HOLD_INVEST(db.Model):
    __tablename__ = "ADS_CUST_HOLD_INVEST"
    ID = db.Column(db.Integer, primary_key=True)
    DATA_DT = db.Column(db.String(255))
    ECIF_CST_ID = db.Column(db.String(255))
    INSNO = db.Column(db.String(255))
    IVS_CHMTPD_CGY_CD = db.Column(db.String(255))
    IVS_CHMTPD_CGY_DSC = db.Column(db.String(255))
    IVS_CHMTPD_TP_CD = db.Column(db.String(255))
    IVS_CHMTPD_TPDS = db.Column(db.String(255))
    CCYCD = db.Column(db.String(255))
    IVS_CHMTPD_ACC_NUM = db.Column(db.String(255))
    IVS_CHMTPD_TMPNT_LOT = db.Column(db.String(255))
    IVS_CHMTPD_TMPNT_BAL = db.Column(db.String(255))
    CNVRCNYIVSCPDTMPNTBAL = db.Column(db.String(255))
    IVS_CHMTPD_MO_ACM = db.Column(db.String(255))
    CNVRCNYIVSCHMTPDMOACM = db.Column(db.String(255))
    IVS_CHMTPD_SSN_ACM = db.Column(db.String(255))
    CNVRCNYISCHMTPDSSNACM = db.Column(db.String(255))
    IVS_CHMTPD_YR_ACM = db.Column(db.String(255))
    CNVRCNYIVSCHMTPDYRACM = db.Column(db.String(255))
    MO_ACM_HPN_AMT = db.Column(db.String(255))
    CNVRCNYMO_ACM_HPN_AMT = db.Column(db.String(255))
    MO_ACM_HPN_LOT = db.Column(db.String(255))
    MO_ACM_HPCNT = db.Column(db.String(255))
    MO_DABAL = db.Column(db.String(255))
    CNVR_CNY_MO_DABAL = db.Column(db.String(255))
    LASTTM_TXN_DT = db.Column(db.String(255))
    SIGN_DT = db.Column(db.String(255))


# 个人客户银行管理信息
class ADS_PERS_CUST_BANK_INFO(db.Model):
    __tablename__ = "ADS_PERS_CUST_BANK_INFO"
    ID = db.Column(db.Integer, primary_key=True)
    DATA_DT = db.Column(db.String(255))
    CST_NO = db.Column(db.String(255))
    AGE = db.Column(db.String(255))
    DMDDEP_CST_IND = db.Column(db.String(255))
    TMDEP_CST_IND = db.Column(db.String(255))
    PSNLOAN_CST_IND = db.Column(db.String(255))
    DBCRD_CST_IND = db.Column(db.String(255))
    QCRCRD_CST_IND = db.Column(db.String(255))
    LNCRD_CST_IND = db.Column(db.String(255))
    LNCRDBIGATINSTMCSTIND = db.Column(db.String(255))
    BNK_CHRTC_CST_IND = db.Column(db.String(255))
    NATDBT_CST_IND = db.Column(db.String(255))
    BOND_CST_IND = db.Column(db.String(255))
    FND_CST_IND = db.Column(db.String(255))
    INS_CST_IND = db.Column(db.String(255))
    PM_CST_IND = db.Column(db.String(255))
    STDNT_PREF_CST_IND = db.Column(db.String(255))
    PRVDFND_CST_IND = db.Column(db.String(255))
    TRDPT_SVMGT_CST_IND = db.Column(db.String(255))
    ACC_PY_CST_IND = db.Column(db.String(255))
    SHRCT_PY_CST_IND = db.Column(db.String(255))
    TRM_TMPNT_BAL = db.Column(db.String(255))
    TRM_MO_DA_NUM = db.Column(db.String(255))
    CRN_TMPNT_BAL = db.Column(db.String(255))
    CRN_MO_DA_NUM = db.Column(db.String(255))
    CCB_CHMTPD_BAL = db.Column(db.String(255))
    CCBCHMTPDBALMO_DA_NUM = db.Column(db.String(255))
    NATDBT_BAL = db.Column(db.String(255))
    NATDBT_MO_DA_NUM = db.Column(db.String(255))
    BOND_BAL = db.Column(db.String(255))
    BOND_MO_DA_NUM = db.Column(db.String(255))
    TRDPT_SVMGT_BAL = db.Column(db.String(255))
    TRDPT_SVMGT_MO_DA_NUM = db.Column(db.String(255))
    FND_BAL = db.Column(db.String(255))
    FND_MO_DA_NUM = db.Column(db.String(255))
    INS_AMT = db.Column(db.String(255))
    INS_MO_DA_NUM = db.Column(db.String(255))
    PM_BAL = db.Column(db.String(255))
    PM_MO_DA_NUM = db.Column(db.String(255))
    CRCRD_OD_BAL = db.Column(db.String(255))
    PSNLOAN_BAL = db.Column(db.String(255))
    PSNLOAN_MO_DA_NUM = db.Column(db.String(255))
    CST_TMPNTAUM_VAL = db.Column(db.String(255))
    CST_MOAVGAUM_VAL = db.Column(db.String(255))
    CST_YR_DAAUM_VAL = db.Column(db.String(255))
    MPB_SIGN_ST = db.Column(db.String(255))
    SMS_SIGN_ST = db.Column(db.String(255))
    EBNKG_SIGN_ST = db.Column(db.String(255))
    EBNKGRCTLY_OC_LAND_DT = db.Column(db.String(255))
    MPB_RCTLY_OC_LAND_DT = db.Column(db.String(255))
    DBCRD_FTM_SIGN_TM = db.Column(db.String(255))
    RCTLY_OC_DBCRD_USE_TM = db.Column(db.String(255))
    QCRCRD_FTM_SIGN_TM = db.Column(db.String(255))
    RCTLYOC_QCRCRD_USE_TM = db.Column(db.String(255))
    FSTTM_TMDEP_TM = db.Column(db.String(255))
    RCTLY_OC_TMDEP_TM = db.Column(db.String(255))
    FSTTM_LN_APLY_TM = db.Column(db.String(255))
    RCTLY_OC_LN_APLY_TM = db.Column(db.String(255))
    ACC_PY_FTM_SIGN_TM = db.Column(db.String(255))
    RCTLYOC_ACC_PY_HPN_TM = db.Column(db.String(255))
    SHRCT_PY_FTM_SIGN_TM = db.Column(db.String(255))
    RCTLYOCSHRCTPY_HPN_TM = db.Column(db.String(255))
    BNK_CHRTC_FTM_PRCH_TM = db.Column(db.String(255))
    RCTLYOCPRCHBNKCHRTCTM = db.Column(db.String(255))
    NATDBT_FTM_PRCH_TM = db.Column(db.String(255))
    RCTLYOCPRCH_NATDBT_TM = db.Column(db.String(255))
    BOND_FTM_PRCH_TM = db.Column(db.String(255))
    RCTLY_OC_PRCH_BOND_TM = db.Column(db.String(255))
    FND_FTM_PRCH_TM = db.Column(db.String(255))
    RCTLY_OC_PRCH_FND_TM = db.Column(db.String(255))
    INS_FTM_PRCH_TM = db.Column(db.String(255))
    RCTLY_OC_PRCH_INS_TM = db.Column(db.String(255))
    PM_FTM_PRCH_TM = db.Column(db.String(255))
    RCTLY_OC_PRCH_PM_TM = db.Column(db.String(255))


# 个贷产品持有信息
class ADS_PERS_LOAN_PROD_HOLD_INFO(db.Model):
    __tablename__ = "ADS_PERS_LOAN_PROD_HOLD_INFO"
    ID = db.Column(db.Integer, primary_key=True)
    DATA_DT = db.Column(db.String(255))
    ECIF_CST_NO = db.Column(db.String(255))
    LN_TPCD = db.Column(db.String(255))
    LN_TPDS = db.Column(db.String(255))
    LDGR_INST_ORG_IND = db.Column(db.String(255))
    CCYCD = db.Column(db.String(255))
    LVL12_CLCD = db.Column(db.String(255))
    ACC_NUM = db.Column(db.String(255))
    RGLR_PNP_BAL = db.Column(db.String(255))
    ODUE_PNP_BAL = db.Column(db.String(255))
    NONACR_PNP_BAL = db.Column(db.String(255))
    YR_INNR_RGLR_PNP_ACM = db.Column(db.String(255))
    SSN_INNR_RGLR_PNP_ACM = db.Column(db.String(255))
    MO_INNR_RGLR_PNP_ACM = db.Column(db.String(255))
    YR_INNR_ODUE_PNP_ACM = db.Column(db.String(255))
    SSN_INNR_ODUE_PNP_ACM = db.Column(db.String(255))
    MO_INNR_ODUE_PNP_ACM = db.Column(db.String(255))
    YRINNR_NONACR_PNP_ACM = db.Column(db.String(255))
    SSNINNRNONACR_PNP_ACM = db.Column(db.String(255))
    MOINNR_NONACR_PNP_ACM = db.Column(db.String(255))
    LN_DSTR_AMT = db.Column(db.String(255))


# 电子渠道个人签约客户渠道信息
class PRIV_CHANL_INFO(db.Model):
    __tablename__ = "PRIV_CHANL_INFO"
    ID = db.Column(db.Integer, primary_key=True)
    CUST_NO = db.Column(db.String(255))
    CHANL_NO = db.Column(db.String(255))
    CUST_CHANL_STS = db.Column(db.String(255))
    ARRE_STS = db.Column(db.String(255))
    OLD_CUST_GRD = db.Column(db.String(255))
    SIGN_STS = db.Column(db.String(255))
    FLT_CUST_GRD = db.Column(db.String(255))
    SIGN_DATE = db.Column(db.String(255))
    END_SIGN_DATE = db.Column(db.String(255))
    SERV_FEE_TYP = db.Column(db.String(255))
    STL_FEE_TYP = db.Column(db.String(255))
    REB_RAT = db.Column(db.String(255))
    CHG_DATE = db.Column(db.String(255))
    CONTRIBUTION_LEVEL = db.Column(db.String(255))


# 电子渠道个人签约客户基本信息
class PRIV_CUST_INFO(db.Model):
    __tablename__ = "PRIV_CUST_INFO"
    ID = db.Column(db.Integer, primary_key=True)
    CUST_NO = db.Column(db.String(255))
    CERT_ID = db.Column(db.String(255))
    WORK_FLG = db.Column(db.String(255))
    SEX = db.Column(db.String(255))
    BIRDAY = db.Column(db.String(255))
    MRG_COND = db.Column(db.String(255))
    NATY_NAME = db.Column(db.String(255))
    PPL_NAME = db.Column(db.String(255))
    EDUC = db.Column(db.String(255))
    MN_INCOM = db.Column(db.String(255))
    HOME_ADDR = db.Column(db.String(255))
    UNIT_ADDR = db.Column(db.String(255))
    UNIT_TYP = db.Column(db.String(255))
    ADDR = db.Column(db.String(255))
    TELEPH = db.Column(db.String(255))
    EMAIL_ADDR = db.Column(db.String(255))
    FAX_NO = db.Column(db.String(255))
    DEPEND_NO = db.Column(db.String(255))
    CON_CUST_FLG = db.Column(db.String(255))
    OCCUP = db.Column(db.String(255))
    POSN = db.Column(db.String(255))
    TITL = db.Column(db.String(255))
    STOCK_CRD = db.Column(db.String(255))
    MAIN_TEL_NO = db.Column(db.String(255))
    MOBIL_NO = db.Column(db.String(255))
    REC_DAY = db.Column(db.String(255))
    CHG_DAY = db.Column(db.String(255))
    CUST_STS = db.Column(db.String(255))



# 关联关系表
class TBL_CUST_ID_CONV(db.Model):
    __tablename__ = "TBL_CUST_ID_CONV"
    ID = db.Column(db.Integer, primary_key=True)
    ECIF_CST_ID = db.Column(db.String(255))
    CUST_NO = db.Column(db.String(255))

    @staticmethod
    def selectAll():
        result = db.session.query(TBL_CUST_ID_CONV.ECIF_CST_ID).all()
        return result


# 电子渠道交易流水
class TRAD_FLOW(db.Model):
    __tablename__ = "TRAD_FLOW"
    ID = db.Column(db.Integer, primary_key=True)
    FLOW_NO = db.Column(db.String(255))
    CHANL_NO = db.Column(db.String(255))
    FLAT_TRAD_DATE = db.Column(db.String(255))
    FLAT_TRAD_TIME = db.Column(db.String(255))
    FLAT_SYS_DATE = db.Column(db.String(255))
    CHANL_DATE = db.Column(db.String(255))
    CHANL_FLOW_NO = db.Column(db.String(255))
    BACK_TRAD_DATE = db.Column(db.String(255))
    CUST_NO = db.Column(db.String(255))
    CHANL_CUST_NO = db.Column(db.String(255))
    CUST_TYP = db.Column(db.String(255))
    CUST_GRD = db.Column(db.String(255))
    ITCD_NO = db.Column(db.String(255))
    AMT1 = db.Column(db.String(255))
    AMT2 = db.Column(db.String(255))
    AMT3 = db.Column(db.String(255))
    SVC = db.Column(db.String(255))
    CURR = db.Column(db.String(255))
    ACCT_TYPE = db.Column(db.String(255))
    ACCT_NAME = db.Column(db.String(255))
    ASS_ACCT_TYPE = db.Column(db.String(255))
    TRAD_BRAN = db.Column(db.String(255))
    ACCT_BRAN = db.Column(db.String(255))
    ASS_ACCT_BRAN = db.Column(db.String(255))
    TOT_FLG = db.Column(db.String(255))
    TRAD_STS = db.Column(db.String(255))








