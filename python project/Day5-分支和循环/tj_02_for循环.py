
"""
什么时候用循环：某个操作需要重复执行，就考虑使用循环
"""
# 1.for 循环
"""
a.语法：
for 变量 in 序列：
    循环体
b.for - 关键字
变量 - 变量名，（满足变量命名规范）
in - 关键字
序列 - 可以是字符串、列表、元组、字典、集合、迭代器、range
循环体 - 和for保持一个缩进的一条或者多条语句（需要重复执行的代码）
c.执行过程：
让变量取序列中取值，一个一个的取，取完为止；每取一个值，依次执行循环体
for循环中，序列中值的个数，确定了循环的次数

d.如果for后面取到的值，在循环体里面不使用，那么这个变量命令的时候，用一个_来命名
"""

for i in "abc":
    print(i)

# 2.range
"""
range(n) - 产生数字序列，序列中的内容是0~ n-1（结果是序列）

range(m,n) - 产生数字序列，序列中的内容是m~ n-1
range(m,n,step) - 产生数字序列，从m开始，每次增加step，直到n-1为止
range一般用在：
            a.需要产生指定范围的数字序列
            b.单纯的控制for循环的次数
"""
for i in range(5):
    print(i)
print("~"*20)
for i in range(10, 15):
    print(i)

for i in range(20, 30, 2):
    print(i)

sum_i = 0  # 保存和
for i in range(1, 101):
    sum_i += i
print(sum_i)

sum1 = 0
for num in range(101):
    if num & 1 == 0:
        sum1 += num

print(sum1)

sum2 = 0
for num in range(2, 101, 2):
    sum2 += num
print(sum2)

str1 = "sd454df5sd5f45dfd4f5dfdg"

count = 0
for char in str1:
    # print(i)
    if "0" <= char <= "9":
        count += 1
print("数字个数：%d" % count)





