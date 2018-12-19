


"""
1.字典不支持+和*

2. in 和not in
判断字典中是否存在指定的key


3.clear
字典.clear（） - 清空字典（删除字典中所有的键值对）

4.copy
字典.copy() - 复制字典中所有的键值对，产生一个新的字典
"""

# 5.fromkeys
"""
dict.fromkeys(序列,值) - 以序列中的元素作为key，值作为所有key对应的默认值，创建一个字典
"""
# 6.keys、values、items
"""
字典.keys() - 获取字典所有的key（返回一个序列，序列中所有的元素就是字典的key）
字典.values() - 获取字典所有的值（返回一个序列，序列中所有的元素就是字典的值）
字典.items() - 获取字典所有的键值对(返回一个序列，序列中的元素是元组，元组元素有两个分别是key和值）

"""
dict1 = {"x": 89, "y": 45, "z": 56}
keys = dict1.keys()
print(keys, type(keys))
values = dict1.values()
print(values, type(values))
print(list(values))
items = dict1.items()
print(items, type(items))
print(list(items), dict(items))

"""
7.setdefault
字典.setdefault(key,value) - 给字典添加键值对（注意：如果key值本来存在，就不会影响字典）
"""
