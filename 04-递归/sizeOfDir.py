import os
#help(os)
def getdirpath(dirpath):
    total =0
    #获取所有文件
    allname = os.listdir(dirpath)
    #print(allname)
    #print(len(allname))
    for name in allname:
        fullpath = os.path.join(dirpath,name)
        #判断是否为文件
        if os.path.isfile(fullpath):
            #获取文件大小
            total = total + os.path.getsize(fullpath)
        elif os.path.isdir(fullpath):
            total = total + getdirpath(fullpath)
    return total
size = getdirpath('D:\BaiduYunDownload')
print(size)





getdirpath('D:\BaiduYunDownload')