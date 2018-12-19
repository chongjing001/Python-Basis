
import tj_02_tools


input("欢迎使用名片系统 v1.0")
username = input("请输入用户名")
pwd = input("请输入密码")
if pwd == "6":
    print("欢迎%s\033[0;33;m" % username)
    id1 = 1  # 添加学号
    while True:
        tj_02_tools.main_menu()
        options = int(input("请选择您要执行的操作"))
        if options == 1:
            print("添加学生")
            print("*"*50)
            tj_02_tools.add_students()
            print("*"*50)
            while True:
                print("1. 继续")
                print("2. 返回")
                order = input()
                if order == "1":
                    tj_02_tools.add_students()

                elif order == "2":
                    break

        elif options == 2:
            print("查看学生")
            tj_02_tools.check_student()

        elif options == 3:
            print("修改学生信息")

        elif options == 4:
            print("删除学生")
        elif options == 5:
            print("退出")
            break
else:
    print("密码错误，您还有两次输入机会")

