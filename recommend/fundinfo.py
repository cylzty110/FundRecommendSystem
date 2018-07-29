from recommend import db, models
from sqlalchemy import and_, func


# 客户关注基金
class CST_FCS_FND:
    def __init__(self):
        self.purchase_num = 0  # 购买该基金人数

    @staticmethod
    def selectByFundId(id):
        result = CST_FCS_FND()
        sql = "select count(*) from CST_FCS_FND where SCR_PD_ECD = %s"
        result.purchaseNum = db.session.execute(sql, id)
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
        self.fundValue = 0.0  # 基金面值
        self.fundPrice = 0.0  # 基金发行价格
        self.fundFirstFeeRate = 0.0  # 基金首次销售服务费率
        self.fundYearFeeRate = 0.0  # 基金销售服务费年费率
        self.type = "empty"  # 基金分类编码
        self.riskGrade = 0  # 基金风险等级代码
        self.riskValue = 0.0  # 基金风险等级评估值

    @staticmethod
    def selectByFundId(id):
        result = FND_BSC_INF()
        data = models.FND_BSC_INF.query.filter_by(SCR_PD_ECD=id).all()
        for item in data:
            result.fundValue = float(data.FND_DNMN)
            result.fundPrice = float(data.FND_ISSU_PRC)
            result.fundFirstFeeRate = float(data.FNDFTMSALESVCFEE_RATE)
            result.fundYearFeeRate = float(data.FNDSALESVCFEEYR_FEERT)
            result.type = data.GLX_FND_LVL2_CL_ECD
            result.riskGrade = int(data.RSK_GRD_CD)
            result.riskValue = float(data.FND_RSK_GRD_EVAL)
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
        result.unitFundBonu = data.UNIT_FND_DVDN_AMT
        result.thisUnitFundBonu = data.THS_FND_UNIT_DVDN_AMT
        result.yearAmount = data.YR_ACAMT
        return result


# 基金转托管信息
class FND_TFROFCSTD_INF:
    pass


class FundInfo:
    def __init__(self):
        self.fundId = 0
        self.cst_fcs_fnd = CST_FCS_FND()
        self.cst_fnd_pft_info = CST_FND_PFT_INFO()
        self.fnd_auto_txn_itt_dtl = FND_AUTO_TXN_ITT_DTL()
        self.fnd_bsc_inf = FND_BSC_INF()
        self.fnd_ftr_attr = FND_FTR_ATTR()
        self.fnd_intlg_txn_strtg = FND_INTLG_TXN_STRTG()
        self.fnd_pd_dvdn_inf = FND_PD_DVDN_INF()
        self.fnd_tfrofcstd_inf = FND_TFROFCSTD_INF()

    @staticmethod
    def selectByFundId(id):
        fundInfo = FundInfo()
        fundInfo.fundId = id
        fundInfo.cst_fcs_fnd = CST_FCS_FND.selectByFundId(id)
        fundInfo.fnd_bsc_inf = FND_BSC_INF.selectByFundId(id)
        fundInfo.fnd_pd_dvdn_inf = FND_PD_DVDN_INF.selectByFundId(id)
        return fundInfo
