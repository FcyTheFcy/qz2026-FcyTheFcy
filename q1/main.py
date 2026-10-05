import json
def analyze_log(filepath:str)->dict:
    try:
        with open(filepath,encoding="utf-8")as fl:
            contents=fl.read()
            contents=contents.splitlines()
            #初始化所需要返回的字典
            dic={
                "total":0,
                "by_level":{},
                "by_user":{},
                "last_error":None,
            }
            #逐个json对象判断
            for jscontent in contents:
                try:
                    jstmp=json.loads(jscontent)
                except json.JSONDecodeError:
                    #非u正确格式的直接跳过
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
        #找不到文件返回空字典
        return {}


if __name__=="__main__":
    pass