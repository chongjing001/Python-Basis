import socket

client = socket.socket()

client.connect(("10.7.187.103", 8989))

# 不断接受数据
data = bytes()  # 创建一个空的二进制数据
while True:
    re_data = client.recv(1024)
    data += re_data
    print("接收到数据")
    if not re_data:
        break

print("end")
with open("new.png", "bw") as f:
    f.write(re_data)
