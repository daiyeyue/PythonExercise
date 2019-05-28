import json
fp = open("1234.json", "r+",encoding = "utf-8")
j_user = json.load(fp)
j_user["status"] = 1
fp.seek(0)
fp.truncate() #清空文件内容
json.dump(j_user,fp)


for i in range(6):
    print("a")