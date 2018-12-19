import fileMananger
import stu_manager
import stu_tools





all_user_file = 'files/user_info.json'

def login():
    usename = input("请输入用户名")
    pwd = input("请输入密码")
    all_user = fileMananger.read_json_file(all_user_file)
    if not all_user:
        print("登录失败！账号没有注册！！！")
        return
    if usename in all_user:
        if all_user[usename] == pwd:
            print("登陆成功")
            # 进入学生管理页面
            stu_manager.username = usename
            stu_manager.show_manager_page()

        else:
            print("登录失败！密码错误！！！")
    else:
        print("登录失败！%s账号没有注册" % usename)


def register():
    """注册"""
    print("注    册")
    while True:
        username = input("请输入用户名(3~6位)")
        if 3 <= len(username) <= 6:
            break
        else:
            print("用户名格式不正确，请从新输入")
    while True:
        pwd = input("请输入密码（6~12位）")
        if 6 <= len(pwd) <= 12:
            break
        else:
            print("密码格式不正确，请从新输入")
    # 判断账号是否注册过
    all_user_dict = fileMananger.read_json_file(all_user_file)
    if not all_user_dict:
        all_user_dict = {}

    if username in all_user_dict:
        print("注册失败 用户名%s已被注册" % username)
        return
    else:
        all_user_dict[username] = pwd
        fileMananger.write_json_file(all_user_file, all_user_dict)
        print("注册成功")
        input()

def show_main_page():
    """
    显示主页
    :return:
    """
    while True:
        print(fileMananger.read_file("files/mainpage.txt"))
        str1 = input("请选择（1~3）")
        if str1 == "1":
            login()
            while True:
                print(fileMananger.read_file("files/stu_mainpage"))
                options = input("请选择您要执行的操作")
                if options == "1":
                    print("添加学生")
                    stu_tools.add_stuent()
                elif options == "2":
                    print("查看学生")
                    stu_tools.check_student()
                elif options == "3":
                    print("修改学生")
                    stu_tools.amend_student()
                elif options == "4":
                    print("删除学生")
                    stu_tools.del_student()
                else:
                    print("退出系统")
                    break

        if str1 == "2":
            register()

        else:
            print("正在注销")
            break


if __name__ == '__main__':
    show_main_page()








