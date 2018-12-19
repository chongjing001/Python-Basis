




"""
1.迭代器（iter）
迭代器是python中容器类的数据类型，可以同时存储多个数据
取迭代器中的数据只能一个一个取，取出来的数据就不存在了

2.迭代器中数据来源
a.将其他序列转换成迭代器
b.使用生成式、生成器去产生数据

所有序列都能转换成迭代器
"""


# 将数据转化成迭代器
iter1 = iter("sdks")
print(iter1)

iter2 = iter([1, 25, 54])
print(iter2)

iter3 = iter({"name": "装甲师", "age": 500})
print(iter3)

# 获取迭代器中的元素
"""
next(迭代器) - 取出迭代器中第一个元素（已经取出的元素，不能返回）
StopTteration
当迭代器是空的时候，使用next获取云阿苏，会出现StopTteration异常
"""
print(next(iter3))
print(iter3.__next__())

"""
通过for循环取出迭代器中的每个元素。
"""