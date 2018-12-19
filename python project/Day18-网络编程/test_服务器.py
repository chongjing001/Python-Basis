import socket
import json

server = socket.socket()

server.bind(("10.7.187.103", 8680))

server.listen(256)
print("服务器开")


def online():
    while True:
        conversation, addr = server.accept()
        print("已连接", addr)
        while True:
            re_data = conversation.recv(1024)

            print("                                                           客户端：", re_data.decode("utf-8"))
            if re_data.decode("utf-8") == "拜拜":
                print("用户已断线...\n等待新用户...")
                online()
            elif re_data.decode("utf-8") == "1":
                with open("也总.jpg", "br") as f:
                    content = f.read()
                    print(content)
                    conversation.send(content)
                conversation.close()
            elif re_data.decode("utf-8") == "2":
                with open("data.json", encoding="utf-8") as f:
                    content = json.load(f)
                    content1 = json.dumps(content)
                    print(content1)
                    conversation.send(bytes(content1,encoding="utf-8"))
            elif re_data.decode("utf-8") == "3":
                print("服务器关闭")
                conversation.close()
            message = input("回复消息")
            conversation.send(bytes(message, encoding="utf-8"))


online()
