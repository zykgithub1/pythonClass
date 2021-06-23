
def derocter(fun):
    def wrap(*args):
        print("进行账号密码验证")
        fun(*args)
    return wrap

@derocter
def deposit(money):
    print("存钱,->%.2f"%money)

@derocter
def withdraw(log_id,pwd):
    print("取钱",log_id,pwd)
#
# deposit(10000)
# withdraw("zs",123)
import time


def count_time(func):
    def wrap(*args):
        start=time.time()
        func(*args)
        end=time.time()
        durationTime=end-start
        print("执行时间为",durationTime)
    return wrap

@count_time
def fun01():
    time.sleep(2)
    print("fun01执行完毕了")

@count_time
def fun02(a):
    time.sleep(1)
    print("fun02执行完毕了,参数是",a)
#
# fun01()
# fun02(11)
print(time.localtime())