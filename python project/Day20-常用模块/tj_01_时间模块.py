import time

"""
1.time  模块主要提供了很多和时间相关的函数，和一个类：struct_time

时间戳 - 指定时间-1970年1月1日 0:0:0
a.使用时间戳的场景
1.节约时间存储成本
   1543545822.2709627  -  8字节
   “2018/11/30 10:51:34”
2. 方便时间进行加密
"""
# 获取当前时间(单位：秒) - 以时间戳的形式返回
print(time.time())

# 2. localtime() - 获取当地时间（返回的是struct_time对象）
result = time.localtime()
print(result)
print("%s-%s-%s " % (result.tm_year, result.tm_mon, result.tm_mday))

result1 = time.localtime(0)
print(result1)

# 3.格式时间
"""
time.strftime(时间格式，时间对象) - 将时间对象转换成指定格式的时间字符串

时间格式 - 字符串，字符串中带有相应的时间格式，用来获取指定的时间值
%Y - 年
%m - 月
%d - 日
%H - 时
%M - 分
%S - 秒
%a - 星期英文单词缩写
%A - 全名
%b - 月份缩写
%B - 全名
事件对象 - struct_time
"""

time_str = time.strftime("%Y-%m-%d  %H:%M:%S  %B %A", time.localtime())
print(time_str)

# time_obj = time.strptime("今年是2018年11月30日", "今年是%Y年%m月30%d")
# print(time_obj)

from datetime import datetime, time, date, timedelta

"""
datetime模块主要包含三个类：
date（日期） -  只能对年月日对应的时间进行表示和操作
time（时间） -  只能对时分秒对应的时间进行表示和操作
datetime(日期和时间) -  能对 年月日 和 时分秒 对应的时间进行表示和操作

"""

date1 = date.today()
print(date1.year, date1.month, date1.day)

time1 = datetime.now()
print(time1.year, time1.month, time1.day, time1.hour, time1.minute, time1.second)

print(time1.date())
print(time1.time())
print(time1.now())
print(time1.ctime())

"""
date 和 datetime 对象支持时间的加减操作
时间对象 + timedelta对象
时间对象 - timedelta对象
"""
print("现在：", time1)
print("放假：", time1 + timedelta(hours=6))
print("加一天：", time1 + timedelta(days=1))


# 将字符串转换成datetime对象
time2 = datetime.strptime("2018-12-12  00:00:00", "%Y-%m-%d  %H:%M:%S")

print(time2 + timedelta(seconds=59))
print(time2 - timedelta(seconds=25))


import calendar

cal = calendar.calendar(2018)
print(cal)
