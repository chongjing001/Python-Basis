import random

# python 中的分支结构只有if语句，没有switch
# 1.if语句
"""
a.语法：
if 条件语句：
    代码段
b.说明：
if - 关键字
条件语句 - 任何有结果的表达式（不管是什么类型）
代码段和if保持一个缩进的一条或者多条语句
c.执行过程：
先判断条件语句的结果是否是True，如果是则执行，反之则不执行
注意：如果条件语句的结果不是布尔，会将结果转化为布尔再判断
     赋值语句不能写在if的后面

"""


# 练习：随机产生一个年龄值，如果大于18就打印 成年

age = random.randint(0, 100)
if age >= 18:
    print("成年")
print("你的年龄是%d" % age)

# 2.if-else语句
"""
a.语法：
if 条件语句：
    代码段1
else:
    代码段2
    
b.执行过程：
先判断条件语句是否为True,为True就执行代码段1：否则执行代码段2

"""
# num = input("请输入")
num = 12
# try,except,finally为异常捕获
try:
    if num & 1 == 0:
        print("我是偶数%d" % num)

    elif num & 1 == 1:
        print("你是奇数%d" % num)
except:
    print("非奇非偶吧你{0}".format(num))
finally:
    print("Hello python")

# 3.if - elif - else
"""
语法：
if 条件语句1:
    代码段1
elif 条件语句2:
    代码段2
elif 条件语句3:
    代码段3
...
else:
    代码段n
    
执行过程：
先判断条件语句1是否为True，为True就执行代码段1；
否则，就判断条件语句2是否为True，为True就执行代码段2
否则，就判断条件语句3是否为True，为True就执行代码段3
...
如果全部条件语句都不执行就执行 else
注意：1.后面的条件判断前提是前面的条件不成立
      2.elif根据条件可以有多个，else也可以省略
"""
score = random.randint(40, 100)
print("你的考试成绩：%d" % score)
print("你的综合测评：", end="")
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("留级")

# 4.if 的嵌套
"""
可以在if ,else后面的代码段中，都可以再写其他的if语句
"""
number = random.randint(0, 100)
if number & 1 == 0:
    print("偶数：%d" % number)
    if number % 4 == 0:
        print("4的倍数:%d" % number)
else:
    print("你是奇数：%d" % number)


# 练习：输入一个字符串，判断是否第一个字符是字母，如果是 打印“一字母开头”
#       如果这个字母是大写的，再打印“大写字母”

str1 = input("请输入")
if str1[0].isalpha():
    print("字母开头")
    if str1[0].isupper():
        print("大写字母")
else:
    print(str1)

# 方法2
if "a" <= str1[0] <= "z" or "A" <= str1[0] <= "Z":
    print("以字母开")
    if "A" <= str1[0] <= "Z":
        print("大写字母")
else:
    print(str1)
