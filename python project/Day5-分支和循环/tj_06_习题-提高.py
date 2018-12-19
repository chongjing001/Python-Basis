
"""
1.控制台输入年龄，根据年龄输出不同的提示
(例如:老年人，青壮年，成年人，未成年，儿童)
"""
# while True:
#     try:
#         age = int(input("请输入年龄"))
#         if 0 < age < 10:
#             print("儿童")
#         elif age < 18:
#             print("未成年")
#         elif age < 25:
#             print("成年人")
#         elif age < 40:
#             print("青壮年")
#         elif 60 <= age < 200:
#             print("老年人")
#         elif age > 200:
#             print("神仙")
#     except:
#         print("请输入正整数")

# 2.计算5的阶乘 5!的结果是

# num = 5
# result = 1
# for i in range(1,num +1 ):
#     result *= i
# print(result)


"""
3.求1+2!+3!+...+20!的和 
程序分析：此程序只是把累加变成了累乘
"""
# sum1 = 0   # 存储和
# for i in range(1, 21):
#     result = 1   # 储存阶乘
#     for j in range(i):
#         result *= j+1
#     sum1 += result
# print(sum1)

# 4.计算 1+1/2!+1/3!+1/4!+...1/20!=?

# sum1 = 0   # 存储和
# for i in range(1, 21):
#     result = 1   # 储存阶乘
#     result1 = 1  # 储存1/阶乘
#     for j in range(i):
#         result *= j+1
#         result1 = 1 / result
#     sum1 += result1
# print(sum1)

# 5.循环输入大于0的数字进行累加，直到输入的数字为0，就结束循环，并最后输出累加的结果

# sum1 = 0
# while True:
#     try:
#         num = float(input("请输入大于0的数字"))
#         if num > 0:
#             sum1 += num
#         elif num < 0:
#             print("您输入的数字小于0，请重新输入")
#         else:
#             print(sum1)
#             break
#
#     except:
#         print("您输入的不是数字，请重新输入")

"""
6.求s=a+aa+aaa+aaaa+aa...a的值，
其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
几个数相加有键盘控制。 1.程序分析：关键是计算出每一项的值
"""





# a = float(input("请输入一个数字"))
# s = 0
# a1 = a
# num = int(input("请输入需要几个数相加"))
# for i in range(num):
#     if num == 1:
#         print(a)
#     else:
#         print(a)
#     s += a
#     a = a*10 + a1
# print(s)


# 7.输入三个整数x,y,z，请把这三个数由小到大输出

# x = int(input("请输入第一个整数"))
# y = int(input("请输入第二个整数"))
# z = int(input("请输入第三个整数"))
#
# if x < y and x < z:
#     if y < z:
#         print(x, y, z)
#     else:
#         print(x, z, y)
# elif y < x and y < z:
#     if x < z:
#         print(y, x, z)
#     else:
#         print(y, z, x)
# elif z < x and z < y:
#     if x < y:
#         print(z, x, y)
#     else:
#         print(z, y, x)
#
#
#
# list1 = [x, y, z]
# max_num = list1.index(max(list1))
# min_num = list1.index(min(list1))
# num1 = 0
# for i in range(3):
#     if min(list1)< list1[i] < max(list1):
#         num1 = i
# print(list1[min_num], list1[num1], list1[max_num])


# 8.
# n = int(input("请输入一个正整数"))
# i = 0
# while i < n:
#     print("*"*(n-i))
#     i += 1
#
#
# n = int(input("请输入一个正整数"))
# i = 0
# while i <= n:
#     if i & 1 == 1:
#         str1 = "*"*i
#         print(str1.center(n, " "))
#     i += 1


# 9.输出9*9口诀。 1.程序分析：分行与列考虑，共9行9列，i控制行，j控制列

# 方法1 while循环
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d*%d=%d " % (j, i, i*j), end="\t")
#         j += 1
#     i += 1
#     print()   # 一行打印完换行
#
# # 方法2 for循环
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d " % (j, i, i*j), end="\t")
#     print()

# 根据数学知识可得：① 3x + 2y + 0.5z = 100
#                 ② x  +  y  +  z  =100
#                由一二可得 5x + 3y = 100
for x in range(0, 100):
    for y in range(0, 100):
        if 5*x + 3*y == 100:
            z = 100 - x - y
            print("大马有%d匹，中马有%d匹，小马有%d匹" % (x, y, z))


# for x in range(0, 100):
#     for y in range(0, 100):
#         if 14*x + 8*y == 100:
#             z = 100 - x - y
#             print("公鸡有%d只，母鸡有%d只，雏鸡有%d只" % (x, y, z))
#             break


"""
12.小明单位发了100元的购物卡，
小明到超市买三类洗化用品，
洗发水（15元），香皂（2元），牙刷（5元）。
要把100元整好花掉，可如有哪些购买结合？
"""

# for x in range(0, 100):
#     for y in range(0, 100):
#         for z in range(0, 100):
#             if 15*x + 2*y + 5*z == 100:
#                 print("洗发水有%d瓶，香皂有%d个，牙刷有%d个" % (x, y, z))
#                 break


