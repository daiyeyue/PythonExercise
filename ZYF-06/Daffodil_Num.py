# 编写一个程序，求100-999之间的所有水仙花数
# 水仙花数：如果一个3位数等于各位数字的立方和，则称之为水仙花数。例如：153=1^3+5^3+3^。

for num in range(100,1000):
    hundredsDigit = int(num/100)
    tensDigit = int((num - hundredsDigit * 100)/10)
    singleDigit = num - hundredsDigit * 100 - tensDigit * 10

    if num == hundredsDigit ** 3 + tensDigit ** 3 + singleDigit ** 3:
        print(str(num) + "是水仙花数")


