#编写一个程序，实现“全部替换”的功能
# open 函数打开文件
# readline读取文件行内容
# replace函数

filename = input("请输入文件名：")
rep_word = input("请输入需要替换的内容：")
new_word = input("请输入需要替换的新的内容：")
def file_replase(filename,rep_word,new_word):
    f = open(filename)
    content = []
    for eachline in f:
        if rep_word in eachline:
            eachline = eachline.replace(rep_word,new_word)
        content.append(eachline)
    print(content)
    decide = input("你确定要这么做嘛？请输入yes or no")
    if decide in ["YES","Yes","yes"]:
        f_write = open(filename,'w')
        f_write.write("".join(content))
        f_write.close()

file_replase(filename,rep_word,new_word)
