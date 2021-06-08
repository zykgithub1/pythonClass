def f1():
    str = "xX"
    str = str.islower()
    a = 100
    b = bin(a)
    print(b)
    a = 'z'
    pass


def f2():
    print(chr(100))
    print(ord("曾"))
    print(ord("驿"))
    print(ord("凯"))
    pass


def f3():
    str = input()
    for i in str:
        print(ord(i), end="  ")

    while True:
        ch = input()
        if ch == "":
            print("Bye")
            break
        ch = int(ch)
        print(chr(ch))
    pass


def f4():
    # name="""
    # w
    # h
    # a
    # t
    # """
    # name='我叫"\tz\ny\tk\t"'
    # print(name)
    # op=open("test.txt",'wr')
    # op.write("哈哈")
    print(ord("悟"))
    print(ord("八"))
    print(chr(100))
    str = "一个和尚两个锅"
    print(str[-3:-5:-1])
    print(str[3:1:-1])
    print("----------------------")
    ans = str.split("sh")
    ans2 = str.strip("sh")

    print(ans2)
    print(ans)

    pass


def f5():
    num = int(input("输入一个数字"))
    for i in range(num):
        if i == 0 or i == num - 1:
            print("*" * num)
        else:
            print("*", end="")
            print(" " * (num - 2), end="")
            print("*")

    pass


def f6():
    str = input("输入一个字符串")
    if str == str[::-1]:
        print(str)
        print(str[::-1])
        print("是回文字符串")
    else:
        print(str)
        print(str[::-1])
        print("不是")


def f7():
    first = 100
    h = first / 2
    sum = first
    while h > 0.01:
        sum += h * 2
        print(h)
        h /= 2
    print("小球一共走了%.2lf米，最后小球反弹高度为%.2lf" % (sum, h))
    print("aaa\abbb")


def f8():
    list01 = list("我是齐天大圣")
    list02 = ["我是齐天大圣"]
    list01.remove("是")
    print(list01)
    del list01[:]
    # list01.remove(list01[0])
    print(list01)
    pass
def f9():
    persons=[]
    str = None
    while str!="":
        str = input("输入人物")
        persons.append(str)
    print(persons[:-1])
    pass
def f10():
    persons=[]
    #一行输入所有任务，中间以逗号隔开
    str=input("输入所有")
    persons=str.split(",")
    print(persons)
    pass

def f11():
    persons=[]
    while True:
        str=input("请输入学生姓名")
        if str=="":
            for i in range(len(persons)-1,-1,-1):
                print(persons[i])
            break
        if str in persons:
            print("%s该学生已存在"%str)
            continue
        persons.append(str)
    pass

if __name__ == "__main__":
    f11()
    pass
