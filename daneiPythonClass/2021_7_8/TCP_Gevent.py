import gevent
from gevent import monkey
monkey.patch_socket()
from socket import *
import time
"""
gevent roroutine server bases on TCP
#logical:
set each handle with client as a function
transform sokect's block into roroutine process
"""
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",9609))
s.listen(4)
def handle(c):
    while True:
        data=c.recv(1024).decode()
        if not data:
            c.close()
            break
        print(data)
        c.send(b"OK")

if __name__ == '__main__':
    a_list=[]
    while True:
        print("tcp server wait for connect")
        c,addr=s.accept()
        print("connect from ",addr)
        f=gevent.spawn(handle,c)

