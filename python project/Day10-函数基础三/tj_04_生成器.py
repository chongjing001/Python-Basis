


"""
生成器就是迭代器；迭代器不一定是生成器
带有yield关键字函数的结果
调用带有yield关键字的函数，拿到的结果就是一个生成器
生成器中的元素就是yield关键字后边的值

只要函数体中有yield关键字，调用函数不会再执行函数体获取返回值
而是创建生成器
"""

def func1():
    print("abc")
    yield 123

re = func1()
"""
next(re) - 执行re对应的函数的函数体，将yield关键字后边的值作为结果
当获取生成器的元素的时候，才会执行函数的函数体，执行到yield语句为止
并且将yield后边的值作为返回结果，保存当前执行的位置
获取下一个元素的时候，就从上次结束的位置往下取执行函数
直到函数结束或者到下一个yield为止
如果函数结束了，就出现StopTteration

生成器对应的函数，执行完成遇到yield的次数，决定了生成器能产生的数据个数
"""

print(re)
print(next(re))


def numbers():
    for i in range(101):
        yield i

gener = numbers()

for _ in range(101):
    print(next(gener), end="\t")



def creat_id():
    num = 0
    while True:
        yield "stu" + str(num).zfill(3)
        num += 1

gener_id = creat_id()
for _ in range(11):
    print(next(gener_id))

# 练习：菲薄拉稀数列

def creat_nums():
    num1 = 1
    num2 = 1
    yield num1
    yield num2
    while True:
        number = num1 + num2
        yield number
        num1, num2 = num2, number

gener_numbers = creat_nums()


for _ in range(21):
    print(next(gener_numbers))

