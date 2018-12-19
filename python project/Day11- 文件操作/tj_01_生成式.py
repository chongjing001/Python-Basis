

"""
迭代器：容器，可以同时存储多个数据，取的时候只能一个一个取，
        并且取出的不能返回
生成器：就是迭代器，数据是通过调用函数，获取yield后面的值而产生的
       数据会在获取的时候产生
调用一个yield关键的函数，就是创建一个生产器
"""


# 生成式
"""
格式一：结果是一个生成器（迭代器）
(表达式 for 变量 in 序列) --> 展开：
                            def  func():
                                 for 变量 in 序列:
                                     yeild 表达式
注意：表达式的结果就是每次循环生成器产生的数据

格式2：
(表达式 for 变量 in 序列 if 条件语句)
----> 展开：
def func1():
    for 变量 in 序列:
       if 条件语句:
         yeild 表达式





"""

gen1 = (10 for i in range(5))
print(gen1)
print(next(gen1))

gen2 = (i for i in range(5))
for _ in range(5):
    print(next(gen2))

gen3 = (i for i in range(10) if i % 2)
for _ in range(5):
    print(next(gen3))
list1 = list(i for i in range(10) if i % 2)
print(list1)



# 交换字典的键值对

dict1 = {"a": 1, "b": 2, "c": 3}

dict2 = dict((value, key) for key, value in dict1.items())
print(dict2)














