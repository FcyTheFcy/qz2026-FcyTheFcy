import json
import os
def analyze_log(filepath:str)->dict:
    try:
        with open(filepath,encoding="utf-8")as fl:
            contents=fl.read()
            contents=contents.splitlines()
            dic={
                "total":0,
                "by_level":{},
                "by_user":{},
                "last_error":None,
            }
            for jscontent in contents:
                try:
                    jstmp=json.loads(jscontent)
                except json.JSONDecodeError:
                    continue
                dic["total"]=dic["total"]+1
                if(dic["by_level"].get(jstmp["level"])==None):
                    dic["by_level"][jstmp["level"]]=1
                else:
                    dic["by_level"][jstmp["level"]]=dic["by_level"][jstmp["level"]]+1
                if(dic["by_user"].get(jstmp["user"])==None):
                    dic["by_user"][jstmp["user"]]=1
                else:
                    dic["by_user"][jstmp["user"]]=dic["by_user"][jstmp["user"]]+1
                if(jstmp["level"]=="ERROR"):
                    dic["last_error"]=jstmp["message"]
            return dic
    except FileNotFoundError:
        return {}


if __name__==__main__:
    pass