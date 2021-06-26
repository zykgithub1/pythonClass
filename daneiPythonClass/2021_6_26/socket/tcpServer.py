import socket
tcp_server=None
connfd=None
try:
    while True:
        tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server.bind(("0.0.0.0",8803))
        tcp_server.listen(5)
        print("wait for connec.....")
        connfd,addr=tcp_server.accept()
        print("Connect from",addr)
        while True:
            data = connfd.recv(1024)
            if data.decode()=="see you":
                print("end over dismiss")
                break
            print("收到", data.decode())
            n = connfd.send(b"thanks")
            print("发送了%d字节"%(n))
        print("cur client dead")
        connfd.close()
except:
    print("server exit")
    tcp_server.close()
