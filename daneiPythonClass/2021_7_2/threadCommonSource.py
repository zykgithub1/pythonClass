"""
共享资源  同步互斥机制

"""
from threading import Thread, Event
import time

s = None
e=Event()


def yang():
    print("杨子荣拜山头")
    global s
    s = "天王盖地虎"
    e.set()


t = Thread(target=yang)
t.start()
# time.sleep(1)
print("说对口令才是自己人")
e.wait()
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("beat him to death")
t.join()
