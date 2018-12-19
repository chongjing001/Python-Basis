
stu_list = []  # 数据库

def main_menu():
    # print('033\[0;33;m')

    print("               ")
    print("1. 添加学生")
    print("2. 查看学生信息")
    print("3. 修改学生")
    print("4. 删除学生")
    print("5. 返回")
    print("="*50)



def add_students():
    print("请输入信息")
    name = input("姓名")
    age = input("年龄")
    phone = input("电话")
    # 添加字典名片
    stu_dict = {"name": name,
                "age": age,
                "phone": phone}


    # 将字典中的元素添加到列表中
    stu_list.append(stu_dict)
    print(stu_list)
    print("添加{0}名片成功".format(name))


def check_student():
    print("1. 查看所有学生")
    print("2. 按姓名查找")
    print("3. 按学号查找")
    print("4. 返回")
    check_order = input("请选择查看方式")
    if check_order == "1":
        if len(stu_list) == 0:
            print("当前没有任何名片，请选择添加学生功能添加名片")
        else:
            print("所有名片如下")
            print("*"*50)
            for name in ["姓名", "年龄", "电话"]:
                print(name, end="\t\t")
            print()
            print("*"*50)
            for stu_dict in stu_list:
                print("%s\t\t%s\t\t%s" % (stu_dict["name"],
                                         stu_dict["age"],
                                         stu_dict["phone"]))
        input()
    elif check_order == "2":
        look_name = input("请输入需要查看的学生姓名")
        for stu_dict in stu_list:
            if stu_dict["name"] == look_name:
                print("="*50)
                print("姓名\t\t年龄\t\t电话")
                print("%s\t\t%s\t\t%s" % (stu_dict["name"],
                                          stu_dict["age"],
                                          stu_dict["phone"]))
                input()
                break
            else:
                print("没有找到改名片")
    elif check_order == "3":
        pass

    elif check_order == "4":
        pass


def amend_message():
    pass



