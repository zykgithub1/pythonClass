from multiprocessing import Process
import os
import time
def run():
    print("going on this process",os.getpid())
    time.sleep(1)
    print("this process over",os.getpid())

if __name__ == '__main__':
    p=Process(target=run)
    p2=Process(target=run)
    p.start()
    p2.start()
    p.join()
    p2.join()
    p.close()
    p2.close()
    pass