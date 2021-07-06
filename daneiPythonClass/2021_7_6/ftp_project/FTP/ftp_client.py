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
                    