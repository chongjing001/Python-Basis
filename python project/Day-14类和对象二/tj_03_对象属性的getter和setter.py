



"""
1.getter和setter
希望在获取对象属性之前要做点其他事，就给这个属性添加getter；
希望在给对象属性赋值之前要做点其他事，就给这个属性添加setter

2.添加getter
a.属性命名时，属性名前加一个_
b.声明一个函数，函数名字是属性名（不需要下划线），不需要额外参数
  并且函数前需要@property修饰，这个函数的返回值就是获取属性的结果
c.当需要获取属性的时候通过 对象.不带下划线的属性  例：对象.age

3.添加setter
想要给对象属性添加setter，必须先给它添加getter
b.声明一个函数，函数的名字是属性名（不要下划线）
  需要一个额外参数，不用返回值，并且函数前使用@getter名.setter修饰
例：
@age.setter
def age(self,value):
    ...
   self._age = value
当需要给属性赋值的时候，通过对象.不带下划线的属性来赋值
例： 对象.age = 100
"""

class Person:
    def __init__(self, name = "小王"):
        self.name = name
        self._age = 5
        self.gender = "男"

    @property
    def age(self):
        if self._age < 1:
            return "婴儿"
        elif self._age < 18:
            return "未成年"
        elif self._age < 60:
            return "壮年"
        elif self._age < 199:
            return "大爷"
        else:
            return "神仙"
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print("年龄必须是整数")
            raise ValueError
        if not (0 <= value <= 200):
            print("年龄超出范围")

        self._age = value




p1 = Person()
print(p1.age)
p1._age = 100
print(p1.age)

# 赋值
p1.age = 200
print(p1.age)


# 声明一个时间类，属性 时间（秒的形式），不断地输入时间，以“XX:xx形式输入”
# 输入多少个时间就保存多少个时间对象，直到end为止

s = "15:456"


class Time:

    def __init__(self):
        self._second = "0"

    @property
    def second(self):
        list1 = self._second.split(":")
        num1 = int(list1[0]) * 60
        num2 = int(list1[1])
        return num1 + num2



# time_list = []
# while True:
#     t1 = Time()
#     t1._second = input("请输入时间，我能能将它转为秒数 例如：10:20 --> 620")
#     if t1._second != "end":
#         print(t1.second)
#         time_list.append(t1)
#     else:
#         print(time_list)
#         break



"""
补充：打印自己声明的类的对象的时候，默认打印是：<模块名.类名 object at 对象地址>
如果不需要以默认的方式打印，可以用 __repr__魔法函数修改

该函数的返回值是字符串
__repr__
"""



class Student:

    def __repr__(self):
        # return ">>"+self.__class__.__module__+"."+self.__class__.__name__+"  object at" + str(hex(id(self)))+"<<"
        return str(self.__dict__)[1:-1]
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("li",26)
print(s1)
