import json
import os

class UserManager:
    def __init__(self):
        self.user_cnt=0
        self.user_list=[{}]
        self.empty_id=[]
    def add_user(self,name:str,age:int)->dict:
        get_id=0
        if(len(self.empty_id)):
            get_id=self.empty_id[0]
            del self.empty_id[0]
        else:
            user_cnt=user_cnt+1
            get_id=user_cnt
        user_dict_tmp={
            "id":get_id,
            "name":name,
            "age":age,
        }
        self.user_list.append(user_dict_tmp)
        return user_dict_tmp
    def find(self,id:int)->dict:
        if(id<1 or id>self.user_cnt):
            return None
        if(id in self.empty_id):
            return None
        return self.user_list[id]
    def update_age(self,id:int,age:int)->bool:
        if(id<1 or id>self.user_cnt):
            return False
        if(id in self.empty_id):
            return False
        self.user_list[id]["age"]=age
        return True
    def remove_user(self,id:int)->bool:
        pass
    def list():
        pass
    def save_all():
        pass
    def load():
        pass