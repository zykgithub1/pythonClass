"""
服务端提供逻辑和数据处理
"""
def searchWords(word):
    f=open("dic.txt","r")
    for line in f:
        w=line.split(" ")[0]
        if w>word:
            f.close()
            return "未找到该单词"
        elif w==word:
            f.close()
            return line
    else:
        f.close()
        return "未找到该单词"
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s1=socket()
ADDR=("127.0.0.1",9609)
s.bind(ADDR)
while True:
    data,addr=s.recvfrom(1024)
    flag=input("is onging")
    if not flag:
        break
    print("收到的请求单词为",data.decode())
    words_info_str=searchWords(data.decode())
    s.sendto(words_info_str.encode(),addr)
s.close()

