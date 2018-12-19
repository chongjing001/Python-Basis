"""
1.声明⼀个电脑类: 属性:品牌、颜⾊、内存⼤小 方法:打游戏、写代码、看视频
a.创建电脑类的对象，然后通过对象点的方式获取、修改、添加和删除它的属性
b.通过attr相关方法去获取、修改、添加和删除它的属性
"""


class Computer:
    def __init__(self, brand, color, storage):
        self.brand = brand
        self.color = color
        self.storage = storage

    def play_game(self):
        return "玩游戏"

    def coding(self):
        return "写代码"

    def watch_video(self):
        return "看视频"


computer = Computer("ASUS", "黑色", "8G")
print(computer.brand)
print(getattr(computer, "brand"))
computer.storage = "16G"
print(computer.storage)
setattr(computer, "storage", "32G")
print(computer.storage)
computer.screen = "15.7寸"
print(computer.screen)

del computer.screen
delattr(computer, "storage")

"""
2.声明⼀个人的类和狗的类:  
狗的属性:名字、颜色、年年龄   
狗的方法:叫唤     
人的属性:名字、年龄、狗   
人的方法:遛狗    
a.创建人的对象小明，让他拥有一条狗大黄，然后让小明去遛大黄
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dog = None

    def walk_dog(self):
        if self.dog:
            print("%s有一条狗叫%s" % (self.name, self.dog.name))
            print("%s经常遛%s" % (self.name, self.dog.name))
        else:
            print("还没有狗")


class Dog:
    def __init__(self, name="", color="", age=0):
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        print("%s汪汪汪~~" % self.name)


xiaoming = Person("小明", 18)
xiaoming.dog = Dog("大黄", "黄", 3)
xiaoming.walk_dog()

# 3.声明⼀一个圆类:
import math


class Circle:
    def __init__(self, r):
        self.r = r

    def eara(self):
        print("面积：%s" % (2 * math.pi * self.r ** 2))

    def girth(self):
        print("周长：%s" % (2 * math.pi * self.r))


circle = Circle(10)
circle.eara()
circle.girth()

"""
4.创建⼀一个学⽣生类:  
属性:姓名，年龄，学号   
方法:答到，展示学⽣生信息 
"""


class Student:
    def __init__(self, name, age, stu_id):
        self.name = name
        self.age = age
        self.stu_id = stu_id

    def introduce(self):
        print("我叫%s,我今年%s，学号：%s" % (self.name, self.age, self.stu_id))


xiaoli = Student("小李", 15, "050112536")
xiaoli.introduce()

"""
创建⼀一个班级类:   
属性:学生，班级名   
方法:添加学生，删除学生，点名, 求班上学生的平均年龄
"""


class Class:
    class_name = "16"

    def __init__(self, stu_dict={}):
        self.stu_dict = stu_dict

    def add_student(self, name, age):
        self.stu_dict[name] = age
        print("添加学生%s成功" % name)

    def del_student(self, name):
        if name in self.stu_dict:
            del self.stu_dict[name]
            print("删除学生%s成功" % name)
        else:
            print("没有学生%s" % name)

    def call_name(self, name):
        name1 = (i for i in self.stu_dict if i == name)
        print("下面开始点名 %s" % next(name1))

    def avg_age(self):
        sum1 = 0
        count = 0
        for i in self.stu_dict:
            sum1 += self.stu_dict[i]
            count += 1
        print("班级平均年龄:", int(sum1 / count))


class_ = Class()
class_.add_student("小李", 15)
class_.add_student("小明", 18)
class_.add_student("老王", 20)

class_.call_name("小李")
class_.avg_age()

class_.del_student("老王")
