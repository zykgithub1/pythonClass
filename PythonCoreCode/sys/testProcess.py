from multiprocessing import Process

def run():
    print("123")

def run2():
    print("456")

if __name__=="__main__":
    p = Process(target=run)
    p.start()
    #p.join()
    p1 = Process(target=run2)
    p1.start()
    #p1.join()




