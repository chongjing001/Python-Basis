

# 1.格式字符串:字符串中通过格式占位符来表示字符串中变化的部分，然后在给占位符赋值
"""
含有格式占位符的字符串 %（占位符对应的值）
说明：格式占位符 - 有固定的写法，可以有多个格式化字符串
      给值遵循一一对应


"""

# 2.常见格式占位符
"""
%d - 整数
%s - 字符串
%.nf - 小数(保留n位小数)
%c - 字符（可以将数字转换成字符）

"""
name = "李四"
age = 99
weight = 100.00

print("%s您好，您的年龄是%d，体重为%.2f" % (name, age, weight))
