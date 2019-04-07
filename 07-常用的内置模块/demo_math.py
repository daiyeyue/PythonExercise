import math
# ceil() 向上取整
print(math.ceil(5.01))

#floor() 向下取整
print(math.floor(5.1))

#查看系统关键字，不可以作为变量命名
import keyword
print(keyword.kwlist)

#round() 4舍5入操作， python内置函数
print(round(5.6))

#sqrt() 开平方,返回是浮点数
print(math.sqrt(5))

#pow() 与幂运算差不多，计算一个数的几次方
print(math.pow(5,12))

#fabs() 对一个数获取它的绝对值,返回浮点型
print(math.fabs(-9))

#abs() 对一个数获取它的绝对值,不是math模块的
print(abs(-9.8))

#fsum() math模块的求和，对整个队列的求和，输入的参数是可迭代参数Iterable的
print(math.fsum([1,4,5,6]))

#sum() python内置的求和
print(sum([1,4,5,6]))

#math.modf() 把一个浮点数拆分为证书部分和小数部分，组成的元组，小数在前，整数在后
print(math.modf(10))
print(math.modf(-4.5))
help(math.modf)

# copysign() 将第二个数的符号（正负号）传给第一个数,返回第一个数值的浮点数
print(math.copysign(2,-3))
print(math.copysign(-2,3))
print(math.copysign(-2,-3))

#打印自然对数e和π的值
print(math.e)
print(math.pi)