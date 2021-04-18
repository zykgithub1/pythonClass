from socket import *
#编写tcp服务器
tcpSock=socket(AF_INET,SOCK_STREAM)
tcpSock.bind(("",7788))
tcpSock.listen(5)
newSock,clientAddr=tcpSock.accept()
#等待连接,创建新套接字，因为listen在listen
#新套接字用于传输
data=newSock.recv(1024)
print(data.decode())
#tcp回信时不需要填写接收方的ip，port等  因为tcp已连接
newSock.send("i accepted your messages".encode("gbk"))
newSock.close()

tcpSock.close()




