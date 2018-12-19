# 1.注释
# 程序中中专门解释说明的文字，不参与代码执行
# 单行注释：在说明性文字前加 #号
# 多行注释:
'''
内容
或者““”内容“”“也行，但一般使用三个双引号
'''
# 2.标识符
# 作用：命名（变量、函数、类...）
"""
要求：由数字、字母或者下划线，但数字不能用于开头
注意：在python3.x ，标识符中可以包含非ASCII码字符（中文、日语、韩语、拉丁文...）
      但在实际开发时，不推荐使用
"""
name = "张三"
age = 40
gender = "男"
# zhangsan = [name,age,gender]
# print(zhangsan)

# 3.行与缩进
"""
python中有严格要求
同一级代码缩进必须一致
"""

if 100 > 10:
    print("True")

# 分行显示：一句代码很长，需要多行显示，在需要换行的代码前加\
print("41564654654564+\
564654564565545+43545+\
6465145614561+4561561561564545")
# 注意不能将变量名或者数据拆开
# 列表、元组、字典、集合的字面量，可以直接运行，不用加\
list = [12,
        "4s15d",
        78,
        "李四"
]
# 5.一行显示多行语句
print("Hello World"); print("Hello Python")

# 6.关键字
"""
python语言已经占用的标识符
['False', 'None', 'True', 'and', 'as', 'assert',
 'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
# 导入关键字模块
import keyword
# 打印python中关键字
print(keyword.kwlist)

# 7.print函数和input函数
"""
print:打印函数,默认会换行，
可以自己封装函数（print(内容,end="换行标志")）
               print(内容,sep="分割标志")
可以打印多个内容print(内容1,内容2,...)
input：接收控制台输入的函数
程序执行到input会停下来，等待用户输入为止
input("提示信息")
"""
print(1, 2, 3, 4)
print("张三", end="*没换行打*")
print("李四")
print("换行了")
print("张三","李四", sep="|没分打|")
print("李四")
print("分了")
your_name = input("请输入您的姓名")
print(your_name)
