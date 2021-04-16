from socket import *

s=socket(AF_INET,SOCK_DGRAM)
a,b=s.accept()
print(a,b)