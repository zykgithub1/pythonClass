"""
客户端发起请求
展现请求结果
"""
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
ADDR=("127.0.0.1",9609)
while True:
    words=input("请输入要查的单词")
    if not words:
        break
    s.sendto(words.encode(),ADDR)
    data=s.recvfrom(1024)
    print("meaning of words:",data[0].decode())



