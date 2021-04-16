from multiprocessing import Pool
import time


def work(num):
    print(num)
    time.sleep(1)


if __name__ == "__main__":
    po =Pool(3)
    for  i in range(20):
        po.apply_async(work,(i,))
    po.close()
    po.join()


