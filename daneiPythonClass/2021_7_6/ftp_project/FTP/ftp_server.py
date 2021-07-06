from socket import *
from threading import Thread
import os,sys
import time
def handle(c):
    pass
class FtpServer(Thread):
    """
    function:
    1,check list
    2,dowmload
    3,quit
    """
    def __init__(self,socket):
        super().__init__()
        self.__socket=socket
        self.__list_file=[]

    def __chect_list(self):
        self.__list_file=os.listdir("FTP")
        if not self.__list_file:
            self.__socket.send("文件库为空".encode())
            return
        else:
            self.__socket.send(b"OK")
            time.sleep(0.1)
        files=[]
        for item in self.__list_file:
            if item[0]!="." and os.path.isfile(os.getcwd()+"\\FTP\\"+item):
                files.append(item+"\n")
        send_str="".join(files)
        self.__socket.send(send_str.encode())




    def __download(self,filename):
        # self.__list_file = os.listdir("FTP")
        # if len(self.__list_file)==0:
        #     self.__socket.send(b"
        pass