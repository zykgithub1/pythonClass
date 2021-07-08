"""
test gevent
"""
import gevent
from gevent import monkey

import time
monkey.patch_all()
def foo(a,b):
    print("running foo  ->  ",a,b)
    time.sleep(2)
    print('foo again')

def bar():
    print("running bar  ->  ")
    time.sleep(4)
    print('bar again')
#generate coroutine obj
f=gevent.spawn(foo,1,2)
b=gevent.spawn(bar)
gevent.joinall([f,b])
