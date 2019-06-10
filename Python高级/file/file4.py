####在上一道题目的基础上增加一点功能，使用户可以随意的输入需要显示的行数
###---12:24
###--- :
###--- :9
###用以上方式表示要打印的起始和结束的行数

filename = input("请输入文件名：")
hangshu = input("请输入需要显示的行数，格式为1:9或者 :：")

def print_line(filename,hangshu):
    f = open(filename)
    begin, end = hangshu.split(":")
    if begin == "":
        begin = 1
    if end == "":
        end = -1

    begin = int(begin) - 1
    end = int(end)

    line = end - begin

    #消耗掉begin之前的行数
    for i in range(begin):
        f.readline()

    if line < 0:
        print(f.read())
    else:
        for j in range(line):
            print(f.readline())
    f.close()

print_line(filename,hangshu)
