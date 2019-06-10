#编写一个程序，当用户输入文件名和行数的时候，把该文件的前N行打印到屏幕上

filename = input("请输入文件名：")
hangshu = input("请输入行数：")

def file_view(filename,hangshu):
    print("\n文件%s的前%s行的内容如下" %(filename, hangshu))
    f = open(filename)
    for i in range(int(hangshu)):
        print(f.readline())
    f.close()

file_view(filename,hangshu)

