from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(("", 8788))
a = 10
while a:
    s.sendto("asd".encode(), ("192.168.43.161", 8585))
    data = s.recvfrom(1024)
    print(data[0].decode(),a)
    a-=1
s.close()
