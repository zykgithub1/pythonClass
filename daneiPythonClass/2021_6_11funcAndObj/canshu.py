"""
position real canshu(位置实参)
vital real canshu  (关键字实参)
fun（b=1,b=2,c=3,a=4）

序列实参：穿个list
*list     星号将序列拆分后按位置传参

字典实参：传字典
**dic  两个星号   *拆分

fun(*a)->  将所有实参合并为一个元组

"""

def fun1(*args):
    print(args)
    pass

def fun(a,*args):
    print(a)
    print(args)
    pass

def fun2(**b):
    print(b)

def funWork(a,b,*args,c,d,**kwargs):
    print(a,b,args,c,d,kwargs)
    pass

def fun01():
    strs="  校  训 ：自  强不息,厚德载物。  "
    countSpace=0
    for item in strs:
        if item ==" ":
            countSpace+=1
    print("空位数量为：",countSpace)
    strs=strs.strip(" ")
    print("删除前后空格后的字符串",strs)
    list01=strs.split(" ")
    print("删除空格后的字符串组成的列表",list01)
    strs="".join(list01)
    print("列表重新组合为字符串",strs)
    index=strs.index("载物")
    print(index)
    print(strs.startswith("校训"))
    pass


def main():
    # ans=fun(1,2,3,4,5)
    # print(ans)
    # fun1(1,2,3,4,5)
    # str="12311"
    # ans=eval(str)
    # print(type(ans))
    # fun2(a={"fir":1,"second":2},b={"bfirst":"b1"})
    # funWork(1,2,1,2,3,4,4,c="C",d="D",g=1,f=2,i=22)
    fun01()
    a=[1,2]
    b=[1,2]
    print(a==b)
    print(a is b)
    pass

if __name__=="__main__":
    main()
    pass