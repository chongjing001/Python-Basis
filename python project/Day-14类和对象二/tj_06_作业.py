"""
0.定义一个学生类。有属性：姓名、年龄、成绩（语文，数学，英语)[每课成绩的类型为整数]
方法： a. 获取学生的姓名：getname() b. 获取学生的年龄：getage()
c. 返回3门科目中最高的分数。get_course()

"""


class Grade(object):
    def __init__(self, chinese, math, english):
        self.chinese = chinese
        self.math = math
        self.english = english

    def max_grade(self):
        all_score = self.__dict__.values()
        return max(all_score)


class Student(object):
    def __init__(self, name, age, grade=Grade(0, 0, 0)):
        self.name = name
        self.age = age
        self.grade = grade

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def get_course(self):
        return self.grade.max_grade()


s1 = Student("小李", 18, Grade(89, 82, 69))
print(s1.get_course())
"""
1.建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，
速度等成员变量，并通过不同的构造方法创建实例。至少要求 汽车能够加速 减速 停车。 
再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD等成员变量 覆盖加速 减速的方法
"""

class Auto(object):

    def __init__(self,color,weight=0):
        self.tyre = 4
        self.color = color
        self.weight = weight
        self.speed = 0

    def add_speed(self,speed):
        if self.speed + speed > 240:
            print("警告！！！超速")
            self.speed = 240
            return
        self.speed += speed

    def sub_speed(self,speed):
        if self.speed - speed < 0:
            self.speed = 0
            return
        self.speed -= speed
    def stop(self):
        self.speed = 0

class CarAuto(Auto):
    def __init__(self,air_conditioning = "",CD = 'CD'):
        super().__init__("蓝色",200)
        self.air_conditioning = air_conditioning
        self.CD = CD





"""
2.创建一个名为User 的类，其中包含属性firstname 和lastname ，
还有用户简介通常会存储的其他几个属性。在类User 中定义一个名 为describeuser() 的方法，
它打印用户信息摘要;再定义一个名为greetuser() 的方法，它向用户发出个性化的问候
管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承User类。
添加一个名为privileges 的属性，用于存储一个由字符串
(如"can add post"、"can delete post"、"can ban user"等)组成的列表。
编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin 实例，
并调用这个方法。
"""


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def add_attribute(self, age, gender):
        message = (age, gender)
        return message

    def describe_user(self):
        return "用户信息摘要：姓名：%s" % self.first_name

    def greet_user(self):
        return "Hello", self.first_name, self.last_name


class Admin(User):
    def __init__(self, privileges):
        super().__init__("小李", "老王")
        self.privileges = privileges

    def show_privileges(self):
        return self.privileges


a1 = Admin(["can add post", "can delete post", "can ban user"])
print(a1.show_privileges())

"""
3.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数
"""


class Person:
    count = 0

    @classmethod
    def count_number(cls):
        cls.count += 1
        return cls.count


p1 = Person()
print(p1.count_number())
p2 = Person()
print(p2.count_number())

"""
(尝试)5.写一个类，其功能是：1.解析指定的歌词文件的内容 
2.按时间显示歌词 提示：歌词文件的内容一般是按下面的格式进行存储的。
歌词前面对应的是时间，在对应的时间点可以显示对应的歌词

"""
import json


class Lyric:

    def __init__(self, time):
        self.time = time

    def analysis(self):
        with open("lyricsfile", encoding="utf-8") as f:
            content = f.read()
            return content

    def show_lyric(self):
        pass


l1 = Lyric("lyricsfile")
l1.analysis()

str1 = "[00:00.20]蓝莲花"
j1 = json.dumps(str1)
print(j1)
