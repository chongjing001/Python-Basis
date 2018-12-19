


"""
匿名函数还是函数，除了声明的语法以外，函数其他的语法匿名函数都支持
匿名函数的声明
函数名 = lambda 参数列表：返回值

说明：
函数名 - 变量名
lambda - 关键字
参数列表 - 和普通函数的参数列表要求一样，但至少要有一个参数
返回值： - 相当于普通函数return关键字后面的表达式
注意：匿名函数中冒号后面的语句属于函数体，在声明的时候不会执行
匿名函数调用和普通函数一样
"""

# 用匿名函数求两个数的和
sum1 = lambda num1, num2: num1+num2
result = sum1(5, 6)
print(result)

# 写一个匿名函数，求两个数的和
sum2 = lambda *args: max(args)
print(sum2(5, 9))


# 补充：python中的三元运算符
"""
C中语法： 条件语句?值1:值2 - 条件语句为True，整个表达式的结果是值1，否则为值2


python中语法：
值1 if 条件语句 else 值2 - 条件语句为True，整个表达式的结果是值1，否则为值2
"""
# 匿名函数
values = lambda dict1, key: dict1[key]
print(values({"k": 100}, "k"))