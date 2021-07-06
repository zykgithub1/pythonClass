from socket import *
import os
s=socket()

s.connect(("127.0.0.1",9609))
while True:
    try:
        sendMessage = input("msg->")
        s.send(sendMessage.encode())
        data = s.recv(1024)
        print(data.decode())
    except KeyboardInterrupt:
        print("结束")
        s.close()
        os._exit(0)
