
"""
1.什么是对象属性
a.声明在__init__方法中
b.self.属性值 = 值
c.通过对象使用：对象.属性
语法：
self.变量名 = 值
说明：变量就是属性名，这个变量就是对象属性


2.对象属性的声明
如果属性的值会因为对象不同而不一样，就声明成对象属性
反之就声明类的字段
"""


class Person:
    def __init__(self):
        #   Person类的对象属性
        self.name = "小李"
        self.age = 20

p1 = Person()
print(p1.name, p1.age)



# 创建对象的时候，决定对象属性的值
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0

p2 = Person("老王")
print(p2.name, p2.age)


class Orthogon:
    def __init__(self, length, wide):
        self.length = length
        self.wide = wide
    def area(self):
        return self.length*self.wide

    def girth(self):
        return 2*(self.length+self.wide)



c1 = Orthogon(10,9)
print("矩形  长：%d  宽：%d" % (c1.length, c1.wide))
print(c1.area())
print(c1.girth())



# 练习：声明一个Point类，拥有属性x坐标和y坐标  功能：求两个点之间的距离


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distence(self, other):
        return (((self.x - other.x))**2 + ((self.y - other.y))**2)**0.5

p1 = Point(0, 10)
p2 = Point(3, 14)
print(p1.distence(p2))






