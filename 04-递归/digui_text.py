#类似于栈的先进后出模式
#满足两个条件：
#1. 要有递推关系；
#2. 要有临界值
def digui(num):
    print(num)
    #定义临界值
    if num > 0:
        #调用自身函数
        digui(num-1)
    else:
        print("="*20)
    print(num)

digui(3)


i = 0
def a():
    global i
    i = i + 1
    print(i)
a()