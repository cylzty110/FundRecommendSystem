import json


#类转Json
def classToJson(obj):
    json_str = json.dumps(obj, default=lambda o: o.__dict__, ensure_ascii=False, indent=2)
    return json_str