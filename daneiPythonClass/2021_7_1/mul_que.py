from multiprocessing import Queue,Process
import time,random
"""
消息队列符合先进先出原则 
"""
q=Queue(5)
def handle(q):
    for i in range(6):
        x=random.randint(1,33)
        q.put(x)
    q.put(random.randint(1,16))

def request(q):
    while True:
        # print("摇号。。。")
        time.sleep(2)
        try:
            print(q.get(3))
        except:
            break

if __name__ == '__main__':
    p1=Process(target=handle,args=(q,))
    p2=Process(target=request,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()



