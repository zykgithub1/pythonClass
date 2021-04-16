from socket import *
dest=("<broadcast>",8080)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.sendto("hi".encode(),dest)
while True:
    ans=s.recvfrom(1024)
    print(ans[0].decode("gbk"))