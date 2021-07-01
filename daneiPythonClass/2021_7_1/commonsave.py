from multiprocessing import Value,Process
import time
import random

money = Value("i", 5000)

def man():
    global money
    for i in range(30):
        time.sleep(0.3)
        money.value+=random.randint(1,1000)
        print("earn->",money.value)

def girl():
    global money
    for i in range(30):
        time.sleep(0.15)
        money.value-=random.randint(100,800)
        print("cost->", money.value)

if __name__ == '__main__':
    p1 = Process(target=man)
    p2 = Process(target=girl)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(money.value)
