

"""
多继承：让一个类同时继承多个类
两个类的字段和方法都能继承，对象属性只能继承第一个类的对象属性
"""

class Animal:
    num1 = 100
    def __init__(self, name="￣□￣｜｜", age=0, color="y"):
        self.name = name
        self.age = age
        self.color = color
    def show_info(self):
        print("名字：%s 年龄：%d 颜色：%s" % (self.name, self.age, self.color))


class Fly:
    num2 = 200
    def __init__(self, distance=0, speed=0):
        self.distance = distance
        self.speed = speed
    @staticmethod
    def show():
        print("飞")


class Birds(Animal, Fly):
    pass

b1 = Birds()
print(b1.num1, b1.num2)


"""
多态
类的特点：封装、继承、多态

封装：可以对多条数据(属性)和多个功能(方法)进行封装
继承：可以让一个类拥有另一个类属性和方法
多态：有继承就有多态（一个事物的多种形态）
"""
