import time
import  datetime

"""
一个进程默认有一个线程，这个线程叫主线程，默认情况下，所有的的代码
都是在主线程中执行的


"""


def download(film_name):
    print("开始下载...  %s" % film_name, datetime.datetime.now())
    time.sleep(5)   # 暂停5秒
    print("%s 下载结束" % film_name, datetime.datetime.now())




if __name__ == '__main__':
    # 在主线程中下载两个电影
    download("小黄人")

    download("地心游记")
    

