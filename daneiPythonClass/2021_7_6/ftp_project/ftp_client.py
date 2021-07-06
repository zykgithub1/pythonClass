from socket import *
from threading import Thread
import os,sys
HOST="127.0.0.1"
PORT=9609
ADDR=(HOST,PORT)
FTP="E:\\vsproject\\pythoncode\\daneiPythonClass\\2021_7_6\\FTP"


class FTPClient:
    """
    check,sendFile,download,quit
    """
    def __init__(self,socket):
        self.__socket=socket

    #get file store list
    def get_list(self):
        self.__socket.send(b'L')
        data=self.__socket.recv(128).decode()
        if data=="OK":
            data=self.__socket.recv(4096)
            print(data.decode())
        else:
            print(data)

    def download_file(self,filename):
        send_str="G %s"%filename
        # print(send_str)
        self.__socket.send(send_str.encode())
        data=self.__socket.recv(128).decode()
        if data=="OK":
            with open(filename,"wb")as f:
                while True:
                    data = self.__socket.recv(4096)
                    if data==b"##":
                        break
                    f.write(data)
        else:
            print(data)

    def post_file(self,filename):
        str_file="P %s"%filename
        self.__socket.send(str_file.encode())
        data=self.__socket.recv(128).decode()
        if data=="OK":
            try:
                f=open(filename,"rb")
            except Exception:
                return
            else:
                print("start post file")
                while True:
                    data=f.read(1024)
                    if not data:
                        break
                    self.__socket.send(data)
                print("file put success")
        else:
            print("client else",data)


    def do_quit(self):
        self.__socket.send(b"Q")
        self.__socket.close()
        sys.exit("goodBye FTP-Server")


def main():
    sockfd=socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
    ftp_client=FTPClient(sockfd)
    while True:
        print("\n========命令选项=========")
        print("======== 1 list  ===========")
        print("======== 2 get file===========")
        print("======== 3 put file===========")
        print("======== 4 quit  ===========")
        print("===========================")
        cmd=input("请输入指令")
        cmd=cmd.strip()
        if cmd=="list":
            ftp_client.get_list()
        elif cmd[:3]=="get":
            target_filename=cmd.split(" ")[-1]
            print(target_filename)
            ftp_client.download_file(target_filename)
        elif cmd[:3]=="put":
            target_filename=cmd.split(" ")[-1]
            print(target_filename)
            ftp_client.post_file(target_filename)
        elif cmd=="put file":
            pass
        elif cmd=="quit":
            ftp_client.do_quit()
        else:
            print("please input right inditate")
            




if __name__ == '__main__':
    main()