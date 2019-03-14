#字符串连接操作
s1 = "I love "
s2 = "wangxiaojing"
s3 = s1 + s2
print(s3)

#字符串的乘法
s = "I love wangxiaojing"
s2 = s * 10
print(s2)

#字符串当成列表
s = "I love wangxiaojing"
print(s[0])
print(s[-1])

##切片操作
s = "123456789"
print(s[2:6])
print(s[:])

###切片返回的是一个全新的字符串嘛？
###如果切片去一部分，则返回全新字符串
###如果取完整切片，可能返回内容指向同一字符串
s = "I love wangxiaojing"
s1 = s
print(len(s))
print(id(s))
print(id(s[:]))
print(id(s[:5]))

#不能直接对字符串下表元素赋值
#s1 = 'A'
print(id(s))
print(id(s1))



l = [1,2,3,4,5,6,7,8,9,100]


ll = l[:6]
l2 = l[:]
print(id(l))
print(id(ll))
print(id(l2))

#帮助命令
help(str)

#capitalize手写字母大写，其余小写，返回字符串
s = "I LOVE WangXiaoJing"
print(s.capitalize())

#title()  将每个单词的首字母变成大写 返回是字符串
s = "i love wangXiaoJing"
s1 = s.title()
print(s1)

#upper() 将所有字母变成大写字母 返回是字符串
s = "I like dog"
print(s.upper())

#upper() 将所有字母变成小写字母 返回是字符串
s = "I like dog"
print(s.lower())

#swapcase() 大小写互换 返回是字符串
s = "I like dog"
print(s.swapcase())

#len() 计算字符串长度，是字符的个数（一个汉字的长度就是1），不属于字符串的内建函数
s = "I like dog"
s1 = "I 狗like dog"
print(len(s))
print(len(s1))

#find() 查找指定字符串，找不到返回结果-1，第一次找到返回第一次索引值
#index() 查找指定字符串，找不到报错
s = "asdfghjklasdfghjkl"
s1 = s.find('s',3)
s2 = s.index('s')
print(s1)
print(s2)

#count() 计算字符串出现的次数 返回整形
s = "asdfghjklasdfghjklsssss"
print(s.count('s'))

#startswitch() 检测是否以指定字母开头  返回布尔值
#endswitch() 检查是否以指定字母结尾
s = "I like dog"
print(s.startswith('i'))
print(s.startswith('I'))
print('=' * 20)
print(s.endswith('g'))
print(s.endswith('o'))

#isupper() 检测所有字母是否大写字母   返回布尔值
s = 'f狗gh'
s1 = 'DF狗GH'
print(s.isupper())
print(s1.isupper())
#isupper() 检测所有字母是否小写字母   返回布尔值
print(s.islower())
print(s1.islower())
#istitle() 检测是否以指定标题显示（每个单词首字母大写）
print(s.istitle())
print(s1.istitle())

s2 = 'I Like Dog'
print(s2.istitle())

#isspace() 检测字符串是否是空字符串
s = '    '
s1 = 'I Like   '
s2 = ' ' #至少要有一个，否则返回False
print(s.isspace())
print(s1.isspace())
print(s2.isspace())


#isalpha() 检测字符串是否字母组成，返回布尔值
#说明：汉字在英文字符包裹中被当做字符处理
s = 'I 狗like dog'
s1 = 'I狗likedog'
print(s.isalpha())
print(s1.isalpha())

s2 = '狗like me'
print(s2.isalpha())

#isalnum() 检测字符串是否字母或数字组成，返回布尔值
#说明：汉字在英文字符包裹中被当做字符处理
s = '333'
s1 = 'I狗likedog234'
s2 = 'I 狗234'
print(s.isalnum())
print(s1.isalnum())
print(s2.isalnum())