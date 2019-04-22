#写一个6位随机验证码程序（使用random模块），要求验证码中至少包含一个数字、一个小写字母、一个大写字母
import random
import string

#yanzhengma = input("请输入验证码：")

help(string)
code = []
code.append(random.choice(string.ascii_lowercase)) #保证验证码中有一个小写字母
code.append(random.choice(string.ascii_uppercase)) #保证验证码中有一个大写字母
code.append(random.choice(string.digits)) #保证验证码中有一个数字
print(code)
while len(code) < 6:
    code.append(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits))

q_code = "".join(code)
print(q_code)


#写一个用户验证登录程序，文件如下1234.json
#{"expire_date": "2021-01-01", "id": "1234", "status": 0, "pay_day": 22, "password": "abc"}
#用户名是json的文件名
#判断是否过期，与expire_date进行比较
#登录成功后打印登录成功，三次登录失败，status的值改为1，并且锁定账号

import os
import time
import json

count = 0 #计数器

exit_flag = False

while count < 3:
    user = input("请输入用户名：")
    f = user.strip() + ".json" #strip是去掉用户输入时的空格
    if os.path.exists(f):
        fp = open(f, "r+",encoding = "utf-8") #r+ 表示打开一个文件用于读写。文件指针将会放在文件的开头
        j_user = json.load(fp)
        if j_user['status'] == 1:
            print("账号已经锁定")
            break
        else:
            expire_dt = j_user["expire_date"]
            current_st = time.time()
            expire_dt = time.mktime(time.strptime(expire_dt,"%Y-%m-%d"))

            if current_st > expire_dt:
                print("用户已经过期")
                break
            else:
                while count<3:
                    pw = input("请输入密码：")

                    if pw.strip() == j_user["password"]:
                        print("登录成功")
                        exit_flag = True
                        break
                    else:
                        if count == 2:
                            #j_user["status"] = 1
                            print("输入三次密码错误，锁定用户")
                            fp.seek(0)
                            fp.truncate() #清空文件内容
                            json.dump(j_user,fp) #写入j_user到fp
                        count = count + 1
    if exit_flag:
         break
    else:
         #print("用户不存在")
         count = count + 1


