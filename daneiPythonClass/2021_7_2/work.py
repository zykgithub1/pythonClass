from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,target=None,args=None,kwargs=None):
        super().__init__()
        self.target=target
        self.args=args
        self.kwar=kwargs

    def run(self):
        self.target(*self.args,**self.kwar)


def player(sec,song):
    for i in range(3):
        print("Playing  %s  : %s"%(song,time.ctime()))
        time.sleep(sec)


if __name__ == '__main__':
    t=MyThread(target=player,args=(2,),
               kwargs={"song":"凉凉"})
    t.start()
    t.join()