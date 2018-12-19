

"""
类中的方法分为：对象方法，类方法和静态方法

1.类方法
a.在声明前添加@classmethod
b.有默认参数cls,调用的时候不需要传参
  系统会自动将当前调用的类传给cls，类可以做的事，cls都可以做
c.通过类来调用：类.类方法()

2.静态方法
a.在声明前添加@staticmethod
b.没有默认参数
c.通过类来调用：类.类方法()

"""



class Person:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s在吃%s" %(self.name, food))


    @classmethod
    def destory(cls):
        print("人类破坏环境")
        print(cls)
        # 可以用cls创建对象
        p1 = cls("小李")
        p1.eat("大餐")
    @staticmethod
    def animal():
        print("动物世界")

Person.destory()
print(Person)
Person.animal()

"""
实际开发中方法的选择
对象方法：当实现函数的功能需要使用到对象的属性的时候

类方法：实现函数的功能不需要对象的属性，但是需要类的时候

静态方法：实现函数的功能不需要对象的属性，也不需要类的时候

"""


# 练习：数学类  属性：pi   求两个数的和， 求一个圆的面积

import math

class Math:
    pi = math.pi

    @staticmethod
    def sum_num(*args):
        return sum(args)

    @classmethod
    def eara(cls, r):
        return cls.pi*r**2


print("和：", Math.sum_num(5, 8))
print("面积：", Math.eara(5))



