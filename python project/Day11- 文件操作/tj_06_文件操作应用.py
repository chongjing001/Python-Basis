# 例：写一个运行第几次打印几程序
# README 为txt文本，里面输入一个数字1
with open("README",encoding="utf-8") as f:
    count = int(f.read())
print("第%d次运行程序" % count)

count += 1
with open("README","w") as f:
    f.write(str(count))




