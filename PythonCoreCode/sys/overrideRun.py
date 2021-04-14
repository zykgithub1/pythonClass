import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def run(self):
        n=5
        while n>0:
            print(n)
            n-=1
            time.sleep(1)
if __name__=="__main__":
    p=MyProcess()
    p.start()
    p.join()