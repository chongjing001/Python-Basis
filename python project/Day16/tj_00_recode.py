"""

继承会继承父类所有的属性和方法
添加对象属性：

运算符重载：在类中实现相应的魔法方法让类的对象支持相应的运算符
"""


class Person:
    def __init__(self):
        self.name = "n"


class Student(Person):
    def __init__(self):
        super().__init__()
        self.age = 20


s1 = Student()

print(s1.__dict__)
