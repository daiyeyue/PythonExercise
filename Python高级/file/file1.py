#编写一个程序，接收用户输入的内容，并且保存为新的文件
#如果用户输入:w的话，表示文件保存退出

filename = input("请输入文件名:")
def filewrite(filename):
    f = open(filename,"w")
    print("请输入内容，单独输入:w保存退出")

    while True:
        write_something = input()
        #判断用户是否输入:w
        if write_something != ":w":
            #向文件里面输入内容
            f.write("%s\n" %write_something) #python格式化输出，参考https://www.cnblogs.com/claidx/p/7253288.html
        else:
            break
    f.close()

filewrite(filename)

# f1 = open(filename)
# for each in f1:
#     print(each)

