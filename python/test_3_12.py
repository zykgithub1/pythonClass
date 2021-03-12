'''1.题
a=input("输入第一个数字")
b=input("输入第二个数字")
c=int(a)-int(b)
if c%2 !=0:
    print(c)
else:
    print("结果不是奇数")'''
#2题
'''a=input("请输入年龄")
while int(a)<0 or int(a)>150:
    print("这不是人")
    a=input("重新输入年龄")
if int(a) < 18:
    print("未成年")
elif int(a)>18:
    print("成年")'''
#3题:
'''count=0
for i in range(1,101):
    if int(i-int(i/10)*10)==2 and i%3==0:
        count=count+1
        print(i,end=" ")
print()
print(count)'''
#4
'''a=input("一个整数：")
count=0
while int(a) >0:
    count+=1
    a=int(a)/10
    #print(int(a))
print(count)'''








