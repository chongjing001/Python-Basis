


"""

1.已知一个列表，求列表中心元素。
2.已知一个列表，求所有元素和。
3.已知一个列表，输出所有奇数下标元素。
4.已知一个列表，输出所有元素中，值为奇数的。
5.已知一个列表，将所有元素乘二。
"""
# 1
list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
if len(list0) & 1 == 1:
    print("中心元素：%d" % list0[len(list0)//2])
else:
    print("中心元素：%d和%d" % (list0[len(list0)//2 - 1], list0[len(list0)//2]))
# 2
sum1 = 0
for i in list0:
    sum1 += i
print("所有元素的和为：%d" % sum1)
# 3
for i in range(len(list0)):
    if list0[i] & 1 == 1:
        print(i, end=" ")
# 4
print()
for i in list0:
    if i & 1 == 1:
        print(i, end=" ")
print()
# 5
for i in range(len(list0)):
    list0[i] *= 2
print(list0)
"""
6.有一个长度是10的列表，数组内有10个人名，
要求去掉重复的  
例如:names = ['张三', '李四', '大黄', '张三'] -
> names = ['张三', '李四', '大黄'] 
"""

names = ['张三', '李四', '大黄', '张三']
names1 = names
names = []
for i in names1:
    if i not in names:
        names.append(i)
print(names)
# 方法二
names = ['张三', '李四', '大黄', '张三']
print(list(set(names)))

"""
7.已经一个数字列表(数字大小在0~6535之间),
将列表转换成数字对应的字符列表  
例如: list1 = [97, 98, 99]  -> list1 = ['a', 'b', 'c'] 
"""
list1 = [97, 98, 99]
for i in range(len(list1)):
    list1[i] = chr(list1[i])
print(list1)

"""
8.用一个列表来保存一个节目的所有分数，
求平均分数(去掉一个最高分，去掉一个最低分，求最后得分
"""
shows = []
while True:
    show = input("请输入节目得分，end表示输入结束")
    if show != "end":
        shows.append(int(show))
    else:
        break
print(shows)
max1 = max(shows)
min1 = min(shows)
# 去除max和min，如果max和min不止一个数，也除掉
shows = list(x for x in shows if (x != max1 and x != min1))
print(shows)
print("平均值：%.2f" % (sum(shows)/len(shows)))



"""
9.有另个列表A和B，使用列表C来获取两个列表中公共的元素  
例如: A = [1, 'a', 4, 90]  B = ['a', 8, 'j', 1] 
--> C = [1, 'a']
"""
A = [1, 'a', 4, 90]
B = ['a', 8, 'j', 1]
C = []
for i in A:
    for j in B:
        if i == j:
            C.append(i)
            break
print(C)


