#删除一个列表重复元素，保持元素顺序不变
'''a=[1,2,1,3,1,3,4.5]
def x(list):
    new_ans=[]
    for i in list:
        if i not in new_ans:
            new_ans.append(i)
    return new_ans
print(x(a))'''

#编写一个函数，接受字符串参数，返回第一个元组
#元组第一个值为大写字母的个数，第二个值为小写字母的个数
'''def x(str):
    new_ans=[]
    upper=0
    lower=0
    for i in range(0,len(str)):
        if str[i].isupper():
            upper+=1
        elif str[i].islower():
            lower+=1
    new_ans=[upper,lower]
    return new_ans
print(x("hello   HELLO"))'''

import  random
'''
def x():
    a=random.randint(1,6)
    b=random.randint(1,6)
    c = random.randint(1, 6)
    return a+b+c
print(x())'''

'''def prepare():
    top=0
    mid=0
    three=0
    for i in range(0,1000):
        a=random.uniform(0,1)
        if a>0 and a<=0.08:
            top+=1
        elif a>0.08 and a<0.3:
            mid+=1
        elif a>0.3 and a<1:
            three+=1
    print("一等奖个数"+str(top))
    print("二等奖个数"+str(mid))
    print("三等奖个数"+str(three))
prepare()'''
'''list=[0,1,2,3,4]
def findFox(list,i):
    a=input("输入你的决策")
    if int(a)== i:
        print("抓住了")
    else:
        print("猜错了")
        findFox(list,(i+1)%len(list))
findFox(list,5)'''

'''Game_dict={
    "top":(0,0.08),
    "second":(0.08,0.3),
    "thrid":(0.3,1)
}
def Game():
    i=random.random()
    for k,v in Game_dict.items():
        if v[0]<=i<=v[1]:
            return  k
result={}
for i in range(1,1000):
    res=Game()
    if res not in result:
        result[res]=1
    else:
        result[res]+=1
print(result)'''
hole=[0,0,0,0,0]
fox=random.randint(0,4)
hole[fox]=1
def move(hole):
    if hole[4]==1:
        hole[3]=1
        hole[4]=0
    elif hole[0]==1:
        hole[1]=1
        hole[0]=0
    else:
        old=hole.index(1)
        hole[old]=0
        hole[old+random.choice([-1,1])]=1
while True:
    chose=int(input("输入决策"))
    if(hole[chose]==1):
        print("抓到了")
        break;
    else:
        print("没抓到")
    move(hole)








