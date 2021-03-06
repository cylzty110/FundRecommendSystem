from recommend import db, models
from sqlalchemy import and_, func


# 客户关注基金
class CST_FCS_FND:
    def __init__(self):
        self.purchaseNum = 0  # 关注该基金人数

    @staticmethod
    def selectByFundId(id):
        result = CST_FCS_FND()
        sql = "select count(*) from CST_FCS_FND where SCR_PD_ECD = '" + id + "'"
        data = db.session.execute(sql).fetchall()
        result.purchaseNum = data[0][0]
        return result


# 客户基金持券收益信息
class CST_FND_PFT_INFO:
    pass


# 基金自动交易发起明细
class FND_AUTO_TXN_ITT_DTL:
    pass


# 基金基本信息
class FND_BSC_INF:
    def __init__(self):
        self.fundFirstFeeRate = 0.0  # 基金首次销售服务费率
        self.fundYearFeeRate = 0.0  # 基金销售服务费年费率
        self.riskGrade = 0.0  # 基金风险等级代码

    @staticmethod
    def selectByFundId(id):
        result = FND_BSC_INF()
        data = models.FND_BSC_INF.query.filter_by(SCR_PD_ECD=id).all()
        for item in data:
            result.fundFirstFeeRate = float(item.FNDFTMSALESVCFEE_RATE)
            result.fundYearFeeRate = float(item.FNDSALESVCFEEYR_FEERT)
            if item.RSK_GRD_CD:
                result.riskGrade = int(item.RSK_GRD_CD)
        return result


# 基金特征属性
class FND_FTR_ATTR:
    pass


# 基金智能交易策略
class FND_INTLG_TXN_STRTG:
    pass


# 基金产品分红信息
class FND_PD_DVDN_INF:
    def __init__(self):
        self.unitFundBonu = 0.0  # 单位基金分红金额
        self.thisUnitFundBonu = 0.0  # 本次基金单位分红金额
        self.yearAmount = 0.0  # 年累计金额

    @staticmethod
    def selectByFundId(id):
        result = FND_PD_DVDN_INF()
        data = models.FND_PD_DVDN_INF.query.filter_by(SCR_PD_ECD=id).all()
        for item in data:
            result.unitFundBonu = item.UNIT_FND_DVDN_AMT
            result.thisUnitFundBonu = item.THS_FND_UNIT_DVDN_AMT
            result.yearAmount = item.YR_ACAMT
        return result


# 基金转托管信息
class FND_TFROFCSTD_INF:
    pass


class FundInfo:
    def __init__(self):
        self.fundId = 0
        self.cst_fcs_fnd = CST_FCS_FND()
        self.fnd_bsc_inf = FND_BSC_INF()
        self.fnd_pd_dvdn_inf = FND_PD_DVDN_INF()

    @staticmethod
    def selectByFundId(id):
        fundInfo = FundInfo()
        fundInfo.fundId = id
        fundInfo.cst_fcs_fnd = CST_FCS_FND.selectByFundId(id)
        fundInfo.fnd_bsc_inf = FND_BSC_INF.selectByFundId(id)
        fundInfo.fnd_pd_dvdn_inf = FND_PD_DVDN_INF.selectByFundId(id)
        return fundInfo
