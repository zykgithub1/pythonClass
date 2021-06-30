import struct
from socket import *

st=struct.Struct(("i32sif"))
s = socket(AF_INET,SOCK_DGRAM)
ADDR = ("127.0.0.1", 9609)
s.bind(ADDR)
while True:
    data, addr = s.recvfrom(1024)
    with open("load.txt","a") as f:
        decode_data=st.unpack(data)
        #(id,name,age,socre)
        # print(type(decode_data))
        decode_data=list(decode_data)
        decode_data[1]=decode_data[1].decode().split('x')[0]
        print(decode_data[1])
        # fk="qdsada"
        # fk.split()
        print(decode_data[0],decode_data[1],decode_data[2],decode_data[3])
        info=str(decode_data[0])+' '+decode_data[1]+' '+str(decode_data[2])+' '+str(decode_data[3])+"\n"
        print(info)
        f.write(info)
