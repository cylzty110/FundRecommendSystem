from recommend import db
import flask_sqlalchemy


# 基金交易账户表
class FundUserRelation(db.Model):
    __tablename__ = "SCR_TNAC"
    ID = db.Column(db.Integer, primary_key=True)
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
        result = db.session.query(FundUserRelation.CST_ID, FundFlow.SCR_PD_ECD).\
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

    # 批量插入
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
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


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
    OPNACC_SIGN_DT = db.Column(db.String(255))
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


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
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


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
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


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
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


# 电子渠道个人签约客户基本信息
class PRIV_CUST_INFO(db.Model):
    __tablename__ = "PRIV_CUST_INFO"
    CUST_NO = db.Column(db.String(255), primary_key=True)
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
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


# 关联关系表
class TBL_CUST_ID_CONV(db.Model):
    __tablename__ = "TBL_CUST_ID_CONV"
    ID = db.Column(db.Integer, primary_key=True)
    ECIF_CUST_NO = db.Column(db.String(255))
    CUST_NO = db.Column(db.String(255))
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))

    @staticmethod
    def selectAll():
        result = db.session.query(TBL_CUST_ID_CONV.ECIF_CUST_NO).all()
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
    UPLOAD_TIME = db.Column(db.String(255))
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


class CST_FCS_FND(db.Model):
    __tablename__ = 'CST_FCS_FND'
    ID = db.Column(db.Integer, primary_key=True)
    CST_ID = db.Column(db.String(255))  # 客户编号
    SCR_TXN_MKT_ID = db.Column(db.String(255))  # 证券交易市场编号
    SCR_PD_ECD = db.Column(db.String(255))  # 证券产品编码
    ASTPRTFL_CL_ID = db.Column(db.String(255))  # 资产组合分类编号
    PD_PRTFL_CFG_NM = db.Column(db.String(255))  # 产品组合配置名称
    SCR_IVS_PCT = db.Column(db.String(255))  # 证券投资占比
    PRMT_IND = db.Column(db.String(255))  # 允许标志
    FCS_DT = db.Column(db.String(255))  # 关注日期
    CMBSOP_SRCCD = db.Column(db.String(255))  # 营销商机来源代码
    CST_RSK_TLRNC_CPY_CD = db.Column(db.String(255))  # 客户风险承受能力代码
    FTR_RNG_DSC = db.Column(db.String(255))  # 特征区间描述
    MULTI_TENANCY_ID = db.Column(db.String(255))  # 多实体标识
    MDF_BR_ID = db.Column(db.String(255))  # 变更分行编号
    SCR_MDF_INSID = db.Column(db.String(255))  # 证券变更机构编号
    MDF_TRID = db.Column(db.String(255))  # 变更柜员编号
    CRT_BR_ID = db.Column(db.String(255))  # 创建分行编号
    SCR_CRT_INSID = db.Column(db.String(255))  # 证券创建机构编号
    SCR_CRT_TRID = db.Column(db.String(255))  # 证券创建柜员编号
    DATA_RCRD_CRT_DT = db.Column(db.String(255))  # 数据记录创建日期
    RCRD_CRT_TM = db.Column(db.String(255))  # 记录创建时间
    STMD_DT = db.Column(db.String(255))  # 状态变更日期
    RCRD_UDT_TM = db.Column(db.String(255))  # 记录更新时间
    DATA_UDT_DT_TM = db.Column(db.String(255))  # 数据更新日期时间
    CUR_VLD_IND = db.Column(db.String(255))  # 当前有效标志
    STRUSIND = db.Column(db.String(255))  # 启用标志
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


class CST_FND_PFT_INFO(db.Model):
    __tablename__ = 'CST_FND_PFT_INFO'
    ID = db.Column(db.Integer, primary_key=True)
    SCR_SVAR_ID = db.Column(db.String(255))  # 证券服务合约编号
    CST_SCRTACNO = db.Column(db.String(255))  # 客户证券账号
    SCR_TXN_ACCNO = db.Column(db.String(255))  # 证券交易账号
    SCR_TXN_MKT_ID = db.Column(db.String(255))  # 证券交易市场编号
    SCR_PD_ECD = db.Column(db.String(255))  # 证券产品编码
    FNDCO_AGNC_SALE_INSID = db.Column(db.String(255))  # 基金公司代理销售机构编号
    FND_CO_DVDN_MTDCD = db.Column(db.String(255))  # 基金公司分红方式代码
    CRFD_IDNWAD_PFT_AMT = db.Column(db.String(255))  # 货币基金当日新增收益金额
    CRFDNOT_CRROV_PFT_AMT = db.Column(db.String(255))  # 货币基金未结转收益金额
    CST_FND_RDMPTN_TXNAMT = db.Column(db.String(255))  # 客户基金赎回交易金额
    CSTFNDACMRDMPTNTXNAMT = db.Column(db.String(255))  # 客户基金累计赎回交易金额
    RCTLY_UDT_DT = db.Column(db.String(255))  # 最近更新日期
    AMT_1 = db.Column(db.String(255))  # 金额一
    AMT_2 = db.Column(db.String(255))  # 金额二
    CSTFDNTDT_PRCH_TXNAMT = db.Column(db.String(255))  # 客户基金国债购买交易金额
    CSTFDNTDTAMPRCHTXNAMT = db.Column(db.String(255))  # 客户基金国债累计购买交易金额
    CST_CRFD_PFT_AMT = db.Column(db.String(255))  # 客户货币基金收益金额
    AMT_3 = db.Column(db.String(255))  # 金额三
    MULTI_TENANCY_ID = db.Column(db.String(255))  # 多实体标识
    DATA_RCRD_CRT_DT = db.Column(db.String(255))  # 数据记录创建日期
    RCRD_CRT_TM = db.Column(db.String(255))  # 记录创建时间
    STMD_DT = db.Column(db.String(255))  # 状态变更日期
    RCRD_UDT_TM = db.Column(db.String(255))  # 记录更新时间
    DATA_UDT_DT_TM = db.Column(db.String(255))  # 数据更新日期时间
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


class FND_AUTO_TXN_ITT_DTL(db.Model):
    __tablename__ = 'FND_AUTO_TXN_ITT_DTL'
    ID = db.Column(db.Integer, primary_key=True)
    SN = db.Column(db.String(255))  # 序号
    APLY_ID = db.Column(db.String(255))  # 申请编号
    INTLG_TXN_SVAR_ID = db.Column(db.String(255))  # 智能交易服务合约编号
    SYS_TX_CODE = db.Column(db.String(255))  # 交易服务编码
    INTLG_TXN_TPCD = db.Column(db.String(255))  # 智能交易类型代码
    SCR_TXN_MKT_ID = db.Column(db.String(255))  # 证券交易市场编号
    SCR_PD_ECD = db.Column(db.String(255))  # 证券产品编码
    CST_SCRTACNO = db.Column(db.String(255))  # 客户证券账号
    SCR_TXN_ACCNO = db.Column(db.String(255))  # 证券交易账号
    TFR_SIGN_ACCNO = db.Column(db.String(255))  # 转账签约账号
    SCR_CUR_LOT = db.Column(db.String(255))  # 证券当前份额
    SIGN_ITT_AMT = db.Column(db.String(255))  # 签约发起金额
    AUTOSBRBRDMPTNMNM_AMT = db.Column(db.String(255))  # 自动申购赎回保底金额
    PLN_ITT_DT = db.Column(db.String(255))  # 计划发起日期
    ACT_ITT_DT = db.Column(db.String(255))  # 实际发起日期
    ACT_ITT_TM = db.Column(db.String(255))  # 实际发起时间
    SCR_ACT_TXNAMT = db.Column(db.String(255))  # 证券实际交易金额
    ACT_TXN_LOT = db.Column(db.String(255))  # 实际交易份额
    AUTOSBRBRDMPTNCCURBAL = db.Column(db.String(255))  # 自动申购赎回客户当前余额
    AUTOSBRBRDMPTNCTBALDT = db.Column(db.String(255))  # 自动申购赎回客户余额日期
    SCR_PCSG_STCD = db.Column(db.String(255))  # 证券处理状态代码
    PSRLT_DSC = db.Column(db.String(255))  # 处理结果描述
    MULTI_TENANCY_ID = db.Column(db.String(255))  # 多实体标识
    DATA_RCRD_CRT_DT = db.Column(db.String(255))  # 数据记录创建日期
    RCRD_CRT_TM = db.Column(db.String(255))  # 记录创建时间
    STMD_DT = db.Column(db.String(255))  # 状态变更日期
    RCRD_UDT_TM = db.Column(db.String(255))  # 记录更新时间
    DATA_UDT_DT_TM = db.Column(db.String(255))  # 数据更新日期时间
    LCL_YRMO_DAY = db.Column(db.String(255))  # 本地年月日
    LCL_HR_GRD_SCND = db.Column(db.String(255))  # 本地时分秒
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


class FND_BSC_INF(db.Model):
    __tablename__ = 'FND_BSC_INF'
    ID = db.Column(db.Integer, primary_key=True)
    SCR_PD_ECD = db.Column(db.String(255))  # 证券产品编码
    SCR_TXN_MKT_ID = db.Column(db.String(255))  # 证券交易市场编号
    FND_NM = db.Column(db.String(255))  # 基金名称
    FND_SHRTNM = db.Column(db.String(255))  # 基金简称
    PD_SL_OBJ_CD = db.Column(db.String(255))  # 产品发售对象代码
    GLX_FND_PD_ECD = db.Column(db.String(255))  # 银河基金产品编码
    SCR_ADMN_ID = db.Column(db.String(255))  # 证券管理人编号
    SCR_TS_PSN_ID = db.Column(db.String(255))  # 证券托管人编号
    FND_DNMN = db.Column(db.String(255))  # 基金面值
    FND_ISSU_PRC = db.Column(db.String(255))  # 基金发行价格
    FND_FTR_DSC = db.Column(db.String(255))  # 基金特征描述
    FNDFTMSALESVCFEE_RATE = db.Column(db.String(255))  # 基金首次销售服务费率
    FNDSALESVCFEEYR_FEERT = db.Column(db.String(255))  # 基金销售服务费年费率
    FND_PD_TPCD = db.Column(db.String(255))  # 基金产品类型代码
    GLX_FND_LVL1_CL_ECD = db.Column(db.String(255))  # 银河基金一级分类编码
    GLX_FND_LVL1_CL_NM = db.Column(db.String(255))  # 银河基金一级分类名称
    GLX_FND_LVL2_CL_ECD = db.Column(db.String(255))  # 银河基金二级分类编码
    GLX_FND_LVL2_CL_NM = db.Column(db.String(255))  # 银河基金二级分类名称
    RSK_GRD_CD = db.Column(db.String(255))  # 风险等级代码
    FND_RSK_GRD_EVAL = db.Column(db.String(255))  # 基金风险等级评价值
    EXT_FND_STCD = db.Column(db.String(255))  # 外部基金状态代码
    FND_CO_DVDN_MTDCD = db.Column(db.String(255))  # 基金公司分红方式代码
    PRMT_DVDN_MOD_DSC = db.Column(db.String(255))  # 允许分红方式描述
    RDMPTN_FNDS_CLRG_DYS = db.Column(db.String(255))  # 赎回资金清算天数
    DVDN_FNDS_CLRG_DYS = db.Column(db.String(255))  # 分红资金清算天数
    FND_IVS_DRC_CD = db.Column(db.String(255))  # 基金投资方向代码
    PARM_LCL_WEBST = db.Column(db.String(255))  # 参数本地网址
    NTW_ADR_CNTNT = db.Column(db.String(255))  # 网络地址内容
    CTR_NM = db.Column(db.String(255))  # 合同名称
    MCCY_IND = db.Column(db.String(255))  # 多币种标志
    CCYCD = db.Column(db.String(255))  # 币种代码
    CSHEX_CD = db.Column(db.String(255))  # 钞汇代码
    FND_ESTB_DT = db.Column(db.String(255))  # 基金成立日期
    SCR_EFDT = db.Column(db.String(255))  # 证券生效日期
    STRUSIND = db.Column(db.String(255))  # 启用标志
    AHN_TRID = db.Column(db.String(255))  # 授权柜员编号
    TXN_ITT_CHNL_CGY_CODE = db.Column(db.String(255))  # 交易发起渠道类别
    MULTI_TENANCY_ID = db.Column(db.String(255))  # 多实体标识
    MDF_BR_ID = db.Column(db.String(255))  # 变更分行编号
    SCR_MDF_INSID = db.Column(db.String(255))  # 证券变更机构编号
    MDF_TRID = db.Column(db.String(255))  # 变更柜员编号
    CRT_BR_ID = db.Column(db.String(255))  # 创建分行编号
    SCR_CRT_INSID = db.Column(db.String(255))  # 证券创建机构编号
    SCR_CRT_TRID = db.Column(db.String(255))  # 证券创建柜员编号
    DATA_RCRD_CRT_DT = db.Column(db.String(255))  # 数据记录创建日期
    RCRD_CRT_TM = db.Column(db.String(255))  # 记录创建时间
    STMD_DT = db.Column(db.String(255))  # 状态变更日期
    RCRD_UDT_TM = db.Column(db.String(255))  # 记录更新时间
    DATA_UDT_DT_TM = db.Column(db.String(255))  # 数据更新日期时间
    FEERTELMTSCOPUPLM_VAL = db.Column(db.String(255))  # 费率要素范围上限值
    PD_TRM = db.Column(db.String(255))  # 产品期限
    EXDAT = db.Column(db.String(255))  # 到期日期
    FND_PERFCMPRBSS_AMT = db.Column(db.String(255))  # 基金业绩比较基准金额
    CSDC_FND_RSK_GRD_CD = db.Column(db.String(255))  # 中登基金风险等级代码
    MSG_LINKS_SKP_ADR = db.Column(db.String(255))  # 消息链接跳转地址
    AD_LINKS_ADR_CNTNT = db.Column(db.String(255))  # 广告链接地址内容
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


class FND_FTR_ATTR(db.Model):
    __tablename__ = 'FND_FTR_ATTR'
    ID = db.Column(db.Integer, primary_key=True)
    SCR_TXN_MKT_ID = db.Column(db.String(255))  # 证券交易市场编号
    SCR_PD_ECD = db.Column(db.String(255))  # 证券产品编码
    DSPL_SEQ_SN = db.Column(db.String(255))  # 显示排序序号
    LBL_ID = db.Column(db.String(255))  # 标签编号
    AHN_TRID = db.Column(db.String(255))  # 授权柜员编号
    TXN_ITT_CHNL_CGY_CODE = db.Column(db.String(255))  # 交易发起渠道类别
    MULTI_TENANCY_ID = db.Column(db.String(255))  # 多实体标识
    MDF_BR_ID = db.Column(db.String(255))  # 变更分行编号
    SCR_MDF_INSID = db.Column(db.String(255))  # 证券变更机构编号
    MDF_TRID = db.Column(db.String(255))  # 变更柜员编号
    CRT_BR_ID = db.Column(db.String(255))  # 创建分行编号
    SCR_CRT_INSID = db.Column(db.String(255))  # 证券创建机构编号
    SCR_CRT_TRID = db.Column(db.String(255))  # 证券创建柜员编号
    DATA_RCRD_CRT_DT = db.Column(db.String(255))  # 数据记录创建日期
    RCRD_CRT_TM = db.Column(db.String(255))  # 记录创建时间
    STMD_DT = db.Column(db.String(255))  # 状态变更日期
    RCRD_UDT_TM = db.Column(db.String(255))  # 记录更新时间
    DATA_UDT_DT_TM = db.Column(db.String(255))  # 数据更新日期时间
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


class FND_INTLG_TXN_STRTG(db.Model):
    __tablename__ = 'FND_INTLG_TXN_STRTG'
    ID = db.Column(db.Integer, primary_key=True)
    INTLG_TXN_SVAR_ID = db.Column(db.String(255))  # 智能交易服务合约编号
    INTLG_TXN_TPCD = db.Column(db.String(255))  # 智能交易类型代码
    SCR_TXN_MKT_ID = db.Column(db.String(255))  # 证券交易市场编号
    SCR_PD_ECD = db.Column(db.String(255))  # 证券产品编码
    TRCK_IDXN_CD = db.Column(db.String(255))  # 追踪指数代码
    CND_CMPR_OPRT_CD = db.Column(db.String(255))  # 条件比较操作符代码
    TXN_REF_VAL_DSC = db.Column(db.String(255))  # 交易参照值描述
    IVS_INCRORDEC_TPCD = db.Column(db.String(255))  # 投资增减类型代码
    IVS_INCRORDEC_PCT = db.Column(db.String(255))  # 投资增减比例
    STRTG_VLD_IND = db.Column(db.String(255))  # 策略有效标志
    MULTI_TENANCY_ID = db.Column(db.String(255))  # 多实体标识
    MDF_BR_ID = db.Column(db.String(255))  # 变更分行编号
    SCR_MDF_INSID = db.Column(db.String(255))  # 证券变更机构编号
    MDF_TRID = db.Column(db.String(255))  # 变更柜员编号
    CRT_BR_ID = db.Column(db.String(255))  # 创建分行编号
    SCR_CRT_INSID = db.Column(db.String(255))  # 证券创建机构编号
    SCR_CRT_TRID = db.Column(db.String(255))  # 证券创建柜员编号
    DATA_RCRD_CRT_DT = db.Column(db.String(255))  # 数据记录创建日期
    RCRD_CRT_TM = db.Column(db.String(255))  # 记录创建时间
    STMD_DT = db.Column(db.String(255))  # 状态变更日期
    RCRD_UDT_TM = db.Column(db.String(255))  # 记录更新时间
    DATA_UDT_DT_TM = db.Column(db.String(255))  # 数据更新日期时间
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


class FND_PD_DVDN_INF(db.Model):
    __tablename__ = 'FND_PD_DVDN_INF'
    ID = db.Column(db.Integer, primary_key=True)
    SCR_TXN_MKT_ID = db.Column(db.String(255))  # 证券交易市场编号
    SCR_PD_ECD = db.Column(db.String(255))  # 证券产品编码
    DVDN_RGDT = db.Column(db.String(255))  # 分红登记日期
    EXDVDY = db.Column(db.String(255))  # 除权日
    DSTR_DT = db.Column(db.String(255))  # 发放日期
    DVDN_UNIT = db.Column(db.String(255))  # 分红单位
    UNIT_FND_DVDN_AMT = db.Column(db.String(255))  # 单位基金分红金额
    THS_FND_UNIT_DVDN_AMT = db.Column(db.String(255))  # 本次基金单位分红金额
    YR_ACAMT = db.Column(db.String(255))  # 年累计金额
    DVDN_DT = db.Column(db.String(255))  # 分红日期
    CCYCD = db.Column(db.String(255))  # 币种代码
    CSHEX_CD = db.Column(db.String(255))  # 钞汇代码
    TXN_ITT_CHNL_CGY_CODE = db.Column(db.String(255))  # 交易发起渠道类别
    MULTI_TENANCY_ID = db.Column(db.String(255))  # 多实体标识
    DATA_RCRD_CRT_DT = db.Column(db.String(255))  # 数据记录创建日期
    RCRD_CRT_TM = db.Column(db.String(255))  # 记录创建时间
    STMD_DT = db.Column(db.String(255))  # 状态变更日期
    RCRD_UDT_TM = db.Column(db.String(255))  # 记录更新时间
    DATA_UDT_DT_TM = db.Column(db.String(255))  # 数据更新日期时间
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))


class FND_TFROFCSTD_INF(db.Model):
    __tablename__ = 'FND_TFROFCSTD_INF'
    ID = db.Column(db.Integer, primary_key=True)
    SCR_TXN_STS_ID = db.Column(db.String(255))  # 证券交易席位编号
    SCR_TXN_STS_NM = db.Column(db.String(255))  # 证券交易席位名称
    CRSSTM_IND = db.Column(db.String(255))  # 跨系统标志
    CRSMKT_TFRIN_PRMT_IND = db.Column(db.String(255))  # 跨市场转入允许标志
    SCR_TXN_MKT_ID = db.Column(db.String(255))  # 证券交易市场编号
    MULTI_TENANCY_ID = db.Column(db.String(255))  # 多实体标识
    DATA_RCRD_CRT_DT = db.Column(db.String(255))  # 数据记录创建日期
    RCRD_CRT_TM = db.Column(db.String(255))  # 记录创建时间
    STMD_DT = db.Column(db.String(255))  # 状态变更日期
    RCRD_UDT_TM = db.Column(db.String(255))  # 记录更新时间
    IMPR_DT = db.Column(db.String(255))  # 导入日期
    DATA_UDT_DT_TM = db.Column(db.String(255))  # 数据更新日期时间
    UPLOAD_USER = db.Column(db.String(255))
    UPLOAD_BATCH = db.Column(db.String(255))











