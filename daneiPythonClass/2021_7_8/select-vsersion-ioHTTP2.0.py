"""
technology  tcp,http ,select ,io reuse
"""
# httpserver 2.0 version
"""
port of class design :
stand in the condition which base on user
"""

from socket import *
from select import *


class HTTPServer:
    def __init__(self, host="127.0.0.1", port=9609, dir=None):
        self.__host = host
        self.__port = port
        self.__dir = dir
        self.__address = (host, port)
        self.__create_socket_bind()
        self.__rlist=[]
        self.__wlist=[]
        self.__xlist=[]
    def __create_socket_bind(self):
        self.__sockfd=socket()
        self.__sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.__sockfd.bind(self.__address)


    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        self.__host = host

    def __handle(self,r):
        pass


    def serve_forever(self):
        self.__sockfd.listen(5)
        print("Listen the port %d"%self.__port)
        #IO concurrence
        self.__rlist.append(self.__sockfd)
        while True:
            rs,ws,xs=select(self.__rlist,self.__wlist,self.__xlist)
            for r in rs:
                if r is self.__sockfd:
                    c,addr=r.accept()
                    print("Connect from ",addr)
                    self.__rlist.append(c)
                else:
                    self.__handle(r)



# the function users can use:
if __name__ == '__main__':
    """
    users can set up a io frame quickly to display their web
    the paramters need user send in
    """
    HOST = "127.0.0.1"
    PORT = 9609
    WEB_DIR = "./static"
    httpd = HTTPServer(HOST, PORT, WEB_DIR)
    httpd.serve_forever()
