
def fun():
    a=tuple(range(11))
    b=[a]
    c=a
    a=b
    print(a)
    print(id(a))
    print(id(b[0]))
    pass

def fun1():
    a=(1111,2222,3333)
    b=[1111,2222,3333]
    for i in range(0,len(a)):
        print(id(a[i])==id(b[i]))
    a=(111,)
    print(type(a))
    str="abcd"
    a=str.split()
    b=tuple("+".join(str))
    print(a)
    print(b)
    pass

def fun2():
    str="a b c d e f g"
    a=str.split()
    ans="".join(a)
    print(ans)
    print(type(a))
    print(type(a[0]))
    d=[1,]
    print(type(d[0]))
    pass

if __name__=="__main__":
    fun2()
    pass