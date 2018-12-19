

"""
python中，声明函数其实就是声明一个类型是function的变量，函数名就是变量名

函数名作为变量除了可以用来调用函数获取返回值，

"""
# 声明类型是int类型的变量






"""

将变量作为列表的元素或者字典的值

"""


"""
将函数1作为实参，传递给函数2，函数2就是一个高阶函数
"""


# sort
"""
def sort(self, key=None, reverse=False)
key - 确定排序的时候以什么值为标准来排序（默认以列表元素大小为标准排序）
      需要传一个函数（函数需要一个参数和一个返回值，参数是指列表的一个元素）
reverse - 是否降序排序，需要一个bool值
"""


o = lambda x: x[1]
print(max([("a", 100), ("b", 20), ("c", 10)], key=o))


# 变量作为函数的返回值



"""
返回值是函数的函数，也叫高阶函数（返回值高阶函数）
"""

def get_operator(str1):
    """
    多种运算
    :param str1: 运算符
    :return: 求差函数
    """
    if str1 == "-":
        def sub(*args):
            num1 = args[0]
            for i in range(1, len(args)):
                num1 -= args[i]
            return num1

    return sub


a = get_operator("-")
print(a(10, 5, 3))
print(get_operator("-")(100, 20, 60))
















