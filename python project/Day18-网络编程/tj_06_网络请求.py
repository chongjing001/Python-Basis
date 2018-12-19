import requests

"""
python中去做第三方请求，需要使用一个第三方库：requests

"""

"""
get(url,参数字典)  - 返回响应
"""
# 向服务器发送get请求
# a.手动拼接url
# url = "https://www.apiopen.top/satinApi?type=1&page=1"
# response = requests.get(url)
# print(response)

# b.自动拼接url
url = "https://www.apiopen.top/satinApi"
response = requests.get(url, {"type": 1, "page": 1})
print(response)

# 获取响应头
header = response.headers
print(header)

# 获取响应体
"""

"""
content = response.content
print(content)

"""
b.获取json格式响应体
"""
json = response.json()
print(type(json))

"""
获取字符串格式
"""

text = response.text
print(text)
print(type(text))

url1 = "https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1543395098&di=2a5bbaa5600097b050ba69a688672de9&src=http://p0.qhimgs4.com/t0112e7ebfdef7f923d.jpg"

response = requests.get(url1)
image_data = response.content
with open("也总.jpg", "wb") as f:
    f.write(image_data)











