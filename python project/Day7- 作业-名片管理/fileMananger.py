

import json


def read_file(file):
    """
 读取文件内容
    :param file:要读取的文件
    :return:文件内容没有则返回None
    """
    try:
        with open(file, encoding="utf-8")as f:
            return f.read()
    except FileNotFoundError:
        print("没有找到文件" )
        return None




def write_json_file(file,obj):
    """
    数据写入json文件中
    :param file: 文件地址
    :param obj: 写入的python数据
    :return: 是否写入成功
    """
    try:
        with open(file, "w", encoding="utf-8")as f:
            json.dump(obj, f)
            return True
    except:
        return False


def read_json_file(file):
    """
    读取指定的json文件中的内容
    :param file: 文件地址
    :return: 文件中内容(python数据)
    """
    try:
        with open(file, encoding="utf-8")as f:
            return json.load(f)
    except FileNotFoundError:
        print("！！！文件不存在")
        return None


