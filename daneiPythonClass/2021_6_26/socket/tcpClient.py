from socket import *
so=socket()
# so.bind(("0.0.0.0",8809))
so.connect(("127.0.0.1",8803))
while True:
    sendtoServer = input("输入信息:")
    so.send(sendtoServer.encode())
    data=so.recv(1024)
    print(data.decode())
    if sendtoServer=="see you":
        break

so.close()

