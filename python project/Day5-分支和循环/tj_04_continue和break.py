
# 1.continue
"""
continue 是一个关键字，只能写在循环中
功能：当循环执行过程中遇到continue，会结束当次循环，直接今日下次循环的判断
    （直接进入下次循环的判断：for循环就是用比那辆取下一个值
                           while就是直接判断条件语句是否为True）

"""

for i in range(0, 10):
    if i & 1 == 0:
        continue
    print("我是奇数：%d" % i)





# 2.break

"""
a.语法:
while 条件语句:
    循环
else:
    代码段
    
for 变量 in 序列:
    循环体
else:
    代码段
    
b.执行过程:
else结构不会影响原循环的执行过程。当循环自然死亡的时候，就会执行else后边的代码段。
循环因为遇到break而结束的时候不会执行else后边的代码段
"""

for x in range(10):
    print(x)
    if x == 3:
        break
else:
    print('for循环结束了')
