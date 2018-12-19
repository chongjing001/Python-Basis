




"""
json支持的数据类型
数字类型 - 包含所有数字
字符串 - 使用双引号括起来的字符串
布尔 - true和false
数组 - 相当于python中的列表，使用中括号括起来，括号里是json支持的任意数据
      例：["abc",123,true]
字典 - 相当于python中的字典，使用{}括起来，括号里是键值对，
键一般是字符串，值是任意类型数据
特殊值 - null(相当于None)




"""

import json
"""
3.python中有一个内置的模块用来支持对json数据的处理：json
a.将json数据转换成Python数据
json.loads(字符串) - 将json格式数据转换python对应的数据
注意：这儿的字符串内容必须是json格式的数据
json         python
数字  --->   整型/浮点型
布尔         布尔（true->True,false->False）
数组         列表
字典         字典
null         None
b.将Python数据转换成json数据
json.dumps(数据) - 将python数据转换成内容符合json格式的字符串
注意：最终结果是字符串
python             json
int/float          数字
字符串              字符串（单引号会变双引号）
布尔                布尔（True->true)
列表                数组
字典                字典

"""
json.loads('100')
json.loads('"abc"')

js3 = json.loads('true')
print(js3)

js4 = json.loads('[100,"abc",true]')
print(js4)

js5 = json.loads('{"name":["abc",10,true],"str1":true}')
print(js5)

with open("date.json", "r", encoding="utf-8") as f:
    js6 = f.read()

# 转换
dict1 = json.loads(js6)
print(dict1["data"][2]["age"])


js1 = json.dumps(True)
print(js1)


# 练习：添加学生信息，保存json，

stu_list = []
while True:
    name = input("姓名：")
    with open("message.json", "r", encoding="utf-8") as f:
        message = f.read()
    js2 = json.loads(message)
    for i in js2:
        if i["name"] == name:
            print("%s姓名已存在" % name)
            name = input("请重新输入姓名：")
    age = input("年龄：")
    phone = input("电话：")
    stu_dict = {"name": name,
                "age": age,
                "phone": phone}
    stu_list.append(stu_dict)
    js1 = json.dumps(stu_list)
    with open("message.json", "w", encoding="utf-8") as f:
        f.write(js1)
    print("添加成功")
    str2 = input("是否继续添加\nyes/no")
    if str2 == "no":
        print("退出成功")
        break


"""
3.json文件操作相关方法
load(文件对象) - 将文件对象的数据读出来，并且转换成python对应的数据
               （文件对象中的内容是json格式的数据）
dump(数据、文件对象) - 将python数据转换成json格式的字符串，在写入文件对象中

"""
# with open("date", encoding="utf-8") as f:
#     content = f.read()
# print(content, type(content))
# js7 = json.loads(content)
# print(js7)

def my_load(file):
    with open(file,encoding="utf-8") as f:
        content = f.read()
    return json.loads(content)

print(my_load("date"))