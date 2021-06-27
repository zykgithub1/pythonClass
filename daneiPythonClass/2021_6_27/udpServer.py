from socket import *
so=socket(AF_INET,SOCK_DGRAM)
so.bind(("127.0.0.1",9609))
while True:
    data,addr=so.recvfrom(1024)
    print("数据：->",data.decode())
    so.sendto(b'Thanks controll your temper',addr)
    if not data:
        break
so.close()
