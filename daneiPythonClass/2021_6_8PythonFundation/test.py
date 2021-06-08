def func():
    # print("hello world")
    # a="增益开"
    # print(id(a))
    # a="曾2凯"
    # b=a
    # print(id(a))
    # print(id(b))
    # c=d=a
    # print(id(c))
    # print(id(d))
    a = 155
    b = 0b111100100100101010100
    # a,b=b,a
    # print("a=%s"%a)
    # print("b=%s"%b)
    print(oct(100))
    a = 5 + 40j
    print(a.imag)


def func2():
    a = 100
    b = a
    print("a" + str(id(a)))
    print("b" + str(id(b)))
    a += 100
    print("a" + str(id(a)))
    print("b" + str(id(b)))


def fun3():
    str = "zyk"
    str = str * 3
    print(str)


def fun4():
    a = "str"
    b = a
    c = a
    del a, b
    print(c)


def fun5():
    a = 1000
    print(id(a))
    b = a - 1
    print(id(b))
    c = b + 1
    print(id(c))
    print(a == c, a is c)
    print(type(id(a)))
    a = str((id(a))) * 5
    # import random as r
    # a=r.choice
    # print(a)


def fun7():
    a = []
    str = input();
    a.append(str);
    b = []
    str = a[0]
    for st in str:
        if st.isdigit():
            b.append(st)
    print(a)
    print(b)


# def fun6():
#     a=random.randint(10,100)
#
#     print(a)

def fun8():
    a=0.01e-3
    count=0
    while a<8844.43:
        a*=2
        count+=1
        print(count, a)

    return

import random as r

def fun9():
    i=0

    while i <100:
        random_Num = r.randint(0, 10)
        print(random_Num,i)
        i+=1
    pass

import math
def  fun10():
    a=16.2312321
    b=3.5121212121
    print("a是{:.4},b是{:.5}".format(a,b))

if __name__ == "__main__":
    # func2()
    # func()
    fun10()
    pass
