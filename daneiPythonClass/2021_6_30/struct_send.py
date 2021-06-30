import struct
from socket import *
st=struct.Struct("i32sif")
s = socket(AF_INET, SOCK_DGRAM)
ADDR = ("127.0.0.1", 9609)
while True:
    print("---------------")
    id=int(input("请输入id"))
    name=input("输入Name:").encode()
    if name=="":
        print("over")
        s.close()
        break
    age=int(input("Age->"))
    score=float(input("Score->"))
    data=st.pack(id,name,age,score)
    print(data)
    s.sendto(data,ADDR)
