

"""
在子类中添加方法
父类不能调用子类的

重写父类
1.完全重写 - 覆盖父类
2.部分重写 super().父类的方法 加上子类需要实现的功能

注意：子类可以通过super()去调用父类的方法
super(类，对象) - 获取对象中父类的部分（要求对象是这个指定的类的对象）
静态方法中不支持super()
c.类中方法调用过程
通过对象或者类地哦啊用方法的时候，先看前类中是否声明过这个方法，
如果声明过就直接地哦啊用当前类对应的...

"""



class Person:

    def person(self):
        print("吃喝拉撒睡")

class Student(Person):

    def __init__(self, name):
        self.name = name

    def study(self):

        print("%s在学习" % self.name)

s1 = Student("小明")
s1.person()
s1.study()

"""
1.添加类的字段
直接在子类中添加新的字段
2.添加对象属性
类的对象属性是通过继承父类的init方法继承下来的

如果想要在保留父类继承下来的对象属性的前提下，添加新的对象属性
需要在子类的init犯法中，通过super()去调用父类的init方法
"""

# 声明一个动物类，属性：年龄，颜色，类型 要求创建动物对象的时候类型和颜色必须赋值年龄可赋可不赋
# 声明一个猫类，属性：年龄、颜色、类型、爱好 要求创建猫对象的时候，颜色必须赋值，类型不能赋值





class Anmial:
    def __init__(self, color, type, age=1):
        self.color = color
        self.type = type
        self.age = age


a1 = Anmial("黑色", "猫科")

class Cat(Anmial):
    def __init__(self, color, age=2, hobby="耍"):
        super().__init__(color, "猫科", age,)
        self.color = color
        self.hobby = hobby

c1 = Cat("blue")

print(c1.color)
print(c1.type)
























