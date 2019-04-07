#按F4可以打开导入模块的源码
import random

# random() 获取0-1之间的随机小数, 可以取0，不取1
for i in range(10):
    print(random.random())
    #随机指定开始和结束区间的整数
    print(random.randint(1,10))

#random.randrange() 获取指定开始和结束之间，可以指定间隔值。
print(random.randrange(1,9))
print(random.randrange(1,9,3))

#choice() 随机获取列表中的值
import random
print(random.choice([1,3,4,5,6,7]))

#shuffle() 随机打乱序列，返回值是none
import random
s = [1,3,4,5,6,7]
random.shuffle(s)
print(s)

#uniform() 随机获取指定范围内的值
import random
print(random.uniform(1,9))