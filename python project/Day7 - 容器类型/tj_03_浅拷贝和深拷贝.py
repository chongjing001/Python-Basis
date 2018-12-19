import copy


"""
copy.copy(对象) - 浅拷贝(直接拷贝元素的值产生一个新的地址)
copy.deepcopy(对象) - 深拷贝（不会直接复制地址，
                   而是将地址对应的值产生一份生成一个新的地址）

"""
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
list1 = [numbers1, numbers2]
list2 = list1.copy()  # 浅拷贝
print("1.浅拷贝")
print("修改前list1:", list1)
print("修改前list2:", list2)
print("对list1进行修改")
list1.append(66)
list1[0].append(666)
print("修改后list1:", list1)
print("修改后list2:", list2)


numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
list1 = [numbers1, numbers2]
list2 = copy.deepcopy(list1)  # 浅拷贝
print("2.深拷贝拷贝")
print("修改前list1:", list1)
print("修改前list2:", list2)
print("对list1进行修改")
list1.append(66)
list1[0].append(666)
print("修改后list1:", list1)
print("修改后list2:", list2)

