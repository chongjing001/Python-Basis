

# 1.while循环
"""
a.语法：
while 条件语句:
    循环体

b. 说明:
while - 关键字
条件语句 - 有结果的表达式（除了赋值语句,一般的表达式都行）

c.执行过程：
先判断条件语句是否为True，为True就执行循环体；
执行完循环体再判断条件语句是否为True，为True就执行循环体；
执行完循环体再判断条件语句是否为True，为True就执行循环体；
...
直到判断条件结果为False，整个循环结束
"""

num = 1
result = 1
while num <= 10:
     result *= num
     num += 1
print(result)

str1 = "abc123"
num = 0
while num < len(str1):
    print(str1[num])
    num += 1

# for循环和while循环的选择
"""
使用for循环：
a. 获取序列中的元素（值）
b. 循环次数确定

while循环：
a. 死循环
b. 循环次数不确定
"""

while True:
    index = input("请输入：")
    if index == "0":
        print("~~~~~~~~~")
        break
