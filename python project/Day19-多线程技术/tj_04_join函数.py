from random import randint

from threading import Thread

import time, datetime

"""
线程对象.join() - 等待线程对象中的任务执行完成

"""


class Dlowload(Thread):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        print("开始下载：%s" % self.file_name)
        a = randint(2, 100)
        time.sleep(a)
        print("%s 下载完成,耗时%d s" % (self.file_name, a))


if __name__ == '__main__':
    t1 = Dlowload("小航人")
    t2 = Dlowload("倒霉熊")
    time1 = time.time()
    t1.start()
    t2.start()
    # t1 和 t2 中的任务都执行完成后才执行后面的代码
    t1.join()
    t2.join()
    t3 = Dlowload("七龙珠")
    t3.start()
    t3.join()
    time3 = time.time()
    print("总时间：%s" % (time3 - time1))
