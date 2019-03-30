#数据类型的内置函数
'''
python的数据类型
Number  数值型(int float   bool    complex(负数))
string  字符串
tuple   元组
dict    字典
list    liebiao
set     集合
'''

#字符串的简单操作
'''
+   字符串的连接操作
*   字符串的复制操作
[]  字符串的索引操作
[开始索引:结束索引:间隔值]    字符串的切片操作，包含开头，不包含结尾
'''
#capitalize 首字母大写，返回字符串
s = 'i like dog'
print(s.capitalize())

#title() 将每个单词的首字母大写
s = 'i like dog'
print(s.title())

#upper() 将所有字母都变成大写
s = 'i like dog'
print(s.upper())

#lower() 将所有字母变成小写字母
s = 'i like dog'
print(s.lower())

#swapcase() 大小写互换
s = 'i like dog'
print(s.swapcase())

#len() 计算字符串的长度，不属于字符串的内置函数
s = 'i like dog'
print(len(s))

#find() 查找指定字符串，找不到返回-1,找到返回索引值
#index() 查找指定字符串，找不到报错，找到返回索引值
s = 'asdfghjklasdfghjkl'
s1 = s.find('a')
s2 = s.index('f')
print(s1)
print(s2)

#count() 查找指定字符串出现的次数
s = 'asdfghjklasdfghjkl'
print(s.count('ab'))

#startwith() 检测是否指定字母开头, 返回True or False
#endwith() 检测是否指定字母结尾, 返回True or False
s = 'asdfghjklasdfghjkl'
print(s.startswith('a'))
print(s.startswith('b'))

#isupper() 检查所有字母是否大写字母，返回布尔值
#islower() 检查所有字母是否小写字母，返回布尔值

#istitle() 检查是否以指定标题显示（每个单词首字母大写）
s = 'i like dog'
s1 = 'I Like Dog'
print(s.istitle())
print(s1.istitle())

#isspace() 检查所有字母是否空格，返回布尔值
s = ' '
print(s.isspace())



