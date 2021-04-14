from multiprocessing import Process

num=1

def run():
    global num
    num+=5
    print("进程一中num=%s"%(num))

def run2():
    global num
    num+=10
    print("进程二中num=%s"%(num))

if __name__=="__main__":
    p=Process(target=run)
    p2=Process(target=run2)
    p.start()
    p2.start()
    p.join()
    p2.join()
    print("主进程中Num=%s"%(num))
