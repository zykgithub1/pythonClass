# score=int(input("请输入分数"))
# while(score>100 or score<0):
#     score=int(input("请输入分数"))
# else:
#     if score>=90:
#         grade='A'
#     elif score>=80:
#         grade='B'
#     elif score>=70:
#         grade='C'
#     elif score>=60:
#         grade='D'
#     else:
#         grade='e'
#     print("分数是{0},等级是{1}".format(score,grade))
#
# score=int(input("请输入分数"))
# degree="ABCDE"
# while(score>100 or score<0):
#     score=int(input("请输入分数"))
# num=score//10
# if num<6:
#     num=5
# print(num,degree[9-num])
# d={"name":"曾以凯",'age':"18","job":"programer"}
# for k in d.items():
#     print(k[0])

# a=range(1,100)
# a=list(a)
# for i in a:
#     print(i)
# print(a[0])

# tb=[]
# a=dict
# a=tuple
#
# r1=dict(name="高效益",age=18,salary=10000,city="cq")
# r2=dict(name="高效2",age=19,salary=30000,city="cq")
# r3=dict(name="高效3",age=28,salary=3000,city="cq")
# tb=[r1,r2,r3]
# for x in tb:
#     if x.get('name')is not "高效益":
#         print(x)
#     else:
#         print("工资小于30000")
# a=[x*2 for x in range(5)if x%2==0]
# print(a)
# a.extend([0,0,0,0,11,1,2,3,4,5,6])
# a.append(19)
# print(a)
# b=a.count(0)
# print(b)
# print(a[::5])
# a.sort(reverse=True)
# # print(sum(a).bit_length())
# a=[]
# a=[
#     ["增益开",18,['北京']],
#     ['e',18,90],
#     ["haha"]
# ]
# for x in a:
#     print(x)
# print(len(a[2]))
# a="zy,ke,aa"
# # # b=tuple(a)
# # # print(b)
# # # a=[1,2,3,4]
# # # b=[5,6,7]
# # # c=[8,9,10]
# # # d=list(zip(a,b,c))
# # # print(d)
# a=[1,2,3,4,5,6]
# sum(a)
# print(sum(a))
# while True:
#     a=input("输入字符q,Q结束")
#     if a.upper()=='Q':
#         break
#     else:
#         print(a.upper().isdigit())
