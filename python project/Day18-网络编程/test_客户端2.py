import socket

# 1.创建套接字对象
client = socket.socket()

# 2.连接服务器
"""
connect((ip, 端口))
"""
client.connect(("192.168.1.5", 8680))

# 3.发送消息
while True:
    message = input("输入--")
    client.send(message.encode("utf-8"))

    # 4.接受消息
    data = bytes()
    while True:
        re_data = client.recv(1024)
        data += re_data
        print("接收到数据")
        if not re_data:
            break
        print(data)
    with open("new.png", "bw") as f:
        f.write(data)
