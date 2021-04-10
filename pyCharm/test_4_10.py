# # s={"name":"haha"}
# # for k in s.keys():
# #     print(k)
# text="i love python dou you love pythoniiiii"
# b={a:text.count(a) for a in text}
# a=[5,4,3,2,1]
# a.sort(reverse=True)
# print(a)
# print(b)
import turtle
#画圆圈：
# t = turtle.Pen()
# my_coloer=["red","yellow","green","blue"]
# t.speed(0)
# for i in range(0,100):
#     t.penup()
#     t.width(5)
#     t.goto(0,-i*20)
#     t.pendown()
#     t.color(my_coloer[i%len(my_coloer)])
#     t.circle(20+20*i)
# turtle.done()
#t=turtle.Pen()
# for row in range(10):
#     t.penup()
#     t.goto(-50,row*10)
#     t.pendown()
#     t.goto(50,row*10)
# for col in range(11):
#     t.penup()
#     t.goto(-50 + col * 10, 90)
#     t.pendown()
#     t.goto(-50 + col * 10, 0)
# width=30
# num=18
# x=([-400,400],[])
# y=[[-400,400],[]]
# t.speed(0)
# for i in range(20):
#     t.penup()
#     t.goto(-200,200-i*40)
#     t.pendown()
#     t.goto(200,200-i*40)
# for i in range(21):
#     t.penup()
#     t.goto(-200+i*40,200)
#     t.pendown()
#     t.goto(-200+i*40,-160)
# turtle.done()
'''def test():
    """比较较大值"""
    print("*"*10)
test()
test()
help(test.__doc__)'''
# print(5/2)
# print(5//2)
# str="zyk"
# str2="henshuai"
# c=str.__add__(str2)
# d=str+str2
# def f():
#     return None
# print(type(f))

# a=5
# def f():
#     global a
#     print(a)
#     a=6
#
# f()
# print(a)
import math
import time
# def test():
#     start=time.time()
#     for i in range(10000000):
#         math.sqrt(100)
#     end=time.time()
#     print("全局变量耗时{0}".format(end-start))
#
#
# def test1():
#     b=math.sqrt
#     start=time.time()
#     for i in range(10000000):
#         b(100)
#     end=time.time()
#     print("局部变量耗时{0}".format(end-start))
# test()
# test1()
# time1=time.time()//1
# # print(time1)
# b=[10,20]
# print(id(b))
# def test(b):
#     print(id(b))
#     b.append(30)
#     print(id(b))
#     return b
# test(b)
# print(id(b))
# print(b==test(b))
# str=['zykhaoshuai']
# str1=[].append(str.append(11))
# print(str)
# print(str1)
# import copy
# def testcopy():
#     a = [10, 20, [5, 6]]
#     b = copy.copy(a)
#     print("a", a)
#     print("b", b)
#
#     b.append(30)
#     b[2].append(7)
#     print("浅拷贝------")
#     print("a", a)
#     print("b", b)
# def testDeepcopy():
#     a = [10, 20, [5, 6]]
#     b = copy.deepcopy(a)
#     print("a", a)
#     print("b", b)
#
#     b.append(30)
#     b[2].append(7)
#     print("深拷贝------")
#     print("a", a)
#     print("b", b)
#
# testcopy()
# testDeepcopy()
# f=lambda a,b,c:a+b+c
# print(f(1,3,4))
# a=3
# b=4
# c=eval("a+b")
# print(c)
class Student:
    company="CQUST"
    count=0
    def __init__(self,name,score):
        self.name=name
        self.score=score
        Student.count+=1

    def say_score(self):
        print("{0}的分数是:{1}".format(self.name,self.score))
        print("公司是"+self.company+"num="+str(self.count))

s1=Student("曾yi凯",99)
s2=Student("曾yi凯",99)
s3=Student("曾yi凯",99)
s1.name="曾二凯"
s1.company="QQ"
s1.age=25
s1.say_score()
s1.say_score()

# a=(1,2,3,4,5)
# b=(6,7,8)
# c=[]
# for i in zip(a,b):
#     c.append(i)
# print(c)

