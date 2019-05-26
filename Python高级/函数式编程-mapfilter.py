#利用map()函数，把用户输入的不规范的英文，变成首字母大写，其他小写的规范的名字：比如：["ADMan","LISA"]变成，["Adman","Lisa"]

def change(str):
    str = str.capitalize()
    return str

#print(list(map(change,["ADMan","LISA"])))

str_list = ["ADMan","LISA"]
print(list((map(change,str_list))))

#回数：从左向右和从右向左读都是一样的数，比如：12321，999,找1-999之间的回数
#请利用filter()函数

def equal(a,b):
    return a == b
#print(equal(3,4))

def is_palindrome(n):
    s = str(n) #先转换成字符串
    for i in range(0,len(s)-1):
        if equal(s[i],s[len(s)-i-1]):
            continue
        else:
            return False
    return True

output =  list(filter(is_palindrome,range(1,999)))
print(output)

#假设，用一组元组tuple来表示学生的名字和成绩，L = [("Bob",75),("Adan",92),("Bart",66),("List",88)],用sorted对上述的列表按照名字排序

L = [("Bob",75),("Adan",92),("Bart",66),("List",88)]

def by_name(t):
    t = sorted(t[0],key=str.lower)
    return t

L2 = sorted(L,key = by_name)
print(L2)

#按照成绩高低进行排序
def by_score(t):
    #t.sort(key=lambda x : x[1])
    t = sorted(range(t[1])) ###使用range包裹一下，就变成可迭代对象，要不报错：TypeError: 'int' object is not iterable
    return t

L2 = sorted(L,key = by_score, reverse=True) ##想要逆序，需要在这里进行定义，不能在函数里面定义
print(L2)
#L = [("Bob",75),("Adan",92),("Bart",66),("List",88)]
#print(by_score(L))
# L.sort(key=lambda x : x[1],reverse=True)
# print(L)

# l=[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
# print(sorted(l, key=lambda x:x[1]))
# print(sorted(l, key=lambda x:x[1], reverse=True))


