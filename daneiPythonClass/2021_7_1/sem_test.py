from multiprocessing import Process,Semaphore
import time
import os
#largest num
sem=Semaphore(3)
def handle(sem):
    sem.acquire()
    print("%s   执行任务"%os.getpid())
    time.sleep(2)
    print("%s   Mission success"%os.getpid())
    sem.release()

if __name__ == '__main__':
    run_list=[]
    for i in range(10):
        p=Process(target=handle,args=(sem,))
        run_list.append(p)
        p.start()
    for i in run_list:
        i.join()
