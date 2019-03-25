#Author guo
#客户端
import socket

client=socket.socket()#声明socket类型，同时生成socket连接对象

client.connect(("localhost",9999))
while True:
    msg=input(">>:").strip()

    client.send(msg.encode("utf-8"))#不能发送该类型 发送ASCII码的

    data=client.recv(1024)
    print("recv:",data.decode())
client.close()
