#利用map()函数，把用户输入的不规范的英文，变成首字母大写，其他小写的规范的名字：比如：["ADMan","LISA"]变成，["Adman","Lisa"]
#使用lambda函数

ls = ["ADMan","LISA"]
new_ls = list(map(lambda x:x.capitalize(),ls))
print(new_ls)

#回数：从左向右和从右向左读都是一样的数，比如：12321，999,找1-999之间的回数
#请利用filter()函数
#先打印1-1000之间的回数

ls = list(range(0,1000))
print(ls)
output = list(filter(lambda x: str(x)[0] == str(x)[len(str(x))-1],ls))
print(output)

#假设，用一组元组tuple来表示学生的名字和成绩，L = [("Bob",75),("Adan",92),("Bart",66),("List",88)],用sorted对上述的列表按照名字排序
L = [("Bob",75),("Adan",92),("Bart",66),("List",88)]

L2 = sorted(L, key = lambda x:x[1],reverse=True) ###x[0]按照姓名排序，x[1]按照分数排序
print(list(L2))