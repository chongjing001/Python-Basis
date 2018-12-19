
"""
编程实现(for和while各写⼀一遍):
1. 求1到100之间所有数的和、平均值
2. 计算1-100之间能3整除的数的和
3. 计算1-100之间不不能被7整除的数的和

"""

# # for 循环
# sum1 = 0  # 存储和
# avg1 = 0    # 存储平均值
# num1 = 0   # 记录次数
# for i in range(101):
#     sum1 += i
#     num1 += 1
# print("1到100之间所有数的和: %d" % sum1)
# print("1到100之间所有数的平均值：%.2f" % (sum1 / num1))
#
# # while 循环
# sum2 = 0
# i = 1
# while i <= 100:
#     sum2 += i
#     i += 1
# print("1到100之间所有数的和: %d" % sum2)
# print("1到100之间所有数的平均值: %.2f" % (sum2/i))
#
#
#
# # for循环
# sum1 = 0   # 存储和
# for i in range(101):
#     if i % 3 == 0:
#         sum1 += i
# print("1-100之间能3整除的数的和: %d" % sum1)
#
# # while 循环
# sum2 = 0
# i = 1
# while i <= 100:
#     if i % 3 == 0:
#         sum2 += i
#     i += 1
# print("1-100之间能3整除的数的和: %d" % sum2)
#
#
# # for循环
# sum1 = 0   # 存储和
# for i in range(101):
#     if i % 7 != 0:
#         sum1 += i
# print("1-100之间不不能被7整除的数的和: %d" % sum1)
#
# # while 循环
# sum2 = 0
# i = 1
# while i <= 100:
#     if i % 7 != 0:
#         sum2 += i
#     i += 1
# print("1-100之间不不能被7整除的数的和: %d" % sum2)


"""
1. 求斐波那契数列列中第n个数的值：1，1，2，3，5，8，13，21，34.... 
"""
# num = int(input("请输入你需要查阅斐波那契数列列中第n个数的值"))
# # n1,n2记录最开始的两个数
# n1 = 1
# n2 = 1
# result = 0
# if num <= 0:
#     print("请输入正整数")
# elif num == 1:
#     print("斐波那契数列列中第1个数的值是1")
# elif num == 2:
#     print("斐波那契数列列中第2个数的值是1")
# else:
#     for count in range(2, num):
#         result = n1 + n2
#         n1 = n2
#         n2 = result
#     print("斐波那契数列列中第%d个数的值是:%d" % (num, result))


"""
判断101-200之间有多少个素数，
并输出所有素数。判断素数的⽅方法：
⽤用⼀一个数分别除2到sqrt(这个 数)，
如果能被整除，则表明此数不不是素数，反之是素数 
"""


for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

"""
3. 打印出所有的⽔水仙花数,所谓⽔水仙花数是指⼀一个三位数，
其各位数字⽴立⽅方和等于该数本身。
例例如：153是 ⼀一个⽔水仙花数,因为153 = 1^3 + 5^3 + 3^3 
"""

for i in range(100, 1000):
    gewei = i % 10
    shiwei = i % 100 // 10
    baiwei = i % 1000 // 100
    if gewei**3 + shiwei**3 + baiwei**3 == i:
        print(i)


"""
有一分数序列：2/1,3/2,5/3,8/5,13/8,21/13...
求出这个数列的第20个分数 
分子：上一个分数的分子加分⺟
分母: 上一个分数的分子 fz = 2 fm = 1 fz+fm / fz 
"""
fz = temp = 2
fm = 1
for i in range(0, 19):

    fz += fm
    fm = temp
    temp = fz
print("%d//%d" % (fz, fm))

# 5. 给一个正整数，要求：1、求它是几位数 2.逆序打印出各位数字

num = input("请输入一个正整数")
len1 = len(num)
print("%s是%d位数" % (num, len1))
print(num[::-1])
