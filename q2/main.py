import json
class UserManager:
    def __init__(self):
        self.user_dict={
            "cnt":0
        }
    #添加用户
    def add_user(self,name:str,age:int)->dict:
        self.user_dict["cnt"]=self.user_dict["cnt"]+1
        dict_tmp={
            "id":self.user_dict["cnt"],
            "name":name,
            "age":age,
        }
        self.user_dict[self.user_dict["cnt"]]=dict_tmp
    #查询用户（id查询）
    def find(self,id:int)->dict:
        return self.user_dict.get(id)
    #更改年龄
    def update_age(self,id:int,age:int)->bool:
        if(self.user_dict.get(id)==None):
            return False
        self.user_dict[id]=age
        return True
    #移除用户（id定位）
    def remove_user(self,id:int)->bool:
        if(self.user_dict.get(id)==None):
            return False
        if(id==self.user_dict["cnt"]):
            self.user_dict["cnt"]=self.user_dict["cnt"]-1
        del self.user_dict[id]
        return True
    #列出用户
    def list(self):
        for i in self.user_dict.keys():
            if(i=="cnt"):
                continue
            print(self.user_dict[i])
    #保存：生成users.json
    def save(self):
        with open("users.json",encoding="utf-8",mode="w")as fl:
            json.dump(self.user_dict,fl,ensure_ascii=False,indent=4)
    #读入：小做修改：如果成功读取文件返回True代表读取成功，读取失败不会抛出FileNotFoundError异常
    def load(self)->bool:
        try:
            with open("users.json",encoding="utf-8",mode="r")as fl:
                self.user_dict=json.load(fl)
        except FileNotFoundError:
            return False
        return True
if __name__=="__main__":
    pass