from recommend import models, db
from sqlalchemy import and_


# 存款产品持有信息
class DepositMessage:
    def __init__(self):
        self.accountBalance = 0.0  # 账户余额
        self.accountCurrent = 0.0  # 账户活期存款余额
        self.accountRegular = 0.0  # 账户定期存款余额
        self.accountAverage = 0.0  # 账户存款月日均余额

    @staticmethod
    def selectByEcifId(id):
        result = DepositMessage()
        data = models.ADS_CUST_HOLD_DEPOSIT.query.filter_by(ECIF_CST_ID=id).all()
        for item in data:
            result.accountBalance = float(item.ACBA)
            result.accountCurrent = float(item.ACC_DMDDEP_BAL)
            result.accountRegular = float(item.ACC_TMDEP_MO_DABAL)
            result.accountAverage = float(item.ACC_DEP_MO_DABAL)
        return result


# 理财产品持有信息
class InvestMessage:
    def __init__(self):
        self.chmtpdMonthAcm = 0.0  # 投资理财产品月积数
        self.chmtpdSeasonAcm = 0.0  # 投资理财产品季积数
        self.chmtpdYearAcm = 0.0  # 投资理财产品年积数
        self.monthAcmHpnLot = 0.0  # 月累计发生份额
        self.monthAcmHpCnt = 0.0  # 月累计发生次数
        self.monthAverageBal = 0.0  # 月日均余额

    @staticmethod
    def selectByEcifId(id):
        result = InvestMessage()
        data = models.ADS_CUST_HOLD_INVEST\
            .query.filter(and_(models.ADS_CUST_HOLD_INVEST.ECIF_CST_ID == id,
                               models.ADS_CUST_HOLD_INVEST.IVS_CHMTPD_CGY_CD == '004')).all()
        for item in data:
            result.chmtpdMonthAcm += float(item.IVS_CHMTPD_MO_ACM)
            result.chmtpdSeasonAcm += float(item.IVS_CHMTPD_SSN_ACM)
            result.chmtpdYearAcm += float(item.IVS_CHMTPD_YR_ACM)
            result.monthAcmHpnLot += float(item.MO_ACM_HPN_LOT)
            result.monthAcmHpCnt += float(item.MO_ACM_HPCNT)
            result.monthAverageBal += float(item.MO_DABAL)
        return result


# 银行信息
class BankInfo:
    def __init__(self):
        self.fundBalance = 0.0  # 基金余额
        self.monthFundNum = 0.0  # 基金月日均数
        self.timePointAum = 0.0  # 客户时点AUM值
        self.monthAverageAum = 0.0  # 客户月均AUM值
        self.yearDailyAum = 0.0  # 客户年日均AUM值

    @staticmethod
    def selectByEcifId(id):
        result = BankInfo()
        data = models.ADS_PERS_CUST_BANK_INFO.query.filter_by(CST_NO=id).all()
        for item in data:
            result.fundBalance = float(item.FND_BAL)
            result.monthFundNum = float(item.FND_MO_DA_NUM)
            result.timePointAum = float(item.CST_TMPNTAUM_VAL)
            result.monthAverageAum = float(item.CST_MOAVGAUM_VAL)
            result.yearDailyAum = float(item.CST_YR_DAAUM_VAL)
        return result


# 电子渠道个人签约客户基本信息
class BasicMessage:
    def __init__(self):
        self.age = 0  # 年龄
        self.income = 0  # 月收入
        self.education = "empty"  # 学历
        self.custStatus = 0  # 客户平台状态

    @staticmethod
    def selectByEcifId(id):
        result = BasicMessage()
        data = models.PRIV_CUST_INFO.query.\
            filter(and_(models.PRIV_CUST_INFO.CUST_NO == models.TBL_CUST_ID_CONV.CUST_NO,
                        models.TBL_CUST_ID_CONV.ECIF_CUST_NO == id)).all()
        for item in data:
            if item.BIRDAY:
                result.age = int(2018 - int(item.BIRDAY)/10000)
            result.income = int(item.MN_INCOM)
            result.education = item.EDUC
            if item.CUST_STS:
                result.custStatus = int(item.CUST_STS)
        return result


# 基金交易成交信息
class FundInfo:
    def __init__(self):
        self.txnAmount = 0.0   # 交易金额

    @staticmethod
    def selectByEcifId(id):
        result = FundInfo()
        data = models.FundFlow.query.filter(and_(models.FundFlow.SCR_TXN_ACCNO ==
        models.FundUserRelation.SCR_TXN_ACCNO, models.FundUserRelation.CST_ID == id)).all()
        for item in data:
            result.txnAmount += float(item.CFM_TXNAMT)
        return result


class CustomMessage:
    def __init__(self):
        self.ecifId = 0  # ECIF客户编号
        self.depositMessage = DepositMessage()   # 存款产品持有
        self.investMessage = InvestMessage()  # 理财产品持有
        self.bankInfo = BankInfo()  # 银行信息
        self.basicMessage = BasicMessage()  # 电子渠道个人签约客户基本信息
        self.fundInfo = FundInfo()  # 基金交易成交信息

    def selectByEcifId(id):
        customMessage = CustomMessage()
        customMessage.ecifId = id
        customMessage.depositMessage = DepositMessage.selectByEcifId(id)
        customMessage.investMessage = InvestMessage.selectByEcifId(id)
        customMessage.bankInfo = BankInfo.selectByEcifId(id)
        customMessage.basicMessage = BasicMessage.selectByEcifId(id)
        customMessage.fundInfo = FundInfo.selectByEcifId(id)
        return customMessage