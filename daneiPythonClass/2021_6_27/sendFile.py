from socket import *
sendSo=socket()
sendSo.connect(("127.0.0.1",8888))
f=open("universe.jpg","rb")
while True:
    data=f.read(1024)
    sendSo.send(data)
    if not data:
        print("文件读入完毕，发送过去")
        break
sendSo.close()
f.close()
