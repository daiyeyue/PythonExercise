help(tuple)

#count() 计算某个元素在元组中出现的次数
tuple1 = (1,2,3,4,5,6,1)
print(tuple1.count(1))
print(tuple1.count(7))

#index() 获取值在元组中的索引
tuple1 = (1,2,3,4,5,6,1)
print(tuple1.index(3))
print(tuple1.index(1,0,7))