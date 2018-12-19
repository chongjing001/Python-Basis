
# with open(r"C:\Users\63562\Desktop\newceshi.txt","w") as f:
# #     f.write("这是个测试！")
# #     print("创建成功")


# with open(r"C:\Users\63562\Desktop\Linux.txt") as f:
#     str = f.readline()
#     while str:
#         print(str)
#         str = f.readline()



list1 = [{"name":1,"age":16},{"name":1},{"name":2}]

def count_name(list1, str1):
    count = 0
    for i in range(len(list1)):

        if list1[i]['name'] == str1:
            count += 1
    return count

print(count_name(list1,1))


# sl = [ {'code': 200,  'name': u'tv.xxx', 'time': '16:29:02'},
# {'code': 200,  'name': u'tv.xxx', 'time': '16:29:02'},
# {'code': 302,  'name': u'news.xxx', 'time': '16:29:03'},
# {'code': 200,  'name': u'news.xxx', 'time': '16:29:03'},
# {'code': 302,  'name': u'w.xxx', 'time': '16:29:03'},
# {'code': 302,  'name': u'w.xxx', 'time': '16:29:03'}]
#
# nl = []
# tl = [ str(r) for r in sl ]
# for record in set(tl):
#     n = eval(record)
#     n.update({"rqs":tl.count(record)})
#     nl.append(n)
# print(nl)