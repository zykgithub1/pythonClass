from socket import *

s=socket(AF_INET,SOCK_DGRAM)
s.bind(("",8585))
s.sendto("begin".encode(),("192.168.43.161",8788))
while True:
    redata=s.recvfrom(1024)
    print("room1收到信息为：",redata[0].decode())
    data=input("请输入：")
    s.sendto(data.encode(),redata[1])
s.close()
