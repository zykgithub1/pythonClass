import time
"""
ans=time.strftime("%Y-%m-%d  %H-%M-%S")
ans2=time.strptime(ans,"%Y-%m-%d  %H-%M-%S")
print(type(ans))
print(type(ans2))
print(ans2)
"""
now=time.strftime("%Y-%m-%d  %H-%M-%S")
f=open("work.txt","a+")
f.seek(0,0)
num=0
for line in f:
    num+=1
while True:
    num += 1
    s="%d->  %s\n"%(num,time.strftime("%Y-%m-%d  %H-%M-%S"))
    f.write(s)
    print(s)
    if num==10:
        break
    f.flush()
    time.sleep(1)
f.close()
