

"""
1. 编写一个函数，求1+2+3+...+N
2. 编写一个函数，求多个数中的最大值
3. 编写一个函数，实现摇色子的功能，打印n个色子的点数和
4. 编写一个函数，交换指定字典的key和value。
例例如:{'a':1, 'b':2, 'c':3} ---> {1:'a', 2:'b', 3:'c'}
5. 编写一个函数，三个数中的最大值
6. 编写一个函数，提取指定字符串中的所有的字母，
然后拼接在一起后打印出来 例如：'12a&bc12d--' ---> 打印'abcd'
7. 写一个函数，求多个数的平均值
8. 写一个函数，默认求10的阶层，也可以求其他数的阶层
9. 写一个函数，可以对多个数进行不同的运算
例例如:  operation('+', 1, 2, 3) ---> 求 1+2+3的结果
        operation('-', 10, 9) ---> 求 10-9的结果
        operation('*', 2, 4, 8, 10) ---> 求 2*4*8*10的结果
"""


# 1
def sum_n(n):
    """
求1+2+3+...+n的值
    :param n: int
    """
    sum1 = 0
    for num in range(n+1):
        sum1 += num
    print(sum1)


sum_n(10)

# 2
def max_n():
    """
求多个数中的最大值
    """
    list1 = []
    while True:
        nums = input("请输入数字，输入end结束")
        if nums != "end":
            list1.append(int(nums))
        else:
            print(max(list1))
            break

# max_n()

# 3
def sice_sum():
    """
实现摇色子的功能，打印n个色子的点数和
    """
    import random
    list1 = []
    while True:
        str1 = input("回车掷骰子，end结束投骰子，并返回掷出骰子的点数和")
        if str1 != "end":
            num = random.randint(1, 7)
            print(num)
            list1.append(num)
        else:
            print(sum(list1))
            break

# sice_sum()

# 4
def swop_kv2(dict1):
    dict2 = {v: k for k, v in dict1.items()}
    print(dict2)


def swop_kv(dict1):
    dict2 = {}
    for i in dict1:
        dict2[dict1[i]] = i
        # dict2.setdefault(dict1[i], i)  也行
    print(dict2)

swop_kv2({'a': 1, 'b': 2, 'c': 3})

swop_kv({'a': 1, 'b': 2, 'c': 3})

# 5
def max3(x, y, z):
    """
三个数中的最大值
    :param x: int
    :param y: int
    :param z: int
    """
    list1 = [x, y, z]
    print(max(list1))

max3(3, 6, 9)

# 6.
def extract_letter(str1):
    str2 = ""
    for i in str1:
        if i.isalpha():
            str2 += i
    print(str2)
extract_letter("45sd44d4s4fds4d8s")

# 7.
def avg_n(n):
    """
求多个数的平均值
    :param n: int
    """
    print(sum(n)/len(n))

avg_n([3, 6, 9, 8, 5, 1])

# 8.
def stratum_n(n):
    """
数的阶层
    :param n:int
    """
    nums = 1
    for i in range(1, n+1):
        nums *= i
    print(nums)
stratum_n(10)
stratum_n(5)

# 9
# def operation(operator, num1=0, num2=0, num3=0, num4=0):
#     """
# 可以对多个数进行不同的运算
#     :param operator: 运算符
#     :param num1: int
#     :param num2: int
#     :param num3: int
#     :param num4: int
#     """
#     if operator == "+":
#         print(num1+num2+num3+num4)
#     elif operator == "-":
#         print(num1-num2-num3-num4)
#     elif operator == "*":
#         print(num1*num2*num3*num4)



def operation(operator, *nums):
    if operator == "+":
        print(sum(nums))
    elif operator == "-":
        list1 = list(nums)
        sub = list1[0]
        for i in range(1, len(list1)):
            sub -= list1[1]
        print(sub)
    elif operator == "*":
        nums1 = 1
        for i in nums:
            nums1 *= i
        print(nums1)




operation("+", 5, 9, 10)
operation("-", 45, 23)
operation("*", 2, 4, 8, 10)




