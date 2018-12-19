

# 变量：在程序中用来保存数据的容器
"""
声明变量（定义）--假的声明
变量名 = 值

说明：
变量名（要求：标识符，不能是关键字）
       规范：遵守PEP8命名规范（名字的所用字母都小写，如果由多个单词组成，单词之间用_隔开）
关于代码规范
http://www.python.org/dev/peps/pep-0008/
谷歌对应中文文档：
http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/

= ： 赋值符号，将等号右边的值负给左边的变量
     值 ： 可以是任何有结果的表达式，例如：100、变量、调用函数表达式

变量必须先声明（赋值）再使用
"""
name1 = "李四"
age = 25
gender = "男"

# 同时声明多个变量
num1 = num2 = num3 = 99
# 注意变量的个数和值的个数要保持一致
x, y, z = 10, 20, 30
# 同一个变量可以存储不同类型的值
num = 100
num = "carry"
num = True
num = [1, 2, 3]

"""
声明变量和给变量赋值的本质
结论：python中所有的变量，存储的都是数据在内存中的地址，内存地址的大小一样
      用一个变量给另一个变量赋值，实质是将变量中的地址赋给另一个变量
      使用变量的时候，是使用变量中对应的值
C中声明变量：
int num = 100
num = 99

python：
num = 100

"""

# 变量的三要素：值、地址和类型
"""
值：变量中存的地址对应的值
地址：变量中存住的地址（id）
类型：变量中存储地址对应值的类型
"""
name1 = "张收纳"
name2 = name1

print(name1)
print(name2)
# id(变量)-获取变量中存储的地址
print(id(name1))
print(id(name2))
