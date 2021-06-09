def fun():
    a=[1,2,3,4,5,6,7,8,9]
    c=[]
    b=[item+1 for item in a if item%2!=0 ]
    print(b)
    pass

def fun1():
    a=[item for item in range(1,11)]
    b=[i for i in a if i%2!=0]
    c=[i for i in a if i%2==0]
    d=[i+1 for i in a if i%2==0 and i>5]
    print(a)
    print(b)
    print(c)
    print(d)
    pass

if __name__=="__main__":
    fun1()
    pass