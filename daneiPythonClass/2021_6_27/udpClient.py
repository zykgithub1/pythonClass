from socket import *
so=socket(AF_INET,SOCK_DGRAM)

ADDR=("127.0.0.1",9609)
while True:
    data=input("MSG->")
    if not data:
        break
    so.sendto(data.encode(),ADDR)
    recvData=so.recvfrom(1024)
    print("from server:->",recvData[0].decode())
so.close()

