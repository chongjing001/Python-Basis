import re

"""
1
正则表达式就是字符匹配的工具；是由正则符号和普通字符组成，
来匹配不同规律的字符串

2.python对正则表达式的支持
re模块
fullmatch(正则表达式，字符串) - 用正则表达式去完全匹配字符串，如果匹配成功返回匹配结果
写法：将正则内容写在字符串中，一般这个字符串最前面加r/R（阻止转义）

"""

# 1.普通字符
"""
普通字符在正则表达式中代表本身
"""
# 匹配一个字符串，依次匹配a、b、c
re_str = r"abc"
result = re.fullmatch(re_str, "abc")
print(result)

# 2  . 匹配任意字符
"""
在正则表达式中，.出现的位置，可以匹配一个任意字符
注意：一个.只能匹配一个字符
中文也能匹配
"""
re_str = r"a.c"
result = re.fullmatch(re_str, "abc")
print(result)

# 3 \w(匹配字母数字或者下划线)
"""
\w出现的位置，可以匹配任意一个的字母、数字、下划线(也能匹配Unicode中除了ASCII码剩下的编码)
"""
re_str = r"\w\w..."
result = re.fullmatch(re_str, "_好kll")
print(result)

# 4  \s(匹配空白字符)
"""
包括：空格、制表符和换行符
"""

re_str = r"\w\w\s\w"
result = re.fullmatch(re_str, "ab\tf")
print(result)

# 5 \d(匹配数字字符)
re_str = "\d\d\d.."
result = re.fullmatch(re_str, "123ab")
print(result)

# 6 \b (检测单侧边界)
"""
注意：\b是检测\b出现的位置是否是单词边界，不会对字符进行匹配
          当正则表达式中出现了\b，匹配的时候去掉\b，匹配成功后再看\B出现的位置是否是单词边界
边界：开头、结尾（只要能够将单词区分开的符号）
"""
re_str = r"hello,\bworld"
result = re.fullmatch(re_str, "hello,world")
print(result)
# 7  ^(检测字符串开头)
"""
在match和fullmatch中没有意义，search、findall等中有意义
"""
re_str = "^The.."

# 8 $(检测字符串结尾)
"""
在match和fullmatch中没有意义，search、findall等中有意义
"""

"""
"\大写字母"对应的功能是"\小写字母"功能取反

\W - 匹配非数字字母下划线
\D - 匹配非数字字符
\S - 匹配非空白字符
\B - 检测非单词边界

"""

# [字符集]（匹配中括号出现的任意一个字符）
"""
1.[字符集] - 匹配中括号出现的任意一个字符
例：[abc] - 匹配一个字符是a或者b或者c
注意：一个中括号只能匹配一个字符
            正则中有特殊功能的单个符号，在[]都表示它本身例如：. $  ^ + *  | 等
            匹配字符的组合符号，在括号中保持原来的功能，例如：\w  \d  \s
"""
# 匹配一个长度是2的字符串，第一个是数字，第二个字符是b或者c或者d
re_str = r"\d[bcd]"
result = re.fullmatch(re_str, "2c")
print(result)

"""
[字符1 - 字符2] - 表示字符1到字符2（注意：要求字1的编码值要小于字符2）
[a-z] - 表示匹配所有的小写字符
[a-zA-Z]  - 匹配所有字母
[1-7] - 匹配数字字符1到7
[\u4e00 - \u9fa5] - 匹配所有的中文

"""
re_str = r"[1-7][abc-][a-z]"
result = re.fullmatch(re_str, "1-g")
print(result)

# 11 [^字符集] - 匹配不在字符集中的任意一个字符
"""
例：[^abc] - 匹配除了"a","b","c"以外的其他任意一个字符

[abc^] - 匹配"a","b","c"，"^"中任意一个字符
"""


