def fc(a):
    """
    传入的是可变对象，函数修改的是传入对象
    不需要return
    栈帧里面形参指向跟原始是一样的
    可变对象 list dic set
    :param a:
    :return:
    """
    a.append(3)
num=100
print("全局ID",id(num))
def fun1():
    global num
    print("global id",id(num))
    num=10
    print("函数ID", id(num))


def fun():
    li1=[1,2]
    fc(li1)
    print(li1)
    pass

def main():

    print(id(num))
    fun1()
    pass

if __name__=="__main__":
    main()
    pass