from socket import *

s=socket(AF_INET,SOCK_DGRAM)
s.bind(("",8788))

while True:
    redata=s.recvfrom(1024)
    print("room2收到的信息为：",redata[0].decode())
    data=input("请输入你要发送的信息:")
    s.sendto(data.encode(),redata[1])
s.close()