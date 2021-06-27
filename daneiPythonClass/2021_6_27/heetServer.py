"""
获取来自浏览器的请求
判断如果请求内容是  将index.html返回给客户端
else return 404
"""
from socket import *
def request(connfd):
    data=connfd.recv(4096)
    if not data:
        print("brower error")
        return
    # print(data.decode())
    request_line=data.decode().split("\n")[0]
    info=request_line.split(" ")[1]
    print(info,"<<--")
    if info=="/":
        with open("index.html","r")as f:
            reponse="HTTP/1.1 200 OK\r\n"
            reponse+="Content-type:text/html\r\n"
            reponse+="\r\n"
            reponse+=f.read()
            print(reponse)
    else:
        reponse = "HTTP/1.1 404 NOT Found\r\n"
        reponse += "Content-type:text/html\r\n"
        reponse += "\r\n"
        reponse+="<h1>Sorry the web is not exist</h1>"
    connfd.send(reponse.encode())
    pass
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
ADDR=("0.0.0.0",9609)
s.bind(ADDR)
s.listen(4)
while True:
    connfd, addr = s.accept()
    print("receive from :->", addr)
    request(connfd)
    break

connfd.close()
s.close()
