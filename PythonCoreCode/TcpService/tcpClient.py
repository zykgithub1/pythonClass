from socket import *

client=socket(AF_INET,SOCK_STREAM)
#客户端不需要绑定端口 因为服务器会用ACEEPT获得客户端的信息
client.connect(("192.168.43.161",7788))
#三次握手建立连接和四次挥手进行断开不需要我们写代码  网上自动完成
client.send(b"nihao")
while True:
    data = client.recv(1024)
    print(data.decode())
    sendData=input("请输入要回复的信息")
    client.send(sendData.encode())
client.close()

