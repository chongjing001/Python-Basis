import json

# 2
with open("data.json", encoding="utf-8")as f:
    content = f.read()
    print(content)

str1 = '{"name":"张三","age":20},4564564,"abc",[0,"s",5,365,89]'

with open("new", "w", encoding="utf-8")as f:
    f.write(str1)

py1 = json.loads('"truejkj"')

print(py1)

py2 = True
j1 = json.dumps(py2)
print(j1, type(j1))

a0 = dict(zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5)))
print(a0)

a2 = [i for i in range(10) if i in a0]
print(a2)

a3 = [a0[s] for s in a0]
print(a3)

a4 = [i for i in range(10) if i in a3]
print(a4)

a5 = {i: i * i for i in range(10)}
print(a5)

a6 = [[i, i * i] for i in range(10)]
print(a6)

stu_id = ("stu" + str(i).zfill(3) for i in range(100))

#
# for _ in range(99):
#     print(next(stu_id))


dict1 = {"name": "张三", "age": 20}
dict2 = {v: k for k, v in dict1.items()}
print(dict2)
