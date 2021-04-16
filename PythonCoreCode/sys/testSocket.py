from socket import *

#udp速度快 安全性没TCP高  tcp较慢
"""
udp不提供有效性  只负责传  可能丢失  不预先建立连接  数据流传输
tcp要先进行对话连接   数据报传输
"""
s=socket(AF_INET,SOCK_DGRAM)
addr=("192.168.43.161",8080)
data=input("输入你要发送的数据")
s.sendto(data.encode("gbk"),addr)
redata=s.recvfrom(2048)
print(redata[0].decode("gbk"))
s.close()

