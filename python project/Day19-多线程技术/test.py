import time
import datetime
import threading
import requests


def download(url):
    image_data = requests.get(url).content
    file_name = url.split("/")[-1]
    with open("images/" + file_name, "wb")as f:
        f.write(image_data)


url = "https://www.apiopen.top/satinApi?type=1&page=1"
# data_dict = requests.get(url).json()
# datas = data_dict["data"]
# for dict1 in datas:
#     print(dict1["profile_image"])
#     # 拿到一个图片地址，就创建一个线程对象，用来在线程中下载图片
#     t = threading.Thread(target=download, args=(dict1["profile_image"],))
#     t.start()
# print("下载完成")

import re
text = requests.get(url).text
all_profile_image = re.findall(r'"profile_image":"(.+?)",',text)
# print(all_profile_image)
for url in all_profile_image:
    threading.Thread(target=download,args=(url,)).start()





