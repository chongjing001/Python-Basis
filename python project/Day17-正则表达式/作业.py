import re

"""
1. 写一个正则表达式判断一个字符串是否是ip地址
规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255
255.189.10.37   正确
256.189.89.9    错误
"""

re_ip = r"((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))"
print(re.fullmatch(re_ip, "251.156.15.9"))

"""
2. 计算一个字符串中所有的数字的和  
例如：字符串是：‘hello90abc 78sjh12.5’ 结果是90+78+12.5 = 180.5
"""


def num_sum(str1):
    sum1 = 0
    re_sum = r"\D(\d+\.?\d*)"
    result = re.findall(re_sum, str1)
    for i in result:
        sum1 += float(i)
    return sum1


print(num_sum("hello90abc 78sjh12.5"))

def find_num(string):
    comp = re.compile(r"-?[1-9]+\.?\d*")
    list_str = comp.findall(string)
    list_num = []
    for i in list_str:
        i = float(i)
        list_num.append(i)
    return sum(list_num)


print(find_num("hello90abc 78sjh12.5"))


# 3. 验证输入的内容只能是汉字


def input_chinese():
    re_str1 = "[\u4e00-\u9fa5]+"
    str1 = input("请输入中文")
    if re.fullmatch(re_str1, str1):
        print("输入成功")
    else:
        print("失败！！！请从新输入")


# input_chinese()

# 电话号码的验证
# "XXX-XXXXXXX"、"XXXX-XXXXXXXX"、"XXX-XXXXXXX"、"XXX-XXXXXXXX"、"XXXXXXX"和"XXXXXXXX
def review_phone_number(number):
    re_number = "^(\(\d{3,4}-)|\d{3.4}-)?\d{7,8}$ "
    if re.fullmatch(re_number, number):
        return True
    else:
        return False


def review_Id_card(id_card):
    re_card = "^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$)|(^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}$"
    if re.fullmatch(re_card, id_card):
        return True
    else:
        return False


re_str = "aaa??b"
print(re.fullmatch(re_str, "aaaab"))



