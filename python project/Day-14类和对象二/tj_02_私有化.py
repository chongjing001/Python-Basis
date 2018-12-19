

"""
1.私有化
在类中，可以通过在属性名前，或者方法名前加__
不能再类的外部使用
注意：不能以__结尾

2.私有化原理
python中没有真正意义上的私有化，不能从访问权限上控制属性和方法的使用
可以通过 _类名__属性名访问
"""


class Person:

    num = 66

    def __init__(self):
        self.__name = "小李"

    def show_message(self):
        print("名字：%s" % self.__name)


p1 = Person()

print(p1._Person__name)


