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
    dataList = []
    userList = models.TBL_CUST_ID_CONV.selectAll()
    for userId in userList:
        customMessage = CustomMessage.selectByEcifId(userId.ECIF_CST_ID)
        for dic in customMessage.__dict__:
            temp = getattr(customMessage, dic)
            for key in temp.__dict__:
                dataList.append(getattr(temp, key))
    dataFrame = pd.DataFrame(dataList)
    return dataFrame
