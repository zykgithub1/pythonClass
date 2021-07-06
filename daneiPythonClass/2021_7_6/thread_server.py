from threading import Thread
import os,sys
from socket import *
"""
1,create socket obj
2,loop for client's connect
3,create threading process deal with client's needs,main Process going on wait for connecting
4,threading process destroyed as long as process quit
"""
HOST="0.0.0.0"
PORT=9609
ADDR=(HOST,PORT)
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1 )
s.bind(ADDR)
s.listen(5)
print("listen the port 9609")
def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()





if __name__ == '__main__':
    while True:
        c=None
        try:
            c,addr=s.accept()
            print("connect from ",addr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print(e)
            continue
        #create thread handle
        t=Thread(target=handle,args=(c,))
        t.setDaemon(True)
        t.start()


    pass