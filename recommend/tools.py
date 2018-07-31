import json
import pandas as pd
from recommend.custom import CustomMessage
from recommend.fundinfo import FundInfo
from recommend import models, db


# 类转Json
def classToJson(obj):
    json_str = json.dumps(obj, default=lambda o: o.__dict__, ensure_ascii=False, indent=2)
    return json_str


# 将数据库数据转换为DataFrame类型数据
def getUserData():
    result = []
    userList = models.TBL_CUST_ID_CONV.selectAll()
    for item in userList:
        dataList = []
        customMessage = CustomMessage.selectByEcifId(item.ECIF_CUST_NO)
        for dic in customMessage.__dict__:
            temp = getattr(customMessage, dic)
            if 'Id' in dic:
                continue
            for key in temp.__dict__:
                dataList.append(getattr(temp, key))
        result.append(dataList)
    dataFrame = pd.DataFrame(result)
    return dataFrame

def getFundData():
    result = []
    sql = "select SCR_PD_ECD from FND_BSC_INF"
    fundList = db.session.execute(sql)
    for item in fundList:
        datalist = []
        fundInfo = FundInfo.selectByFundId(item.SCR_PD_ECD)
        for dic in fundInfo.__dict__:
            temp = getattr(fundInfo, dic)
            if 'Id' in dic:
                continue
            for key in temp.__dict__:
                datalist.append(getattr(temp, key))
        result.append(datalist)
    dataFrame = pd.DataFrame(result)
    return dataFrame