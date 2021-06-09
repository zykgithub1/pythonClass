import random
def test():
    count=0
    cost=0
    while True:
        caipiao=goal()
        goumai=pay()
        print(caipiao)
        print(goumai)
        print("这是%d组"%(count))
        flag=True
        for i in range(0,len(goumai)):
            if caipiao[i]!=goumai[i]:
                flag=False
                continue
        if flag==True:
            break
        cost+=2
        count+=1

    print("total times : %d"%(count))
    print("cost is :%d"%(cost))
    pass

def goal():
    ans=[]
    num=0
    while len(ans)!=6:
        num=random.randint(1,33)
        if num not in ans:
            ans.append(num)
    blueball=random.randint(1,16)
    ans.append(blueball)
    return ans

def pay():
    ans=[]
    num=0
    while len(ans)!=6:
        num=random.randint(1,33)
        if num not in ans:
            ans.append(num)
    blueball = random.randint(1, 16)
    ans.append(blueball)
    return ans

if __name__=="__main__":
    test()
    pass