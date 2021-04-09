'''num=input("输入一个数字")
if int(num)>10:
    print(num)
if 3:
    print("ok")'''
"""s=""
print(s if s else "false")"""

'''score=int(input("输入成绩"))
grade=""
if score<=60:
    grade="不及格"
elif score<80:
    grade="良好"
print("成绩为{0}，等级是{1}".format(score,grade))'''
import  random

h=0
while (h)<1000 :
    i = random.uniform(0,1)
    h+=1
    print(i)