

"""
抛出异常：主动让程序出现异常

语法：
raise 错误类型 - 程序执行到raise的时候直接抛出异常

注意：错误类型必须是一个类，并且这个类是Except的子类

"""


while True:
    age = int(input("请输入年龄"))
    if age < 0 or age > 100:
        raise ValueError
    print("**")


