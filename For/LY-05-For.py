'''
打印以下图形
* 
* * 
* * * 
* * * * 
* * * * * 
'''
for i in range(0,5):
    print("* " * (i + 1))


'''

打印以下图形
* 
* * 
*   * 
*     * 
* * * * * 
'''
for i in range(0,5):
    for j in range(0,i+1):
        if i == 4:
            print("* ", end="")
            continue

        # 如果不是最后一行
        # j是控制列的数字
        if j == 0 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

'''
打印倒三角
* * * * * 
* * * * 
* * * 
* * 
* 
'''
for i in range(0,5):
    for j in range(0,5-i):
        print("* ", end="")
    print()

#这样也可以
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("* ", end="")
    print()

'''
打印倒空三角
* * * * * 
*     * 
*   * 
* * 
* 
'''
for i in range(0,5):
    for j in range(0,5-i):
        if i == 0:
            print("* ", end="")
            continue
        if j == 0 or j == 5-i-1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

def triangle(n):
    '''
    *           
   * *
  * * *
 * * * * 
* * * * *
    :param n: 等边三角形的行数
    :return: 
    '''
    if n <= 1:
        print("一行*无法成为等边三角形")
    else:
        for i in range(n,0,-1):
            print(" " * (i - 1) + "*" + " *" * (n-i))


triangle(5)