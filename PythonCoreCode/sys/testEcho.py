from socket import *

udpSock=socket(AF_INET,SOCK_DGRAM)
udpSock.bind(("",8585))
while 1:
    redata = udpSock.recvfrom(1024)
    udpSock.sendto(redata[0], redata[1])
udpSock.close()
