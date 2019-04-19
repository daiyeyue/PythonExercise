import random
import math

def line():
    #定义一个空字符串
    str_num = ''
    #循环前4个随机字母,使用ASCII码表
    for i in range(0,4):
        str_num = str_num + chr(random.randrange(97,123))

    for i in range(0,8):
        str_num = str_num + chr(random.randrange(48,58))

    return str_num




def num_game(total,source):
    while 1:
        num = input("请输入三位数，输入-1结束")
        if int(num) == -1:
            break
        if num.isdigit() and 100<= int(num) <=999:
            #计算有效输入有多少次
            total = total + 1
            print("输入次数为",total)
            rd = random.randint(100,999)
            if int(num) > rd:
                print("百位数是{},十位数是{},个位数是{}".format(num[0],num[1],num[2]))
            if int(num) < rd:
                for i in range(0,12):
                #因为line有返回值，所以需要一个变量来接收返回值
                    str_line = line()
                    #参数a是追加，w是写入
                    with open('str_num.txt','a') as f:
                        f.write(str_line+'\n')
               # print(str_line)
            if int(num) == rd:
                source = source + 10
                print("恭喜你中奖了,目前分数为",source/total)
                print("中奖")
        else:
            print("你输入的是什么玩意儿！！！")

#程序入口
if __name__ == '__main__': #当模块被import到其他模块中时，__name__ == '__main__'结果为假，就是不调用对应的方法。
    # 定义一个变量用于初始化分数
    source = 0
    # 定义一个变量累计输入了多少次
    total = 0
    num_game(total,source)

