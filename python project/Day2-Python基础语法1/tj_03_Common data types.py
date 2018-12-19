# python 常用数据类型
# 整型、浮点型、布尔、字符串、列表、元组、字典、集合、函数
# 1.常量
"""
整型：整数（10,100...）
浮点型：带小数点的数(-1.3,2.0 ...)
布尔：True,False
字符串：两个单引号或双引号的内容("sjdbj45sd45祭祀等级")
列表：[内容1,内容2...]
元组：(内容1,内容2...)
字典：{键：值}   例： zhangsan = {name:"张三"}
"""
# 2.数字相关的类型
"""
整型：所有整数，python3.x中整型----> int
浮点型：所有小数---->float
       支持科学计数法 例：2e4 = 2*(10**4)
布尔：只有True和False   -----> bool
      True:1   False:0
复数(虚数)：所有虚数(实部+虚部)  ---->complex
          形如z=a+bi的数称为复数（complex number)，其中规定i为虚数单位
"""

print(2e4)
print(2e-4)

# 3.type函数：获取数据对应的类型
print(type(120))
print(type(True))

# 4.isinstance函数：判断xx是否为xx
print(isinstance(100, int))

# 5.类型的强制转换
"""
类型名(被转换的数据)
任何类型的数据都可以转换成bool
复数不能转换为整型和浮点型
     
"""
print(int(12.54321))
print(float(12))
print(bool(20))
print(bool(-20))
# 只有0或None会转换为False
print(bool(0))
print(bool(None))
print(complex(2))
print(complex(True))
print(complex(False))


