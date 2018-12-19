import time
from threading import Thread, Lock

"""
注意：当多个线程对同一个数据进行操作的时候，可能会出现数据混乱

多个线程对一个数据进行操作，一个线程将数据读出来，还没来得及存进去
另一个线程又去读了，这个时候就可能产生数据安全隐患  -  解决方案：加锁

Thread - 线程类（创建子线程）
Lock - 锁  （创建锁对象）
"""


class Account(object):
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.lock = Lock()

    def save(self, num):
        # 加锁
        self.lock.acquire()
        print("开始存钱")
        balance = self.balance
        time.sleep(5)
        self.balance = balance + num
        print("存入%s 成功" % num)
        # 解锁
        self.lock.release()

    def draw(self, num):
        # 加锁
        self.lock.acquire()
        print("开始存钱")
        balance = self.balance
        time.sleep(5)
        self.balance = balance - num
        print("取出%s 成功" % num)
        # 解锁
        self.lock.release()


acount1 = Account(10000, "小李")

t1 = Thread(target=acount1.save, args=(1000,))
t2 = Thread(target=acount1.draw, args=(500,))

t1.start()
t2.start()
t1.join()
t2.join()
print("余额：%s" % acount1.balance)
