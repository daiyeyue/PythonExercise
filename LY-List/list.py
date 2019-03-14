#append() 向列表末尾添加新元素 返回值None
list1 = [1,2,3,4,5]
print(id(list1))
list1.append(5)
print(list1)
print(id(list1))

# copy 复制列表
list1 = [1,2,3,4,5]
list2 = list1.copy()
print(list2)
print(id(list1))
print(id(list2))

# count() 计算某个元素在列表中出现的次数
list1 = [1,2,3,4,5]
print(list1.count(2))

#extend() 将一个列表继承另一个列表
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
list3 = list1.extend(list2)
print(list1)
print(list2)
print(list3)  #注意结果出乎意料
print(list1+list2)

list3 = list1
print(list3)

#index() 获取值在列表中的索引,找到第一个匹配的值
list1 = [1,2,3,4,5,3,2]
print(list1.index(3))
print(list1.index(2,2,7))

# insert() 在指定位置前插入元素 2个参数
list1 = [1,2,3,4,5]
list1.insert(2,9)
print(list1)

# pop() 根据索引移除列表内一个元素，不给索引默认移除最后一个 返回移除那个值
list1 = [1,2,3,4,5]
print(list1.pop())
print(list1)

# remove() 移除李表中指定的值   返回None
list1 = [1,2,3,4,5]
print(list1.remove(2))
print(list1)

#reverse() 列表翻转
list1 = [1,2,3,4,5]
print(list1)
list1.reverse()
print(list1)

#sort() 排序 默认从小到大
list1 = [1,2,3,7,5]
list1.sort()
print(list1)

#从小到大
list1.sort(reverse=True)
print(list1)
