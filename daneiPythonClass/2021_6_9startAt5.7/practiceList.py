def fun1():
    a=[55,22,12,52,35,17]
    poviod=30
    b=[]
    for num in a:
        if(num>poviod):
            b.append(num)
    for num1 in a:
        for num2 in b:
            if num1==num2:
                print(id(num1)==id(num2))
    a[0]=44
    a[3]=44
    a[4]=44

    print(b)
    pass

def fun2():
    maxV=0
    for i in range(5):
        a=int(input("输入一个数"))
        # max=max if max>a else a
        maxV=max(maxV,a)
    print(maxV)

def fun3():
    a = [55, 22, 12, 52, 35, 17]
    for i in range(0,len(a)):
        print(a[i])
    pass

def fun4():
    b = [55, 22, 12, 52, 35, 17]
    for i in range(len(b)-1,-1,-1):
        if b[i]>20:
            b.remove(b[i])
    print(b)
    pass

def fun5():
    lis=[]
    for i in range(11):
        lis.append(str(i))
    print(lis)
    ans="".join(lis)
    ans="~~".join(["hahah","yes"])
    strs="zyk hello world"
    anss=strs[::-1]
    print(anss)
    pass

def fun6():
    list_str=[]
    while True:
        str=input("输入字符串")
        if str=="":
            break
        list_str.append(str)
    print(list_str)
    ans=",".join(list_str)
    print(ans)
    pass

def fun7():
    str01="曾-易-凯"
    ans=str01.split("-")
    print(ans)
    pass

def fun8():
    str="how are you"
    a=[1,2,3,4,5,6]
    a.reverse()
    lis=str.split(" ")
    lis.reverse()
    ans=" ".join(lis)
    print(a)
    print(ans)
    pass

if __name__=="__main__":
    fun8()
    pass