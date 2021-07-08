"""
sample of coroutine
"""
import greenlet
def fun1():
    print("conduct dun1")
    gr2.switch()

    print('fun1 over')
    gr2.switch()


def fun2():
    print("conduct dun2")
    gr1.switch()

    print('fun2 over')
    gr1.switch()


gr1=greenlet.greenlet(fun1)
gr2=greenlet.greenlet(fun2)
gr1.switch()


