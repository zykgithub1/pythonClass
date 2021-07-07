import select
from socket import *
import os,time

s=socket()
s.bind(("127.0.0.1",9609))
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.listen(3)
rlist=[s]
wlist=[]
xlist=[]
while True:
    rs,ws,xs=select.select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("connect from ", addr)
            rlist.append(c)
        #client send msg
        else:
            data=r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            wlist.append(r)

    for w in ws:
        w.send(b"OK")
        wlist.remove(w)

    for x in xs:
        pass



