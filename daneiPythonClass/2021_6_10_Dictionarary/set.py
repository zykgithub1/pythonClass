
def fun():
    s1=set("1234")
    s2=set("2345")
    strs=str(s2)
    print(strs)
    s3=s1|s2
    print(s3)
    print("--------------------")
    list01=[1,2,3,4,5,1,1,2,3,4,5]
    set1=set(list01)
    str_s=str(set1).strip("{").strip("}")
    print(str_s)
    print(set1)

    pass
"""
交 &，并 |，补->  a^b，子 s1<s2  ->true，超 s1>s2 false
"""
def fun1():
    set1=set()
    print(set1)
    while True:
        strs=input("输入字符串")
        if strs=="":
            break
        set1.add(strs)
    print(set1)
    pass

def fun2():
    s1={"曹操","刘备","孙权"}
    s2={"曹操","刘备","张飞","关羽"}
    #是经理也是技术的
    s3=s1&s2
    print(s3)
    #是经理，不是技术
    s3=s1-s2
    print(s3)
    #是技术，不是经理
    s3=s2-s1
    print(s3)
    #张飞是经理吗
    flag="张飞" in s1
    print(flag)
    #身兼一职的有哪些
    s3=s1^s2
    print(s3)
    #一共多少人
    s3=len(s1|s2)
    print(s3)

    pass

def fun3():
    for i in range(4):
        for j in range(i+1):
            print("*",end=" ")
        print()

    for i in range(1):
        print(i)
    pass

def fun4():
    arr=[10,9,5,4,8,2,6,7,1,0]
    for  i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    for i in arr:
        print(i,end=" ")
    pass
import copy
def fun5():
    list01=[
        [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
            ]
    list02=copy.deepcopy(list01)
    for i in range(len(list01)):
        for j in range(len(list01[0])):
            list02[j][i]=list01[i][j]
    for i in list02:
        print(i)
    pass

def fun6():
    list01 = [
        [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]
    ]
    ans=[]
    for i in range(len(list01)):
        ans.append([])
        for j in range(len(list01[0])):
            ans[i].append(list01[j][i])
    print(ans)
    pass

def fun7():
    l1=["香蕉","苹果","哈密瓜"]
    l2=["可乐","牛奶"]
    l3=[]
    set_t=set()
    dfs(l1,0,set_t,l3)
    print(l3)
    pass

def dfs(lis,index,temp,ans):
    if len(temp)==len(lis):
        ans.append(list(temp))
    temp.add(lis[index])
    dfs(lis,index+1,temp,ans)
    temp.remove(lis[index])

def fun8(angle,row):
    # print(angle)
    if row==len(angle)-1:
        return
    for i in range(row,len(angle)):
        if i!=row:
            angle[row][i],angle[i][row]=angle[i][row],angle[row][i]
    fun8(angle,row+1)

def test():
    list01 = [
        [1, 2, 3, 4,5],
        [ 6, 7, 8,9,10],
        [ 11, 12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ]
    print(list01)
    fun8(list01,0)
    print(list01)
    # for i in ans:
    #     print(i)
    pass

def main():
    test()

    pass

if __name__=="__main__":
    main()
    pass