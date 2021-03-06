#编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数”的异常
def jianfa(a,b):
    if a < b:
        raise BaseException("被减数不能小于减数")
    else:
        return(a-b)
try:
    jianfa(3,7)
except BaseException as error:
    print("好像出错了，出错的内容是{}".format(error))


#定义一个函数func(filename) filename:文件的路径，函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误
import os
def func(filename):
    try:
        file = open(filename)
    except Exception as error:
        print("出错了，出错的内容是{}".format(error))
    else:
        print(file.read())
        file.close()
func("h")
func(r"D:\test.txt") #需要使用r避免双引号内的\被转义


#自己定义一个异常类，集成Exception类，捕获下面的过程，判断输入的字符串长度是否小于5
class MyError(Exception):
    def __init__(self,stri):
        self.stri = stri
    def process(self):
        if len(self.stri)< 5:
            print("字符串长度必须大于5")
        else:
            print("算你聪明")
try:
    er = MyError(123)
    er.process()
except MyError as error:
    print(error)
