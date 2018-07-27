from recommend import models, db
from sqlalchemy import and_


# 存款产品持有信息
class DepositMessage:
    accountBalance = None  # 账户余额
    accountCurrent = None  # 账户活期存款余额
    accountRegular = None  # 账户定期存款余额
    accountAverage = None  # 账户存款月日均余额

    def __init__(self):
        self.accountBalance = 0.0
        self.accountCurrent = 0.0
        self.accountRegular = 0.0
        self.accountAverage = 0.0

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
    typeCode = None  # 投资理财产品类型码
    chmtpdMonthAcm = None  # 投资理财产品月积数
    chmtpdSeasonAcm = None  # 投资理财产品季积数
    chmtpdYearAcm = None  # 投资理财产品年积数
    monthAcmHpnLot = None  # 月累计发生份额
    monthAcmHpCnt = None  # 月累计发生次数
    monthAverageBal = None  # 月日均余额

    def __init__(self):
        self.typeCode = "empty"
        self.chmtpdMonthAcm = 0.0
        self.chmtpdSeasonAcm = 0.0
        self.chmtpdYearAcm = 0.0
        self.monthAcmHpnLot = 0.0
        self.monthAcmHpCnt = 0.0
        self.monthAverageBal = 0.0

    @staticmethod
    def selectByEcifId(id):
        result = InvestMessage()
        data = models.ADS_CUST_HOLD_INVEST.query.filter(and_(models.ADS_CUST_HOLD_INVEST.
        ECIF_CST_ID == id, models.ADS_CUST_HOLD_INVEST.IVS_CHMTPD_CGY_CD == '004')).all()
        for item in data:
            result.typeCode = item.IVS_CHMTPD_TP_CD
            result.chmtpdMonthAcm += float(item.IVS_CHMTPD_MO_ACM)
            result.chmtpdSeasonAcm += float(item.IVS_CHMTPD_SSN_ACM)
            result.chmtpdYearAcm += float(item.IVS_CHMTPD_YR_ACM)
            result.monthAcmHpnLot += float(item.MO_ACM_HPN_LOT)
            result.monthAcmHpCnt += float(item.MO_ACM_HPCNT)
            result.monthAverageBal += float(item.MO_DABAL)
        return result

# 银行信息
class BankInfo:
    # chmtPdBalance = None  # 我行理财产品余额
    fundBalance = None  # 基金余额
    monthFundNum = None  # 基金月日均数
    timePointAum = None  # 客户时点AUM值
    monthAverageAum = None  # 客户月均AUM值
    yearDailyAum = None  # 客户年日均AUM值

    def __init__(self):
        # self.chmtPdBalance = 0.0
        self.fundBalance = 0.0
        self.monthFundNum = 0.0
        self.timePointAum = 0.0
        self.monthAverageAum = 0.0
        self.yearDailyAum = 0.0

    @staticmethod
    def selectByEcifId(id):
        result = BankInfo()
        data = models.ADS_PERS_CUST_BANK_INFO.query.filter_by(CST_NO=id).all()
        for item in data:
            # result.chmtPdBalance = float(item.CCB_CHMTPD_BAL)
            result.fundBalance = float(item.FND_BAL)
            result.monthFundNum = float(item.FND_MO_DA_NUM)
            result.timePointAum = float(item.CST_TMPNTAUM_VAL)
            result.monthAverageAum = float(item.CST_MOAVGAUM_VAL)
            result.yearDailyAum = float(item.CST_YR_DAAUM_VAL)
        return result


class LoanInfo:
    pass

"""
# 电子渠道个人签约客户渠道信息
class ChannelInfo:
    settleFeeType = None  # 结算费收费方式

    def __init__(self):
        self.settleFeeType = "empty"

    @staticmethod
    def selectByEcifId(id):
        result = ChannelInfo()
        data = models.PRIV_CHANL_INFO.query.\
            filter(and_(models.TBL_CUST_ID_CONV.ECIF_CST_ID == id,
                        models.PRIV_CHANL_INFO.CUST_NO == models.TBL_CUST_ID_CONV.CUST_NO)).all()
        for item in data:
            result.settleFeeType = item.STL_FEE_TYP
        return result
"""

# 电子渠道个人签约客户基本信息
class BasicMessage:
    age = None  # 年龄
    income = None  # 月收入
    education = None  # 学历
    custStatus = None  # 客户平台状态

    def __init__(self):
        self.age = 0
        self.income = 0
        self.education = "empty"
        self.custStatus = 0

    @staticmethod
    def selectByEcifId(id):
        result = BasicMessage()
        data = models.PRIV_CUST_INFO.query.\
            filter(and_(models.PRIV_CUST_INFO.CUST_NO == models.TBL_CUST_ID_CONV.CUST_NO,
                        models.TBL_CUST_ID_CONV.ECIF_CST_ID == id)).all()
        for item in data:
            if item.BIRDAY is not None:
                result.age = int(2018 - int(item.BIRDAY)/10000)
            result.income = int(item.MN_INCOM)
            result.education = item.EDUC
            if item.CUST_STS is not None:
                result.custStatus = int(item.CUST_STS)
        return result


# 基金交易成交信息
class FundInfo:
    txnAmount = None   # 交易金额

    def __init__(self):
        self.txnAmount = 0.0

    @staticmethod
    def selectByEcifId(id):
        result = FundInfo()
        data = models.FundFlow.query.filter(and_(models.FundFlow.SCR_TXN_ACCNO ==
        models.FundUserRelation.SCR_TXN_ACCNO, models.FundUserRelation.CST_ID == id)).all()
        for item in data:
            result.txnAmount += float(item.CFM_TXNAMT)
        return result


# 电子渠道交易流水
class TradFlow:
    pass


class CustomMessage:
    ecifId = None  # ECIF客户编号
    depositMessage = None   # 存款产品持有
    investMessage = None  # 理财产品持有
    bankInfo = None  # 银行信息
    # channelInfo = None  # 电子渠道个人签约客户渠道信息
    basicMessage = None  # 电子渠道个人签约客户基本信息
    fundInfo = None  # 基金交易成交信息

    def __init__(self):
        self.ecifId = 0
        self.depositMessage = DepositMessage()
        self.investMessage = InvestMessage()
        self.bankInfo = BankInfo()
        # self.channelInfo = ChannelInfo()
        self.basicMessage = BasicMessage()
        self.fundInfo = FundInfo()

    def selectByEcifId(id):
        customMessage = CustomMessage()
        customMessage.ecifId = id
        customMessage.depositMessage = DepositMessage.selectByEcifId(id)
        customMessage.investMessage = InvestMessage.selectByEcifId(id)
        customMessage.bankInfo = BankInfo.selectByEcifId(id)
        # customMessage.channelInfo = ChannelInfo.selectByEcifId(id)
        customMessage.basicMessage = BasicMessage.selectByEcifId(id)
        customMessage.fundInfo = FundInfo.selectByEcifId(id)
        return customMessage