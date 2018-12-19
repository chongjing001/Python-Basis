

print("\033[3;36;m")
"""
1.类的字段
声明在类中，函数外面的变量
类的字段需要通过类来使用： 类名.字段 - 类中外调用方式都一样
不会因为对象不同而不一样


2.内置类属性
声明类饿时候，类中已经声明好1的属性（包含类的字段和类的对象）

a. __name__ - 获取类的名字（字符串）
b. __class__ - 获取对象对象的类（结果是一个类，原来类能做它都能做）

"""


class Dog:
    """够累"""
    type = "犬科"

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self, food):
        print("%s在吃%s" % (self.name, food))

    @classmethod
    def shot(cls):
        print("汪汪汪~~")

    @staticmethod
    def bite():
        print("狗在跑")


dog1 = Dog("萧何", 3, "yello")


class_name = Dog.__name__
print(class_name)
print(Dog.__class__)
print(dog1.__class__)
print(Dog)
# 获取对象对应的类名
print(dog1.__class__.__name__)


"""
类.__dict__ - 获取当前类的所有的类的字段及其对应的值
对象.__dict__ - 将当前对象及其对应的值准换成字典，key是属性，value是值
"""
print(Dog.__dict__)
print(dog1.__dict__)

"""
__base__ - 获取当前类的父类(以元组的形式返回)
类.__base__
"""
print(Dog.__bases__)

"""
类.__module__  - 获取当前类所在的模块名
"""
print(Dog.__module__)
print(int.__module__)
"""
类.__doc__  - 获取类的说明文档
"""
print(Dog.__doc__)








