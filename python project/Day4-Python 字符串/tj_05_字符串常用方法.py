
import random


#
# num = random.randint(0, 20)
# new_num = "python1808" + str(num).rjust(3, "0")
# print(new_num)
#
# str = "123456"
# print(str.startswith("12"))
# print(str.endswith("6"))
#
# str = "123456"
# print(str.find("3"))
# print(str.rfind("6"))
# print(str.find("7"))
# print(str.index("3"))
# print(str.rindex("6"))
#
# str = "123456"
# str2 = "abc"
# print(str.replace("123", str2))
#
#
# str1 = "abc123bnm"
# print(str1.isdecimal())
#
#
#
#
# str3 = "123456abc"
# print(str3.isalnum())
# print(str3.isalpha())
# print(str3.isdigit())
# print(str3.isdecimal())
#
# str3 = "123456abc"
# print(str3.islower())
# print(str3.isupper())

str4 = "123一二三壹幺萬"
str5 = " "
str6 = "Asjdkjdk123"
print(str4.isnumeric())
print(str5.isspace())
print(str6.istitle())

# str1 = "abc***DEF***123456"
# print(str1.upper())
# print(str1.lower())
# print(str1.swapcase())

str1 = "123456789066666"
print(str1.count("6"))
print(len(str1))

str2 = "  000 000**00"
print(str2.lstrip())
str3 = "**0000   "
print(str3.lstrip("**"))
str4 = "123abc000"
print(str4.split("23"))
print(str3.rstrip())


print(bool(""))