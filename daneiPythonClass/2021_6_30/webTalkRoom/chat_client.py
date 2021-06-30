from socket import *
import os,sys
ADDR=("127.0.0.1",9609)
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    names=[]
    while True:
        name=input("请输入姓名")
        msg="L "+name
        s.sendto(msg.encode(),ADDR)
        data,addr=s.recvfrom(1024)
        if data.decode()=="OK":
            print("welcome to zyk's talk room")
        else:
            print("forbid this commission\n",data.decode())

    # s.close()

if __name__ == '__main__':
    main()
    pass