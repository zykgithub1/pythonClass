from threading import Thread, Lock

a = b = 0
l = Lock()

def value():
    while True:
        l.acquire()
        if a != b:
            print("a=%d  b=%d" % (a, b))
        if a == 100:
            break
        l.release()


if __name__ == '__main__':
    t = Thread(target=value)
    t.start()
    while True:
        with l:
            if a == 100:
                break
            a += 1
            b += 1
            print("a=%d  b=%d" % (a, b))
    t.join()
