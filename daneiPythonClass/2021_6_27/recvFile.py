import socket
so=socket.socket()
so.bind(("127.0.0.1",8888))
so.listen(3)
c,addr=so.accept()
print("Connect from:",addr)
#接收文件思路
"""
1->打开新文件  wb写
2->文件写入
"""
f=open("rcevFile.jpg","wb")
while True:
    data=c.recv(1024)
    f.write(data)
    if not data:
        print("传输完毕，over")
        break
f.close()
c.close()
so.close()
print("传输完毕")
