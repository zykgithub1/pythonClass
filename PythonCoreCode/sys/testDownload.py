from socket import *
import struct

cmb_buf=struct.pack("!H8sb5sb",1,"down.png".encode(),0,"octet".encode(),0)
udpSock=socket(AF_INET,SOCK_DGRAM)
udpSock.sendto(cmb_buf,("192.168.43.161",69))
f=open("down.png","ab")    #"a"为追加模式“b“为二进制形式打开
while True:
    recv_data = udpSock.recvfrom(1024)
    caozuoma,ack_num=struct.unpack("!HH",recv_data[0][:4])
    rand_port=recv_data[1][1]
    if int(caozuoma)==5:
        print("文件不存在")
        break
    print("操作码：%d,ACK: %d,服务器随机端口号：%d,数据长度：%d"%(caozuoma,ack_num,rand_port,len(recv_data)))
    f.write(recv_data[0][4:])
    if len(recv_data[0])<516:
        print("传输完毕")
        break
    ack_data=struct.pack("!HH",4,ack_num)
    udpSock.sendto(ack_data,("192.186.43.161",rand_port))

