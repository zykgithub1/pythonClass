# a=int(input("请输入园的半径"))
# area=3.1415*a**2
# print("园的面积是%.2f"%area)
# from turtle import *
# turtle.pensize(2)
# turtle.circle(20)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(160)
# turtle.done()
# TempStr=input("输入带有符号的温度")
# if TempStr[-1] in ['F','f']:
#     C=(eval(TempStr[0:-1])-32)/1.8
#     print("转化后的温度是%.2fC"%C)
# elif TempStr[-1] in ['C','c']:
#     F=1.8*eval(TempStr[0:-1])+32
#     print("转化后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")


num=input("请输入字符")
# for nu in num:
#     print(nu,end=" ")
ans=num.startswith("RMB")
print(ans)


