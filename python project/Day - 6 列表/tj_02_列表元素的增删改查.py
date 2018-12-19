


# 查（获取列表的元素）
"""
列表[下标] - 获取指定下标对应的元素

列表一旦确定，列表中每一个元素都对应一个下标；
下标范围：0~列表长度-1； -1~列表长度
下标不能越界



"""

# 增（增加元素）
"""
a.列表.append(元素) - 在制定列表的最后添加指定的元素
"""
# list1 = []
# while True:
#     num = input("请输入成绩")
#     if num != "end":
#         list1.append(num)
#     else:
#         print(list1)
#         break
#
# score = input("请输入成绩")
# scores = []
# while score != "end":
#     scores.append(score)
#     score = input("请输入成绩")
# print(scores)

# 列表
"""
列表.insert(下标，元素) - 在指定的下标前插入指定的元素
遍历列表（将列表中的元素一个一个取出来）
方法一：
for item in 列表:
    print(item)
方法二：
通过遍历下标获取列表元素
for i in range(len(列表)):
    print(列表[i])


"""

list1 = [1, 7, 34, 67, 100]
num = int(input("请输入数字"))
list1.append(num)
list1.sort()
print(list1)

# 错误
# list1 = [1, 7, 34, 67, 100]
# num = int(input("请输入数字"))
# list1.append(num)
# list2 = [1]
# for i in list1:
#     if i > list2[-1]:
#         list2.append(i)
#     elif i < list2[0]:
#         list2.insert(0, i)
# print(list2)

# 3.删除（删除列表元素）
"""
a.del 列表[下标] - 删除列表中指定对应的元素
del - 关键字，可以删除任何内容

b.列表.remove(元素) - 删除指定列表中的元素
注意：如果指定元素在列表中有多个，只删除最前面那一个

c. 列表.pop() - 取出列表中最后一个元素
   列表.[下标] - 取出列表中指定下标对应的元素
"""
list1 = [1, "abc", 404, "hello", 56, 45]
list2 = []
for i in list1:
    if isinstance(i, str):
        list2.append(i)
        list1.remove(i)
print(list1)
print(list2)

# 改（修改列表元素的值）
"""
列表[下标] = 新值 - 将列表中对应的元素修改成指定的元素
"""


