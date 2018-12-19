import socket
from threading import Thread

server = socket.socket()

server.bind(("10.7.187.103", 12345))
server.listen(200)


class MoreThread(Thread):
    def __init__(self, conversation, addr):
        super().__init__()
        self.conversation = conversation
        self.addr = addr

    def sun(self):
        while True:
            mesage = conversation.recv(1024).decode("utf-8")
            print(mesage)


while True:
    conversation, addr = server.accept()
    print(addr)

    # 给服务器发送请求的客服端建立一个子线程，在子线程中处理每一个请求
    t1 = MoreThread(conversation, addr)
    t1.start()

    # while True:
    #     message = conversation.recv(1024)
    #     print(message)
