#1(1):采用字典的形式统计每个字母的个数：不用考虑字母加入字典的代码，只考虑字母出现次数的叠加
# chars=['a','c','x','d','p','a','c','a','c','a']
# ans={}
# for i in chars:
#     if i in ans:
#         ans[i]=ans[i]+1
#     else:
#         ans[i]=1
# print(ans)
'''ans2={}
for i in chars:
    if i in ans2:
        continue
    else:
        ans2[i]=chars.count(i)
print(ans2)
test=0
a=''
for i in ans2.keys():
    if ans2[i]>test:
        test=ans2[i]
        a=i
print(test, a)'''
#2输入姓名进行检测，如果不存在则加入列表
'''persons=[{'name':'zhangsan','age':'18'},
{'name':'lisi','age':'20'},
{'name':'wangwu','age':'19'},
{'name':'herry','age':'21'}
]
s=input("输入姓名")
for i in persons:
    if s in i.values():
        print("姓名已存在")
        break
    else:
        age=int(input("请输入年龄"))
        dic={};
        dic["name"]=s
        dic['age']=age
        persons.append(dic)
        break
print(persons)'''
students = [
    {'name': '张三', 'age': 18, 'score': 52, 'tel': '1388888998', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 89, 'tel': '1388666666', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 95, 'tel': '1365588889', 'gender': 'unknown'},
    {'name': 'jerry', 'age': 20, 'score': 90, 'tel': '156666789', 'gender': 'unknown'},
    {'name': 'chris', 'age': 17, 'score': 98, 'tel': '13777775523', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52, 'tel': '13999999928', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 98, 'tel': '1388888888', 'gender': 'unknown'}
]
count=0
kids=0
for student in students:
    if student["score"]<60:
        count+=1;
        print(student["name"]+"不及格，成绩为"+str(student["score"]))
for student in students:
    if student["age"]>18:
        kids+=1
print("未成年人数为"+str(kids)+"  ")
for student in students:
    if student["tel"].endswith('8'):
        print(student["name"]+"的手机尾号为8")
max=0
maxName=" "
for student in students:
    if student["score"]>max:
        max=student["score"]
        maxName=student['name']
print("最优学生是"+maxName+"成绩为"+str(max))
i=0
for student in students:
    if student['gender']is 'unknown':
        students.remove(student)
for student in students:
    print(student,end="\n")