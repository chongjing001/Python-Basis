import fileMananger
import stu_manager
import json

stu_list = []
nums = 1  # 添加学号

xuhao = 0    # 添加序号

def count_name(dict1, str1):
    count = 0
    for i in dict1:
        if i == str1:
            count += 1
    return count

def input_enter(modified_value, tip_message):
    str1 = input(tip_message)
    if len(str1) > 0:
        return str1
    else:
        return modified_value

def data_conversion():
    stu_str = fileMananger.read_file("files/" + stu_manager.username)
    stu_list = json.loads(stu_str)
    return stu_list

def add_stuent():
    print("请输入信息")
    name = input("姓名")
    age = input("年龄")
    phone = input("电话")
    global nums
    stu_id = "stu" + (str(nums)).zfill(3)
    nums += 1
    # 添加字典名片
    stu_dict = {"stu_id": stu_id,
                "name": name,
                "age": age,
                "phone": phone}
    #
    stu_list.append(stu_dict)
    fileMananger.write_json_file("files/" + stu_manager.username, stu_list)
    print("添加{0}名片成功".format(name))

def check_student():
    print("1. 查看所有学生")
    print("2. 按姓名查找")
    print("3. 按学号查找")
    print("4. 返回")
    check_order = input("请选择查看方式")
    if check_order == "1":
        stu_list = data_conversion()
        if not stu_list:
            print("当前没有任何学生信息，请选择添加功能添加学生信息")
        else:
            print("所有名片如下")
            print("*" * 50)
            for name in ["学号", "姓名", "年龄", "电话"]:
                print(name, end="\t\t")
            print()
            print("*" * 50)
            for stu_dict in stu_list:
                print("%s\t%s\t\t%s\t\t%s" % (stu_dict["stu_id"],
                                              stu_dict["name"],
                                              stu_dict["age"],
                                              stu_dict["phone"]))
        input()
    elif check_order == "2":
        look_id = input("请输入需要查看的学生姓名")
        print("=" * 50)
        print("学号\t\t姓名\t\t年龄\t\t电话")
        stu_list = data_conversion()
        for stu_dict in stu_list:
            if stu_dict["name"] == look_id:
                print("%s\t%s\t\t%s\t\t%s" % (stu_dict["stu_id"],
                                              stu_dict["name"],
                                              stu_dict["age"],
                                              stu_dict["phone"]))
        input()
    elif check_order == "3":
        look_id = input("请输入需要查看的学生学号")
        stu_list = data_conversion()
        for stu_dict in stu_list:
            if stu_dict["stu_id"] == look_id:
                print("=" * 50)
                print("学号\t\t姓名\t\t年龄\t\t电话")
                print("%s\t%s\t\t%s\t\t%s" % (stu_dict["stu_id"],
                                              stu_dict["name"],
                                              stu_dict["age"],
                                              stu_dict["phone"]))
                input()
    elif check_order == "4":
        pass

def amend_student():
    amend_name = input("请输入您想要修改的学生信息的姓名或学号")
    stu_list = data_conversion()
    if count_name(stu_list, amend_name) > 1:
        print("=" * 50)
        print("序号\t\t学号\t\t姓名\t\t年龄\t\t电话")
        for stu_dict in stu_list:
            if stu_dict["name"] == amend_name:
                global xuhao
                stu_dict["xuhao"] = xuhao
                xuhao += 1
                print("%d\t\t%s\t%s\t\t%s\t\t%s" % (stu_dict["xuhao"],
                                                    stu_dict["stu_id"],
                                                    stu_dict["name"],
                                                    stu_dict["age"],
                                                    stu_dict["phone"]))
        str1 = input("请输入需要修改的学生信息的序号")
        # print(stu_list)
        for stu_dict in stu_list:
            if "xuhao" in stu_dict:
                if stu_dict["xuhao"] == int(str1):
                    print("=" * 50)
                    stu_dict["stu_id"] = input_enter(stu_dict["stu_id"], "学号[回车不修改]")
                    stu_dict["name"] = input_enter(stu_dict["name"], "姓名[回车不修改]")
                    stu_dict["age"] = input_enter(stu_dict["age"], "年龄[回车不修改]")
                    stu_dict["phone"] = input_enter(stu_dict["phone"], "电话[回车不修改]")
                    print("修改%s的信息成功" % amend_name)
                    input()
                    break
    else:
        for stu_dict in stu_list:
            if stu_dict["name"] == amend_name or stu_dict["stu_id"] == amend_name:
                print("=" * 50)
                print("学号\t\t姓名\t\t年龄\t\t电话")
                print("%s\t%s\t\t%s\t\t%s" % (stu_dict["stu_id"],
                                              stu_dict["name"],
                                              stu_dict["age"],
                                              stu_dict["phone"]))
                print("=" * 50)
                stu_dict["stu_id"] = input_enter(stu_dict["stu_id"], "学号[回车不修改]")
                stu_dict["name"] = input_enter(stu_dict["name"], "姓名[回车不修改]")
                stu_dict["age"] = input_enter(stu_dict["age"], "年龄[回车不修改]")
                stu_dict["phone"] = input_enter(stu_dict["phone"], "电话[回车不修改]")
                print("修改%s的信息成功" % amend_name)
                input()
                break


def del_student():
    del_name = input("请输入您想要删除的学生信息的姓名或学号")
    stu_list = data_conversion()
    if count_name(stu_list, del_name) > 1:
        print("=" * 50)
        print("序号\t\t学号\t\t姓名\t\t年龄\t\t电话")
        for stu_dict in stu_list:
            if stu_dict["name"] == del_name:
                global xuhao
                stu_dict["xuhao"] = xuhao
                xuhao += 1
                print("%d\t\t%s\t%s\t\t%s\t\t%s" % (stu_dict["xuhao"],
                                                    stu_dict["stu_id"],
                                                    stu_dict["name"],
                                                    stu_dict["age"],
                                                    stu_dict["phone"]))
        print("=" * 50)
        str1 = input("请输入需要删除学生信息的序号")
        for stu_dict in stu_list:
            if "xuhao" in stu_dict:
                if stu_dict["xuhao"] == int(str1):
                    str2 = input("请确认是否删除 yes/no")
                    if str2 == "yes":
                        stu_list.remove(stu_dict)
                        print("删除序号为%s的%s学生信息成功" % (str1, del_name))
                    else:
                        break
    else:
        for stu_dict in stu_list:
            if stu_dict["name"] == del_name or stu_dict["stu_id"] == del_name:
                print("=" * 50)
                print("学号\t\t姓名\t\t年龄\t\t电话")
                print("%s\t%s\t\t%s\t\t%s" % (stu_dict["stu_id"],
                                              stu_dict["name"],
                                              stu_dict["age"],
                                              stu_dict["phone"]))
                print("=" * 50)
                str2 = input("请确认是否删除 yes/no")
                if str2 == "yes":
                    stu_list.remove(stu_dict)
                    print("删除%s的信息成功" % del_name)
                else:
                    break