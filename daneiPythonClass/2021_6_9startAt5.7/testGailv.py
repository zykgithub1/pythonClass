import random
def getNum():
    ans=[]
    num=random.randint(1,1000)
    num2=random.randint(1,1000)
    ans.append(num)
    ans.append(num2)
    return ans

def test():
    times=0
    lis1=[]
    lis2=[]

    while True:
        lis1=getNum()
        flag = True
        lis2=getNum()
        for i in range(0,len(lis1)):
            if lis1[i]!=lis2[i]:
                flag=False
                continue
        if flag ==True:
            print("结束了找到了")
            break
        times+=1
    print(times)

if __name__=="__main__":
    test()


