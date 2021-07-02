from threading import Thread,Lock
import time
class Acount:
    def __init__(self,id,balance,lock):
        self.id=id
        self.balance=balance
        self.lock=lock

    def draw(self,amount):
        self.balance-=amount

    def save(self,amount):
        self.balance+=amount

    def get_balance(self):
        return self.balance

Tom=Acount("tom",5000,Lock())
Alex=Acount("Alex",8000,Lock())
def transfer(from_1,to_,amount):
    from_1.lock.acquire()
    time.sleep(1)
    to_.lock.acquire()
    from_1.draw(amount)
    to_.save(amount)
    to_.lock.release()
    from_1.lock.release()
    print("%s 给 %s 转了 %d"%(from_1.id,to_.id,amount))

t1=Thread(target=transfer,args=(Tom,Alex,2000))
t2=Thread(target=transfer,args=(Alex,Tom,3000))
t1.start()
t2.start()
transfer(Tom,Alex,40)
print(Tom.get_balance(),Alex.get_balance())
t1.join()
t2.join()


