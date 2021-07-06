from multiprocessing import Process
import os

FILENAME = "111u.jpg"
file_size = os.path.getsize(FILENAME)


def top():
    fr = open(FILENAME, "rb")
    fw = open("top.jpg", "wb")
    n = file_size // 2
    fw.write(fr.read(n))
    fw.close()
    fr.close()


def down():
    fr = open(FILENAME, "rb")
    fw = open("down.jpg", "wb")
    fr.seek(file_size // 2)
    fw.write(fr.read())
    fw.close()
    fr.close()


if __name__ == '__main__':
    p1 = Process(target=top)
    p2 = Process(target=down)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("OK")
    pass
