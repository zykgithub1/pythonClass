from socket import *
import struct

ip="192.168.43.161"
fileName="up.png"
f=open(fileName,"ab")
s=socket(AF_INET,SOCK_DGRAM)
sendInfo=struct.pack("!H%dsb5sb"%(len(fileName)),1,fileName.encode(),0,"octet".encode(),0)
s.sendto(sendInfo,(ip,69))
while True:
    recv_data=s.recvfrom(1024)
    caoZuoMa,ackNum=struct.unpack("!HH",recv_data[0][:4])
    randPord=recv_data[1][1]
    if int(caoZuoMa)==5:
        print("文件不存在")
        break
    print("操作码：%d ACK:%d 服务器端口号:%d 数据长度:%d"\
          %(caoZuoMa,ackNum,randPord,len(recv_data[0])))
    f.write(recv_data[0][4:])
    if len(recv_data[0])<516:
        print("文件传输完毕")
        break
    ack_data=struct.pack("!HH",4,ackNum)
    s.sendto(ack_data,(ip,randPord))