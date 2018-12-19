import socket

"""
socker又叫套接字，指的就是实现通信过程的两个端。等待请求的一段叫服务端
发送请求的一段叫客服端

python提供了一个socket模块来支持socket编程

"""

"""
1.=======服务器套接字
创建套接字对象
socket(family, type)
family - 设置ip类型  AF_INET (默认值)  - ipv4    AF_INET6 - ipv6
type - 设置传输类型   SOCK_STREAM（默认值） - tcp
"""
# 创建一个基于ipv4和TCP的套接字对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip地址和端口
"""
bind((ip,端口号))
ip地址：服务器对应的计算机ip地址，字符串
端口号 - 用来区分计算机上不同服务;是一个数字，范围是0~65535，
             但其中1024以下的是著名端口，用来表示一个特殊服务，一般不要用
              同一时间一个端口只能对应一个服务器
"""
server.bind(("10.7.187.103", 9696))

# 开始监听
"""
listen(最大监听数)
最大监听数 - 用来设置当前服务器一次可以处理多少个请求
"""
server.listen(10)
print("开始监听")

# 让服务器一直处于启动状态
while True:
    # 接受客服端发送的请求，返回请求（客服端）地址和建立的会话  注意：这段代码会阻塞线程
    # 程序运行到这儿会停下来，知道有客户端给当前服务器发送请求为止
    conversation, addr = server.accept()
    print("===", addr)
    # 接受消息（客户端发送给服务器的消息）
    """
    recv(缓存大小)
    """
    re_data = conversation.recv(1024)
    print(re_data.decode("utf-8"))
    # 发送数据 (服务器给客户端发送给客户端)
    """
    send(数据) - 将指定的数据发送给客户端
    数据 - 要求是二进制
    a.字符串（str）转二进制（bytes）
    b.conversation.send(message.encode(encoding="utf-8"))
    
    二进制转字符串
    a.str(二进制数据，“utf-8")
    b.二进制.decode("utf-8")
    """
    message = input("回复消息")
    conversation.send(bytes(message, encoding="utf-8"))

    # 关闭连接
    conversation.close()
