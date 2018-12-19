# 字符串复习
# 1.统计
str1 = "115dfd4ffssffd"
print(str1.count("d"))
print(str1.count("df"))
print(str1.count("ff"))
print(len(str1))

# 2.对齐

str2 = "对齐"
print(str2.center(8, "*"))
print(str2.rjust(8, "*"))
print(str2.ljust(8,"*"))
print(str2.zfill(8))

# 3.最值
# max 和 min

# 4.查找
str3 = "abc123jik"
print(str3.startswith("a"))
print(str3.startswith("ab"))
print(str3.endswith("k"))


print(str3.find("k"))
print(str3.find("p"))

print(str3.rfind("1"))
print(str3.index("2"))

print(str3.isdecimal())
print("5456".isdecimal())

# 替换
str4 = "abc123"
print(str4.replace("c1","sd"))

print(str4.capitalize())

print(str4.upper())
print("ABC155".lower())

print("abcOPQ".swapcase())


# 判断

print(str4.isalnum())

print(str4.isalpha())
print(str4.isdigit())
print("123".isdigit())

print(str4.islower())
print("ASD".islower())

print(str4.isupper())

print(str4.isnumeric())
print("789".isnumeric())

print(str4.isspace())
print("  ".isspace())

print("Tsjdi".istitle())
print("abctyh456".lstrip("ab"))
print("abcfgh123".split("cf"))


