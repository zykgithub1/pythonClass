"""
socket in unblock way
each 3 sed fill in log
"""
from socket import *
import time,os
f=open("log.txt","a+")
s=socket()
s.bind(("127.0.0.1",9609))
s.listen(5)
#set s into unblock status
s.setblocking(False)
if __name__ == '__main__':
    while True:
        print("wait for connect")
        try:
            conn,addr=s.accept()
        except BlockingIOError as e:
            time.sleep(3)
            f.write("%s : %s\n"%(time.ctime(),e))
            f.flush()
        except Exception:
            f.close()
            s.close()
            os._exit(0)
        else:
            print("connect from %s"%addr)

