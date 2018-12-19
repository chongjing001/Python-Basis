import time
import datetime
import threading

"""
python通过threading模块，来支持多线程技术

默认线程叫主线程，其他的线程叫子线程,如果希望代码在子线程执行
必须手动创建

"""


def download(film_name):
    print("开始下载...  %s" % film_name, datetime.datetime.now())
    time.sleep(5)  # 暂停5秒
    print("%s 下载结束" % film_name, datetime.datetime.now())
    print("下载 %s" % film_name, threading.current_thread())


if __name__ == '__main__':
    # download("倒霉熊")

    # 1.创建线程对象
    """
    Thread(target=函数名，args=参数列表) - 直接创建线程对象
    函数名 = 需要在当前的子线程中执行的函数变量
    参数列表 = 元组 ，元组的元素是
    """
    t1 = threading.Thread(target=download, args=("倒霉熊",))
    t2 = threading.Thread(target=download, args=("金刚",))
    # 在子线程中执行任务
    """
    调用t1对应的线程中调用download函数，并且传递一个参数
    """
    t1.start()
    t2.start()
