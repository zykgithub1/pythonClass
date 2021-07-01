"""
1，Pipe只能用于有亲缘关系的进程中
2，管道对象在父进程中创建，子进程通过父进程进行获取
"""
from multiprocessing import Pipe, Process
import time

fd1, fd2 = Pipe()


def app1(fd1):
    print("app1 start   请登录")
    print("请App2 授权")
    fd1.send(("app1 请求登录"))
    data = fd1.recv()
    if data:
        print("登陆成功：", data)


def app2(fd2):
    # print("app2 running")
    data = fd2.recv()  # 阻塞函数
    print(data,"app2 收到的data")
    fd2.send(("Python", "pygame"))


if __name__ == '__main__':
    p1 = Process(target=app1, args=(fd1,))
    p2 = Process(target=app2, args=(fd2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("over")
