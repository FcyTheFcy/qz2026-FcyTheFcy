from main import*
import json
if __name__=="__main__":
    um=UserManager()
    um.add_user("群大狗",114514)
    um.add_user("丛雨",500)
    um.add_user("🐵",857857)
    print(um.find(1))
    print(um.find(114514))
    print(um.update_age(3,1919810))
    print(um.remove_user(3))
    print(um.remove_user(3))
    um.list()
    um.save()
    print("-----------------------")
    um2=UserManager()
    um2.load()
    um2.list()
#result:UserManager successfully performed 