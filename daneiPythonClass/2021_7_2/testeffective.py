from threading import Thread
from multiprocessing import Process
import time

def count(x,y):
    c=0
    while c<7000000:
        x+=1
        y+=1
        c+=1
if __name__ == '__main__':
    th_list = []
    th_time_start = time.time()
    for i in range(10):
        th_test = Process(target=count, args=(0, 0))
        th_test.start()
        th_list.append(th_test)
    for i in th_list:
        i.join()
    end_time = time.time()
    # for i in range(10):
    #     count(0,0)
    # end_time=time.time()
    distance_time = end_time - th_time_start
    print(distance_time)