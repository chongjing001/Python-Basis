

# 1.查（获取字典的值）
"""
a.获取单个值
字典[key] - 获取字典中key对应的值

字典.get(key) - 获取字典中对应的值（如果key不存在，不会报错）

None 是python中的关键字，表示一个特殊值（没有，空的意思）

"""
zhangsan = {"name": "张三", "age": 89, "gender": "男", "hobby": "play"}
print(zhangsan["name"])

print(zhangsan.get("age"))
print(zhangsan.get("hobby"))
print(zhangsan.get("hahahhahhaha"))

# 直接遍历字典拿到的是字典中所有的key值

for key in zhangsan:
    print(key)

for key, value in zhangsan.items():
    print(key, value)

# 2.增（添加键值对）
"""
字典[key] = 值   - 当key不存在的时候，就是在字典中添加键值对
"""
dict1 = {"a": 1}
dict1["b"] = 2
print(dict1)
"""
字典1.update(序列) - 将字典中的元素转换为键值对，然后再添加到字典1中
当key值有重名的时候，会用序列中键值对对应的值，更新原字典key对应的值
注意：update(序列)要求能够转换成字典的序列。 序列中的元素是自由两个元素的
小序列
"""
dict3 = {'a': 1, 'b': 2, "c": 3}
dict3.update({'a': 10, 'b': 20})
print(dict3)

# 3.改（修改key对应的值）
"""
字典[key] = 值  - 当key存在的时候，就是修改key对应的值
"""

# 4.删（删除键值对）
"""
a.del 字典[key] - 删除字典中key值对应的键值对
b.字典.pop(key) - 取出字典中key对应的值(删除整个键值对)
   字典.popitem() - 取出“最后”一个键值对，一元组的形式返回
   字典popitem()方法作用是：随机返回并删除字典中的一对键和值（项）。
   为什么是随机删除呢？因为字典是无序的，没有所谓的“最后一项”或是其它顺序。
   在工作时如果遇到需要逐一删除项的工作，用popitem()方法效率很高
"""

