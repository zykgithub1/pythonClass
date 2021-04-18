from socket import *
from multiprocessing import *
import sys,os

def dealWithClient(newSocket,clientAddr,fn):
    sys.stdin = os.fdopen(fn)
    while True:
        #print(newSocket)
        recvData=newSocket.recv(1024)
        if(len(recvData))>0:
            print("收到信息%s"%(recvData.decode()))
            sendData=input("输入你要发送的信息")

            newSocket.send(sendData.encode())
        else:
            print("%s客户端已关闭"%clientAddr)
            break
        # newSocket.close()
def main():
    fn = sys.stdin.fileno()
    serSocket=socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    localAddr=("",7788)

    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
       while True:
           print("主进程等待客户端到来：")
           newSocket, clientAddr = serSocket.accept()
           print("主进程创建一个新的进程来处理数据")
           clientDeal = Process(target=dealWithClient,args=[newSocket,clientAddr,fn])
           clientDeal.start()
           # newSocket.close()
    finally:
        print("服务结束，TCP服务器关闭")
        serSocket.close()
if __name__=="__main__":
    main()