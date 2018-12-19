



def id_count(list1,str1):
    return list1.count(str1)



def login():
    while True:
        print("\033[5;32;m")
        str1 = input("""
    =======================================
    =     注册登录系统  v 1.00             =
    =       1--注册                       =
    =       2--登录                       =
    =       3--退出                       =
    =======================================
    \n""")
        if str1 == "1":
            username = input("请输入用户名")
            with open("idandpwd","r",encoding="utf-8") as f:
                str2 = f.read()
            list1 = str2.split("/")
            for i in list1:
                if i == username:
                    username = input("\033[5;31;m用户名已存在，请重新输入")
            pwd = input("\033[5;33;m请输入密码")
            pwd1 = input("请再次确认密码")
            if pwd == pwd1:
                print("注册成功")
                with open("idandpwd","a",encoding="utf-8") as f:
                    f.write(username+"/"+pwd+"/")
        elif str1 == "2":
             print("*"*50)
             username = input("\033[5;34;m请输入用户名")
             pwd = input("请输入密码")
             with open("idandpwd", "r", encoding="utf-8") as f:
                 str3 = f.read()
             list2 = str3.split("/")
             for i in range(len(list2)):
                 if list2[i] == username:
                     if list2[i+1] == pwd:
                        print("登录成功")
             if id_count(list2,username) == 0:
                 print("没有%s的用户信息，请您先注册在登录" % username)
             input()
        elif str1 == "3":
            print("退出成功")
            break

login()