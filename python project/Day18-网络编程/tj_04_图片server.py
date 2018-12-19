import socket

server = socket.socket()

server.bind(("10.7.187.103", 8989))

server.listen(266)
print("开")
while True:
    conversation, addr = server.accept()
    print(addr)
    with open("luffy.png", "br") as f:
        content = f.read()
        conversation.send(content)

    conversation.close()

