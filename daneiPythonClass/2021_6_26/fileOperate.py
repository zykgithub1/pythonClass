# fread=open("copyFile.txt","rb")
# fwirte=open("dest.txt","wb")
# ans=fread.readlines()
# # print(type(ans2))
# # for item in ans:
# #     fwirte.write(item)
# while not fread.read(1111):
#     print(fread.read())
# fread.close()
# fwirte.close()
try:
    fread=open("111.jpg","rb")
except FileExistsError as e:
    print(e)
else:
    fw=open("copy.jpg",'wb')
    # print(type(fread.read()))
    while True:
        data=fread.read(1024)
        print(type(data))
        print(data)
        if not data:
            break
        fw.write(data)
    fw.close()
    fread.close()
