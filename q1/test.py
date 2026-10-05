import main
import json

#该源文件用于测试analy_log()函数，成功运行则生成一个test_out.json文件
#test_out.json文件所展示的内容即为analy_log()的返回值

if __name__=="__main__":
    dic=main.analyze_log("test.jsonl")
    dic=json.dumps(dic,ensure_ascii=False,indent=4)
    with open("test_out.json",mode="w",encoding="utf-8") as output:
        output.write(dic)
