from  recommend import models, db
from sqlalchemy import and_


#存款产品持有信息
class DepositMessage:
    accont_balance = 0.0 #账户余额

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.ADS_CUST_HOLD_DEPOSIT.query.filter_by(ECIF_CST_ID=id).all()
        for item in data:
            depositMessage = DepositMessage()
            depositMessage.accont_balance = item.ACBA
            result.append(depositMessage)
        return result


#理财产品持有信息
class InvestMessage:
    category_code = 0 #投资理财产品类别码
    category_describe = "" #投资理财产品类别描述
    type_code = 0 #投资理财产品类型码
    type_describe = ""  # 投资理财产品类型描述
    account_num = 0 #投资理财产品账户数
    last_trade_date = "" #最后一次交易日期

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.ADS_CUST_HOLD_INVEST.query.filter_by(ECIF_CST_ID=id).all()
        for item in data:
            investMessage = InvestMessage()
            investMessage.category_code = item.IVS_CHMTPD_CGY_CD
            investMessage.category_describe = item.IVS_CHMTPD_CGY_DSC
            investMessage.type_code = item.IVS_CHMTPD_TP_CD
            investMessage.type_describe = item.IVS_CHMTPD_TPDS
            investMessage.account_num = item.IVS_CHMTPD_ACC_NUM
            investMessage.last_trade_date = item.LASTTM_TXN_DT
            result.append(investMessage)
        return result

#银行信息
class BankInfo:
    fund_first_date = "" #基金首次购买时间
    fund_recently_date = "" #最近一次购买基金时间
    fund_balance = 0 #基金余额
    bond_balance = 0 #债券余额
    insurance_balance = 0 #保险金额
    pm_balance = 0 #贵金属余额
    loan_balance = 0 #个贷余额
    time_aum = 0 #客户时点AUM值
    monthly_aum = 0 #客户月均AUM值
    year_daily_aum = 0 #客户年日均AUM值

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.ADS_PERS_CUST_BANK_INFO.query.filter_by(CST_NO=id).all()
        for item in data:
            bankInfo = BankInfo()
            bankInfo.fund_first_date = item.FND_FTM_PRCH_TM
            bankInfo.fund_recently_date = item.RCTLY_OC_PRCH_FND_TM
            bankInfo.fund_balance = item.FND_BAL
            bankInfo.bond_balance = item.BOND_BAL
            bankInfo.insurance_balance = item.INS_AMT
            bankInfo.pm_balance = item.PM_BAL
            bankInfo.loan_balance = item.PSNLOAN_BAL
            bankInfo.time_aum = item.CST_TMPNTAUM_VAL
            bankInfo.monthly_aum = item.CST_MOAVGAUM_VAL
            bankInfo.year_daily_aum = item.CST_YR_DAAUM_VAL
            result.append(bankInfo)
        return result

#个贷产品持有信息
class LoanMessage:
    account_num = 0 #账户数
    type_code = "" #贷款类型代码
    type_describe = "" #贷款类型描述
    normal_principal_balance = 0.0 #正常本金余额
    overdue_principal_balance = 0.0 #逾期本金余额

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.ADS_PERS_LOAN_PROD_HOLD_INFO.query.filter_by(ECIF_CST_NO=id).all()
        for item in data:
            loanMessage = LoanMessage()
            loanMessage.account_num = item.ACC_NUM
            loanMessage.type_code = item.LN_TPCD
            loanMessage.type_describe = item.LN_TPDS
            loanMessage.normal_principal_balance = item.RGLR_PNP_BAL
            loanMessage.overdue_principal_balance = item.ODUE_PNP_BAL
            result.append(loanMessage)
        return result

#电子渠道个人签约客户渠道信息
class ChannelInfo:
    contribute_level = "" #客户贡献级别

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.PRIV_CHANL_INFO.query.\
            filter(and_(models.TBL_CUST_ID_CONV.ECIF_CST_ID==id,
                        models.PRIV_CHANL_INFO.CUST_NO==models.TBL_CUST_ID_CONV.CUST_NO)).all()
        for item in data:
            channelInfo = ChannelInfo()
            channelInfo.contribute_level = item.CONTRIBUTION_LEVEL
            result.append(channelInfo)
        return result


#电子渠道个人签约客户基本信息
class BasicMessage:
    sex = "" #性别
    age = 0 #年龄
    income = 0 #月收入
    occupy = "" #职业
    post = "" #职务
    title = "" #职称
    education = "" #学历

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.PRIV_CUST_INFO.query.\
            filter(and_(models.PRIV_CUST_INFO.CUST_NO==models.TBL_CUST_ID_CONV.CUST_NO,
                        models.TBL_CUST_ID_CONV.ECIF_CST_ID==id)).all()
        for item in data:
            basicMessage = BasicMessage()
            basicMessage.sex = item.SEX
            basicMessage.age = item.BIRDAY
            basicMessage.income = item.MN_INCOM
            basicMessage.occupy = item.OCCUP
            basicMessage.post = item.POSN
            basicMessage.title = item.TITL
            basicMessage.education = item.EDUC
            result.append(basicMessage)
        return result



#基金交易成交信息
class FundInfo:
    account_num = "" #基金交易账号
    trade_amount = 0.0 #交易金额
    trade_lot = 0 #交易份额

    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.FundFlow.query.filter(and_(models.FundFlow.SCR_TXN_ACCNO==
        models.FundUserRelation.SCR_TXN_ACCNO,models.FundUserRelation.CST_ID==id)).all()
        for item in data:
            fundInfo = FundInfo()
            fundInfo.account_num = item.SCR_TXN_ACCNO
            fundInfo.trade_amount = item.CFM_TXNAMT
            fundInfo.trade_lot = item.CFM_TXN_LOT
            result.append(fundInfo)
        return result


#电子渠道交易流水
class TradFlow:
    atm1 = 0.0 #amt1交易金额
    atm2 = 0.0 #amt2交易金额
    atm3 = 0.0 #amt3交易金额
    svc = 0.0 #手续费
    curr = "" #币种
    @staticmethod
    def selectByEcifId(id):
        result = []
        data = models.TRAD_FLOW.query.filter(and_(models.TRAD_FLOW.CUST_NO==
        models.TBL_CUST_ID_CONV.CUST_NO,models.TBL_CUST_ID_CONV.ECIF_CST_ID==id)).all()
        for item in data:
            tradFlow = TradFlow()
            tradFlow.atm1 = item.AMT1
            tradFlow.atm2 = item.AMT2
            tradFlow.atm3 = item.AMT3
            tradFlow.svc = item.SVC
            tradFlow.curr = item.CURR
            result.append(tradFlow)
        return result


class CustomMessage:
    ecifId = "" #ECIF客户编号
    depositMessage = [] #存款产品持有
    investMessage = [] #理财产品持有
    bankInfo = [] #银行信息
    loanMessage = [] #个贷产品持有
    channelInfo = [] #电子渠道个人签约客户渠道信息
    basicMessage = [] #电子渠道个人签约客户基本信息
    fundInfo = [] #基金交易成交信息
    tradFlow = [] #电子渠道交易流水

    def selectByEcifId(id):
        customMessage = CustomMessage()
        customMessage.ecifId = id
        customMessage.depositMessage = DepositMessage.selectByEcifId(id)
        customMessage.investMessage = InvestMessage.selectByEcifId(id)
        customMessage.bankInfo = BankInfo.selectByEcifId(id)
        customMessage.loanMessage = LoanMessage.selectByEcifId(id)
        customMessage.channelInfo = ChannelInfo.selectByEcifId(id)
        customMessage.basicMessage = BasicMessage.selectByEcifId(id)
        customMessage.fundInfo = FundInfo.selectByEcifId(id)
        customMessage.tradFlow = TradFlow.selectByEcifId(id)
        return customMessage