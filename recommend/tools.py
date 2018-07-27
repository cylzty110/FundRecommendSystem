import json
import pandas as pd
from recommend.custom import CustomMessage
from recommend import custom, models


# 类转Json
def classToJson(obj):
    json_str = json.dumps(obj, default=lambda o: o.__dict__, ensure_ascii=False, indent=2)
    return json_str


# 将数据库数据转换为DataFrame类型数据
def getData():
    result = []
    userList = models.TBL_CUST_ID_CONV.selectAll()
    for userId in userList:
        dataList = []
        customMessage = CustomMessage.selectByEcifId(userId.ECIF_CST_ID)
        for dic in customMessage.__dict__:
            temp = getattr(customMessage, dic)
            if 'Id' in dic:
                continue
            for key in temp.__dict__:
                dataList.append(getattr(temp, key))
        result.append(dataList)
    dataFrame = pd.DataFrame(result)
    return dataFrame
