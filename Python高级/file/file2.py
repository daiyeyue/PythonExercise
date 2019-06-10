#比较两个文件内容，如果不同，则显示出所有不同的行号

file1 = input("请输入第一个需要比价的文件名：")
file2 = input("请输入第二个需要比价的文件名：")

def file_compare(file1,file2):
    f1 = open(file1)
    # for line1 in f1:
    #     print(line1)
    f2 = open(file2)
    # for line2 in f2:
    #     print(line2)
    count = 0 #统计行数
    differ = [] #统计不一样的数量

    for line1 in f1:
        line2 = f2.readline()
        print(line2)
        count = count + 1
        if line1 != line2:  #文件不同
            differ.append(count)
    f1.close()
    f2.close()
    return differ

differ = file_compare(file1,file2)

if len(differ) == 0:
    print("两个文件完全相同")
else:
    print("两个文件有%s处不同" %len(differ))
    for each in differ:
        print(each)