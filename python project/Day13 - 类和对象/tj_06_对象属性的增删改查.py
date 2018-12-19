

"""



"""


print("\033[5;35;m")
class Dog:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type


dog1 = Dog("旺达","蓝色","二哈")

"""
1.查
a.对象.属性    -  属性不存在的时候会报错
b.getattr(对象，属性名，默认值)  - 当属性不存在的时候，如果设置了默认值，
                              程序不崩溃，而是返回默认值
"""
print(dog1.color)
print(getattr(dog1, "color"))
print(getattr(dog1, "name1", "caca"))
"""
2.增、改
对象.属性 = 值
setattr（对象，属性名，值）
注意：属性存在的时候，对应的功能是修改属性的值，当属性不存在的时候是添加属性

"""


dog1.name = "大白"
print(dog1.name)

dog1.sex = "母"
print(dog1.sex)

setattr(dog1, "name", "hahha")
print(dog1.name)

setattr(dog1, "name2", "huhuh")
print(dog1.name2)

"""
3.删除
del 对象.属性
delattr(对象，属性名)
"""

del dog1.name2

delattr(dog1, "name")


"""
注意：对想属性的增删改查，都是针对指定的对象，不会影响其他对象
"""





"""
约束类的对象属性（只能有括号内的属性，其他地方不能添加属性）
__slots__ = (属性1，属性2，...)

"""




