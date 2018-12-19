


"""
1.异常：
程序执行过程中出现错误，也叫异常

2.异常捕获
让本来会出现异常的位置，不出现异常，而是自己出处理异常出现的情况

a.捕获所有的异常
语法：
try:
    代码段1
except：
    代码段2

b.捕获指定的异常
语法：
try：
   代码段1
except 错误类型名：
   代码段2


c.同时捕获多个异常，对不同的异常做出相同的反应
try:
   代码段1
except （错误类型1、错误类型2、错误类型3...）:
   代码段2
执行过程：执行代码段1，当代码段1中出现了指定的异常，不崩溃，然后执行代码2


d.同时捕获多个异常，对不同异常做出不同反应
try:
    代码段1
except： 错误类型1：
    代码段2
except： 错误类型2：
    代码段3
...





3. finally
try:
   代码段1
except：
   代码段2
finally：
    代码段3
出不出现异常 finally里的代码都会执行




4.什么时候使用异常捕获
可能出现异常，
"""


# 封装一个函数，功能是获取指定文件中的内容（普通文本文件）


def read_file(file):
    with open(file,encoding="utf-8")as f:
        content = f.read()
    return content


try:
    print(read_file("datse"))
except FileNotFoundError:
    print("空文件啊")




