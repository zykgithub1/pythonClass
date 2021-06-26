"""
每次open 打开文件偏移量都在开头
用a方式打开在结尾
读写公用一个偏移量
"""
if __name__=="__main__":
    f=open("dest.txt","rb+")
    print(f.tell())
    data=f.read(5)
    print(f.tell())
    f.seek(-5,2)
    f.write(b"$$$")
    f.close()
    pass