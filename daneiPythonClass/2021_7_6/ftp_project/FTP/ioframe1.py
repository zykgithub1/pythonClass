from multiprocessing import Process
from socket import *
import os
import signal
"""
step:
1,creat socket obj
2.wait for connecting
3.server create new process to deal with client's need
4,the main process is still waiting for client's connect
5,if client quit,destroy the process
"""
#globle variation
HOST="0.0.0.0"
PORT=9609
ADDR=(HOST,PORT)
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
print("listen the port 9609")
def process_control(s,c):
    s.close()
    handle(c)
    os._exit(0)

def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"Ok")
    c.close()
    pass


if __name__ == '__main__':
    while True:
        c, addr = None, None
        try:
            c, addr = s.accept()
            print("connect from->", addr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print(e)
            continue
        # create new process to deal with issue
        p1 = Process(target=process_control,args=(s,c))
        p1.daemon=True
        p1.start()
    # deal with zombie process
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    pass