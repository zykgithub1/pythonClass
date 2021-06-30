"""
chat room
socket udp  多进程
全局变量：
服务器地址

"""
from socket import *
import os,sys

ADDR=("127.0.0.1",9609)
def do_login():
    pass
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        get_type=data.decode().split(" ")[0]
        get_name=data.decode().split(" ")[1]
        if get_type=="L":
            pass
        elif get_type=="Q":
            pass
        else:
            pass
    pass
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    do_request(s)


    pass
if __name__ == '__main__':
    main()
    pass
