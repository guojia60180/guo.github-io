#Author guo
#服务器端

import  socket
server=socket.socket()
server.bind(("localhost",6969))#绑定需要监听的端口
server.listen()#监听
print("等待")
conn, addr = server.accept()  # 等发送过来
# 链接实例 与地址
print("laile")
while True:

    # conn,addr=server.accept()#等发送过来
    # #链接实例 与地址
    # print("laile")
    data=conn.recv(1024)
    if not data:
        break#客户端已断开
    print("recv:",data)
    conn.send(data.upper())

server.close()