import socket

# 1.创建套接字对象
client = socket.socket()

# 2.连接服务器
"""
connect((ip, 端口))
"""
client.connect(("10.7.187.103", 8686))

# 3.发送消息
while True:
    message = input("输入--")
    client.send(message.encode("utf-8"))

    # 4.接受消息
    re_data = client.recv(1024)
    print("                                                   服务器：", re_data.decode("utf-8"))
    if re_data.decode("utf-8") == "":
        print("退出")
        break
client.close()
