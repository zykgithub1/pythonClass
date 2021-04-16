from multiprocessing import Pool
import time
num=0
def run():
    global num,i
    num+=5
    print("run",num,i)
    # time.sleep(1)

def run2():
    global num,i
    num+=10
    print("run2",num,i)
    # time.sleep(1)
i=0
if __name__=="__main__":
    p=Pool()
    for i in range(100):
        p.apply_async(run())
        p.apply_async(run2())
    # p.close()
    # p.join()


