from socket import *
import struct

sever_IP="192.168.43.161"
fileName="down.png"
f=open(fileName,"ab")
s=socket(AF_INET,SOCK_DGRAM)

send_data=struct.pack("!H%dsb5sb"%(len(fileName)),1,fileName.encode(),0,"octet".encode(),0)
s.sendto(send_data,(sever_IP,69))

while True:
    recv_data=s.recvfrom(1024)
    #前2个是操作码  后2两个是块编号  后面512才是数据
    #ackNum 是发送过来的包是第几块
    #作为接受方  你接收数据后肯定要回信  把ACKNUm发回去 表示自己已收到这一个包
    caozuoma,arc_num=struct.unpack("!HH",recv_data[0][:4])
    rand_port = recv_data[1][1]
    if int(caozuoma)==5:
        print("文件不存在")
        break
    print("操作码:%d,ACK: %d 服务器端口号: %d ,数据长度：%d"\
          %(caozuoma,arc_num,rand_port,len(recv_data[0])))
    f.write(recv_data[0][4:])
    if len(recv_data[0])<516:
        print("文件传输完毕")
        break
    ack_data=struct.pack("!HH",4,arc_num)
    s.sendto(ack_data,(sever_IP,rand_port))

