



"""
1.变量的作用域
变量在程序中能够使用的范围

2.全局变量
声明在函数或者类外部的变量都是全局变量
全局变量的作用域是从声明开始到整个py文件结束，任何位置都可以使用
(从声明开始到文件结束)

3.局部变量
声明在函数或者类内部的变量都是全局变量
从声明开始到函数结束


4.global


5.nonlocal 关键字只能在函数中使用
当需要在局部的局部中修改局部变量的值，就使用nonlocal

"""

functions = []
for x in range(5):
    def func1(a):
        return a*x
    functions.append(func1)
t1 = functions[0]
t2 = functions[2]
print(t1(2))
print(t2(2))