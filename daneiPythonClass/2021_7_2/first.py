"""
self thread
"""
from threading import Thread
import time

class myClass(Thread):
    def __init__(self, *args):
        super().__init__()
        self.attr = args[0]

    def f1(self):
        time.sleep(1)
        print("step  1!!!",self.attr)
        pass

    def f2(self):
        time.sleep(2)
        print("step  2!!!!")
        pass

    def run(self):
        self.f1()
        self.f2()


if __name__ == '__main__':
    t=myClass("ABC")
    t.start()
    for i in range(5):
        time.sleep(1)
        print("我是主进程")
    t.join()
    pass
