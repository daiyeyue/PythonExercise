#clear() 清除整个字典，返回None
dict1 = {"a":1,"b":2,"c":3}
dict1.clear()
print(dict1)

dict1 = {"a":1,"b":2,"c":3}
dict2 = dict1.copy()
print(dict2)

# fromkeys() 按照指定的序列为键创建字典，值都是一样的
list1 = ['a','b','c']
dict1 = {}.fromkeys(list1)
dict2 = {}.fromkeys(list1,3)
print(dict1,dict2)

help(dict)

# get() 根据键获取指定的值，找不到的键如果设默认值则返回默认值，如果没有设置默认值，返回None
dict1 = {"a":1,"b":2,"c":3}
print(dict1.get('b'))
print(dict1.get('d'))
print(dict1.get('d',4))

# items() 将字典变成类似于元组的形式方便遍历
dict1 = {"a":1,"b":2,"c":3}
for k,v in dict1.items():
    print(k,v)
print(dict1.items())

#pop() 移除字典指定元素 返回键所对应的值。如果键不存在，则返回默认值，如果键找不到，没设默认值，就会报错
dict1 = {"a":1,"b":2,"c":3}
print(dict1.pop('a'))
print(dict1.pop('d',4))
#print(dict1.pop('d'))

#popitem() 移除字典的键值对，返回移除的键值对
dict1 = {"a":1,"b":2,"c":3}
print(dict1.popitem())
print(dict1)
print(dict1.popitem())
print(dict1)

# setdefault() 在字典里添加一个元素
dict1 = {"a":1,"b":2,"c":3}
print(dict1.setdefault('d',5))
print(dict1)



#update() 修改字典中的值
dict1 = {"a":1,"b":2,"c":3}
dict1.update({"a":3,"e":6})
print(dict1)

dict1["d"] = 34
print(dict1)

help(set)
a = set()
print(a)
list1 = [1,2,3,4]
a = set(list1)
print(a)

# add() 向集合中添加元素
set1 = {5,1,2,3,4,'b','u'}
set1.add('6')
print(set1)

# clear() 清空集合
# copy() 复制集合
# pop() 随机弹出一个元素
a = {5,1,2,3,4,'b','u'}
a.pop()
print(a)

#remove() 删除集合中的某个值，如果这个值不在集合中报错
a = {5,1,2,3,4,'b','u'}
a.remove(4)
print(a)
#a.remove(4)

# difference() 差集
# difference_update() 区别就是第一个返回一个新的集合，第二个就是把原来的集合覆盖
set1 = {1,2,3,4,7}
set2 = {2,4,5,111,24}
set3 = set1.difference(set2)
print(set3)
print(set1)

set1 = {1,2,3,4,7}
set2 = {2,4,5,111,24}
set1.difference_update(set2)
#print(set4)
print(set1)