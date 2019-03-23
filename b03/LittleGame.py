#给用户三次机会，猜想我们程序生成的一个数字A，每次用户猜想过后会提示数字是否正确以及用户输入数字是大于还是小于A，当机会用尽后提示用户已经输掉了游戏
import random

secret = random.randint(1,100) #产生随机数
print(secret)

times = 3 #初始化用户次数是3

while times:
    num = input("请输入数字")
    if num.isdigit():
        tmp = int(num)
        if tmp == secret:
            print("你答对了")
            break
        elif tmp < secret:
            print("你的数字太小了")
            times = times -1
        else:
            print("你的数字太大了")
    else:
        print("让你输入数字")
print("你的机会用完了")