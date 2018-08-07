import json
import pandas as pd
from recommend.custom import CustomMessage
from recommend.fundinfo import FundInfo
from recommend import models, db


# 类转Json
def classToJson(obj):
    json_str = json.dumps(obj, default=lambda o: o.__dict__, ensure_ascii=False, indent=2)
    return json_str


# 由数字生成对应字母
def getAlphabet(num):
    result = ""
    while num > 0:
        m = num % 26
        if m == 0:
            m = 26
        result = chr(64 + m) + result
        num = int((num - m) / 26)
    return result


# 将数据库数据转换为DataFrame类型数据
def getAllUserData():
    result = []
    index = []
    sql = "select ECIF_CUST_NO from TBL_CUST_ID_CONV"
    user_list = db.session.execute(sql)
    for item in user_list:
        data_list = getUserData(item.ECIF_CUST_NO)
        index.append(item.ECIF_CUST_NO)
        result.append(data_list)
    dataFrame = pd.DataFrame(result)
    return dataFrame, index


def getAllFundData():
    result = []
    index = []
    sql = "select SCR_PD_ECD from FND_BSC_INF"
    fund_list = db.session.execute(sql)
    for item in fund_list:
        data_list = getFundData(item.SCR_PD_ECD)
        index.append(item.SCR_PD_ECD)
        result.append(data_list)
    dataFrame = pd.DataFrame(result)
    return dataFrame, index


def getFundData(id):
    data_list = []
    fund_info = FundInfo.selectByFundId(id)
    for dic in fund_info.__dict__:
        temp = getattr(fund_info, dic)
        if 'Id' in dic:
            continue
        for key in temp.__dict__:
            data_list.append(getattr(temp, key))
    return data_list


def getUserData(id):
    data_list = []
    custom_message = CustomMessage.selectByEcifId(id)
    for dic in custom_message.__dict__:
        temp = getattr(custom_message, dic)
        if 'Id' in dic:
            continue
        for key in temp.__dict__:
            data_list.append(getattr(temp, key))
    return data_list
