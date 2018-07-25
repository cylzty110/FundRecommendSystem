from  recommend import models, db
from sqlalchemy import and_


#存款产品持有信息
class DepositMessage:
    accountBalance = 0.0 #账户余额
    accountCurrent = 0.0 #账户活期存款余额
    accountRegular = 0.0 #账户定期存款余额
    accountAverage = 0.0 #账户存款月日均余额


    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.ADS_CUST_HOLD_DEPOSIT.query.filter_by(ECIF_CST_ID=id).all()
        for item in data:
            depositMessage = DepositMessage()
            depositMessage.accountBalance = item.ACBA
            depositMessage.accountCurrent = item.ACC_DMDDEP_BAL
            depositMessage.accountRegular = item.ACC_TMDEP_MO_DABAL
            depositMessage.accountAverage = item.ACC_DEP_MO_DABAL
            result.append(depositMessage)
        return result


#理财产品持有信息
class InvestMessage:
    categoryCode = 0 #投资理财产品类别码
    typeCode = 0 #投资理财产品类型码
    chmtpdMonthAcm = 0 #投资理财产品月积数
    chmtpdSeasonAcm = 0 #投资理财产品季积数
    chmtpdYearAcm = 0 #投资理财产品年积数
    monthAcmHpnLot = 0 #月累计发生份额
    monthAcmHpCnt = 0 #月累计发生次数
    monthAverageBal = 0 #月日均余额
    lastTmTxnDt = "" #最后一次交易日期



    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.ADS_CUST_HOLD_INVEST.query.filter_by(ECIF_CST_ID=id).all()
        for item in data:
            investMessage = InvestMessage()
            investMessage.category_code = item.IVS_CHMTPD_CGY_CD
            investMessage.type_code = item.IVS_CHMTPD_TP_CD
            investMessage.chmtpdMonthAcm = item.IVS_CHMTPD_MO_ACM
            investMessage.chmtpdSeasonAcm = item.IVS_CHMTPD_SSN_ACM
            investMessage.chmtpdYearAcm = item.IVS_CHMTPD_YR_ACM
            investMessage.monthAcmHpnLot = item.MO_ACM_HPN_LOT
            investMessage.monthAcmHpCnt = item.MO_ACM_HPCNT
            investMessage.monthAverageBal = item.MO_DABAL
            investMessage.lastTmTxnDt = item.LASTTM_TXN_DT

            result.append(investMessage)
        return result

#银行信息
class BankInfo:
    chmtPdBalance = 0 #我行理财产品余额
    fundBalance = 0 #基金余额
    monthFundNum = 0 #基金月日均数
    timePointAum = 0 #客户时点AUM值
    monthAverageAum = 0 #客户月均AUM值
    yearDailyAum = 0 #客户年日均AUM值
    fundFirstBuy = "" #基金首次购买时间
    fundRecentlyBuy = "" #最近一次购买基金时间

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.ADS_PERS_CUST_BANK_INFO.query.filter_by(CST_NO=id).all()
        for item in data:
            bankInfo = BankInfo()
            bankInfo.chmtPdBalance = item.CCB_CHMTPD_BAL
            bankInfo.fundBalance = item.FND_BAL
            bankInfo.monthFundNum = item.FND_MO_DA_NUM
            bankInfo.timePointAum = item.CST_TMPNTAUM_VAL
            bankInfo.monthAverageAum = item.CST_MOAVGAUM_VAL
            bankInfo.yearDailyAum = item.CST_YR_DAAUM_VAL
            bankInfo.fundFirstBuy = item.FND_FTM_PRCH_TM
            bankInfo.fundRecentlyBuy = item.RCTLY_OC_PRCH_FND_TM
            result.append(bankInfo)
        return result


class LoanInfo:
    pass


#电子渠道个人签约客户渠道信息
class ChannelInfo:
    settleFeeType = "" #结算费收费方式

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.PRIV_CHANL_INFO.query.\
            filter(and_(models.TBL_CUST_ID_CONV.ECIF_CST_ID==id,
                        models.PRIV_CHANL_INFO.CUST_NO==models.TBL_CUST_ID_CONV.CUST_NO)).all()
        for item in data:
            channelInfo = ChannelInfo()
            channelInfo.settleFeeType = item.STL_FEE_TYP
            result.append(channelInfo)
        return result


#电子渠道个人签约客户基本信息
class BasicMessage:
    workFlag = 0 #员工标志
    age = 0 #年龄
    income = 0 #月收入
    education = "" #学历
    custStatus = 0 #客户平台状态

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.PRIV_CUST_INFO.query.\
            filter(and_(models.PRIV_CUST_INFO.CUST_NO==models.TBL_CUST_ID_CONV.CUST_NO,
                        models.TBL_CUST_ID_CONV.ECIF_CST_ID==id)).all()
        for item in data:
            basicMessage = BasicMessage()
            basicMessage.workFlag = item.WORK_FLG
            basicMessage.age = item.BIRDAY
            basicMessage.income = item.MN_INCOM
            basicMessage.education = item.EDUC
            basicMessage.custStatus = item.CUST_STS
            result.append(basicMessage)
        return result



#基金交易成交信息
class FundInfo:
    txnAmount = 0.0  # 交易金额
    txnAccountNum = "" #基金交易账号
    customAccountNum = "" #客户基金账号
    txnLot = 0.0 #交易份额

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.FundFlow.query.filter(and_(models.FundFlow.SCR_TXN_ACCNO==
        models.FundUserRelation.SCR_TXN_ACCNO,models.FundUserRelation.CST_ID==id)).all()
        for item in data:
            fundInfo = FundInfo()
            fundInfo.txnAmount = item.CFM_TXNAMT
            fundInfo.txnAccountNum = item.SCR_TXN_ACCNO
            fundInfo.customAccountNum = item.CST_SCRTACNO
            fundInfo.txnLot = item.CFM_TXN_LOT
            result.append(fundInfo)
        return result


#电子渠道交易流水
class TradFlow:
    pass


class CustomMessage:
    ecifId = "" #ECIF客户编号
    depositMessage = [] #存款产品持有
    investMessage = [] #理财产品持有
    bankInfo = [] #银行信息
    channelInfo = [] #电子渠道个人签约客户渠道信息
    basicMessage = [] #电子渠道个人签约客户基本信息
    fundInfo = [] #基金交易成交信息

    def selectByEcifId(id):
        customMessage = CustomMessage()
        customMessage.ecifId = id
        customMessage.depositMessage = DepositMessage.selectByEcifId(id)
        customMessage.investMessage = InvestMessage.selectByEcifId(id)
        customMessage.bankInfo = BankInfo.selectByEcifId(id)
        customMessage.channelInfo = ChannelInfo.selectByEcifId(id)
        customMessage.basicMessage = BasicMessage.selectByEcifId(id)
        customMessage.fundInfo = FundInfo.selectByEcifId(id)
        return customMessage