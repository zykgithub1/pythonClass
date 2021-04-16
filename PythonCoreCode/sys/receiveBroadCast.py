from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.bind(("",8080))
ans=s.recvfrom(1024)
print(ans[0].decode())
s.sendto("我已收到".encode("gbk"),ans[1])