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
