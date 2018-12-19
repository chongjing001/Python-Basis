import socket

# 1.创建套接字对象
client = socket.socket()

# 2.连接服务器
"""
connect((ip, 端口))
"""
client.connect(("10.7.187.103", 8680))

# 3.发送消息
while True:
    message = input("输入--")
    client.send(message.encode("utf-8"))

    # 4.接受消息
    if message == "1":
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
    elif message == "2":
        data = []
        while True:
            re_data = client.recv(1024)
            print("接收")
            print(re_data.decode("utf-8"))
            data += re_data
            if not re_data:
                print("end")
                break
        print("                                                   服务器：", data.decode("utf-8"))
    else:
        re_data = client.recv(1024)

        print("                                                   服务器：", re_data.decode("utf-8"))
    if re_data.decode("utf-8") == "":
        print("退出")
        break
client.close()
