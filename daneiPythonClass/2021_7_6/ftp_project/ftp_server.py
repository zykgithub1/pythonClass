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
        #     self.__socket.send(b"FTP is Empty")
        # elif filename not in self.__list_file:
        #     self.__socket.send(("there is no file called %s"%filename).encode())
        # else:
        #     self.__socket.send(b"OK")
        #     with open(filename,"rb")as f:
        #         while True:
        #             data=f.read(4096)
        #             if not data:
        #                 break
        #             self.__socket.send(data)
        try:
            str_file=os.getcwd()+"\\FTP\\"+filename
            f=open(str_file,"rb")
        except Exception:
            self.__socket.send("the file is not exist".encode())
            return
        else:
            self.__socket.send(b"OK")
            time.sleep(0.1)
        while True:
            data=f.read(1024)
            if not data:
                time.sleep(0.1)
                self.__socket.send(b"##")
                print("传输完成")
                break
            self.__socket.send(data)

    def __getfile_fromclient(self,filename):
        if filename not in self.__list_file:
            self.__socket.send(b"OK")
            str_file = os.getcwd() + "\\FTP\\" + filename
            with open(str_file, "wb")as f:
                data = self.__socket.recv(1024)
                if not data:
                    print("server get file finished")
                    return
                f.write(data)
            print("server already recive file from client")



    def run(self):
        while True:
            data=self.__socket.recv(1024).decode()
            if not data or data=="Q":
                return
            elif data=="L":
                self.__chect_list()
            elif data[0]=="G":
                filename=data.strip().split(" ")[-1]
                self.__download(filename)
            elif data[0]=="P":
                filename=data.strip().split(" ")[-1]
                self.__getfile_fromclient(filename)





def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    print("listen the port %s"%str(PORT))
    while True:
        try:
            c, addr = s.accept()
            print("connect from ->",addr)
        except KeyboardInterrupt:
            sys.exit("exit server")
        except Exception as e:
            print(e)
            continue
        client=FtpServer(c)
        client.daemon=True
        client.start()


    pass
#globle variation
HOST="0.0.0.0"
PORT=9609
ADDR=(HOST,PORT)
cur_path=os.getcwd()
all_file=os.listdir("FTP")




if __name__ == '__main__':
    # print(os.getcwd())
    # print(os.listdir("FTP"))
    main()

    pass