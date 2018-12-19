

# 0.写一个匿名函数，判断指定的年是否是闰年

leap_year = lambda year: True if year % 400 == 0 or (year % 4 == 0 and year % 100 == 0) else False
print(leap_year(2000))
print(leap_year(2009))

# 1.写一个函数将一个指定的列表中的元素逆序
# ( 如[1, 2, 3] -> [3, 2, 1])(注意:不要使列表自带的逆序函数)


def list_reverse(list1):
    return list1[::-1]


print(list_reverse([1, 2, 3]))

# 2.写一个函数，提取出字符串中所有奇数位上的字符


def extract(str1):
    str2 = ""
    list1 = list(str1)
    for i in range(len(list1)):
        if i % 2 == 1:
            str2 = str2 + list1[i]
    return str2


print(extract("vhhj123jklove"))

# 3.写一个函数，统计指定列表中指定元素的个数(不用列表自带的count方法)


def count1(list1,num):
    time1 = 0
    for i in list1:
        if i == num:
            time1 += 1
    return time1


print(count1([1, 56, 5, "d", "f", "g", "d", 5], 5))



# 4.写一个函数，获取指定列表中指定元素的下标(如果指定元素有多个，将每个元素的下标都返回


def subscript(list1, value):
    str1 = ""
    for i in range(len(list1)):
        if list1[i] == value:
            str1 += (",%s" % str(i))
    return str1

print(subscript(["a","c","e","c",1, 2, 6], "c"))


# 5.写一个函数，能够将一个字典中的键值对添加到另外一个字典中(不使用字典自带的update方法)


def add_kv(dict1, dict2):
    for key in dict1:
        dict2[key] = dict1[key]
    return dict2


print(add_kv({"a": 10, "b": 20}, {"c": 100}))


# 6.写一个函数，能够将指定字符串中的所有的小写字母转换成大写字母；
# 所有的大写字母转换成小写字母(不能使用字符串相关方法)


def transform(str1):
    str2 = ""
    for i in str1:
        if "a" <= i <= "z":
            i = chr(ord(i)-32)
            str2 += i
        elif "A" <= i <= "Z":
            i = chr(ord(i)+32)
            str2 += i
        else:
            str2 += i
    return str2


print(transform("4ds556d4AAS4"))


# 7.写一个函数，能够将指定字符串中的指定子串替换成指定的其他子串(不能使用字符串的replace方法)
# 例如: func1('abcdaxyz', 'a', '\\') - 返回: '\\bcd\\xyz'

def replace1(str1, str2, str3):
    str4 = ""
    for i in str1:
        if i == str2:
            i = str3
            str4 += i
        else:
            str4 += i
    return str4


print(replace1('abcdaxyz', 'a', r'\\'))



# 8.实现一个输入自己的items方法，可以将自定的字典转换成列表。
# 列表中的元素是小的列表，里面是key和value (不能使用字典的items方法)
# 例如:{'a':1, 'b':2} 转换成 [['a', 1], ['b', 2]]

def items1(dict1):
    list1 = []
    for key in dict1:
        list1.append([key, dict1[key]])
    return list1


print(items1({'a': 1, 'b': 2}))







print(ord("r"))
print(ord("R"))


