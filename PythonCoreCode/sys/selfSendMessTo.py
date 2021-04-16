from socket import *

s=socket(AF_INET,SOCK_DGRAM)
s.sendto("Nihao".encode(),("192.168.43.161",8080))
redata=s.recvfrom(2048)
print(redata[0].decode("gbk"))
print(redata[1])
for i in range(5):
    redata = s.recvfrom(2048)
    print(redata[0].decode("gbk"))
    print(redata[1])
s.close()