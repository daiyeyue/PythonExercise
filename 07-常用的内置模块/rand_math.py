import math
import random

#输入函数
num = input("请输入一个三位数")

#输入函数输入的是字符类型，所以必须强制转换，不转换会报错
if num.isdigit() and 100 <= int(num) <= 999:
    #判断输入的数，与系统随机数比较大小
    pass

else:
    print('请按规定输入')

