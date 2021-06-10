"""
容器来管理数据的思想
"""
def fun():
    str=input("输入月份如3月5日")
    # b=str.split("月")
    # print(b)
    month=int(str.split("月")[0])
    day=int(str.split("月")[1].split("日")[0])
    print(month,day)
    day_of_month=(31,28,31,30,31,30,31,31,30,31,30,31)
    ans=0
    for i in range(0,month-1):
        ans+=day_of_month[i]
    ans+=day
    print("这是这一年的第%d天"%ans)
    pass

def fun1():
    dict01={}
    while True:
        name=input("输入商品信息")
        if name =="":
            break
        price = int(input("输入商品价格"))
        dict01[name]=price
    for k,v in dict01.items():
        print(k,":",v)
    pass

def fun2():
    dict01 = {}
    value_dic = {"age":0,"socre":0,"sex":"sex"}
    while True:
        name = input("输入姓名")
        if name == "":
            break
        value_dic["name"] = int(input("输入年龄"))
        value_dic["socre"] = int(input("输入乘机"))
        value_dic["sex"] =input("输入性别")
        dict01[name] = value_dic
    for k, v in dict01.items():
        print(k, ":", v)
    pass

def fun3():
    list01 = []
    value_dic = {"name":"","age":"","socre":0,"sex":"sex"}
    while True:
        name = input("输入姓名")
        if name == "":
            break
        value_dic["name"] = name
        value_dic["age"] = int(input("输入年龄"))
        value_dic["socre"] = int(input("输入乘机"))
        value_dic["sex"] =input("输入性别")
        list01.append(value_dic)
    print(list01)
    pass

def fun4():
    list_ans=[]
    for i in range(1970,2051):
        if i %4==0 and i%100!=0 or i%400==0:
            list_ans.append(i)
    print(list_ans)
    pass

def fun5():
    list_ans=[]
    dic01={"北京":{"景区":["故宫","天安门","天坛"],"美食":["烤鸭","炸酱面","卤煮"]}}
    list_ans.append(dic01)
    print(list_ans)
    pass

def fun6():
    str="abcedf"
    dic_ans={}
    for item in str:
        if item in dic_ans:
            dic_ans[item]+=1;
        else:
            dic_ans[item]=1
    for k,v in dic_ans.items():
        print(k,":",v)
    pass
import copy
def fun7():
    list01=["看书","敲代码","考研"]
    dic_01={"zyk":list01}
    list01.append("锻炼")
    print(id(list01)==id(dic_01["zyk"]))
    print(list01)
    print(dic_01["zyk"])
    list02=copy.deepcopy(list01)
    dic_02={"kyz":list02}
    dic_02["kyz"].append("当然还有啦")
    print(dic_01["zyk"])
    pass

def fun8():
    # dic01={item:item**2 for item in range(1,11) if 8>=item>=5}
    # print(dic01)
    list01=["张无忌","赵敏","周芷若"]
    dic_ans={item:len(item) for item in list01}
    print(dic_ans)
    print("-----------------------")
    list02=[100,101,102]
    ziped=zip(list01,list02)
    # for a,b in ziped:
    #     print(a,":",b)
    dic02={}
    for key,val in ziped:
        print(key,val)
        dic02[key]=val
    print(dic02)
    pass

def fun9():
    s1=set()
    pass
def main():
    fun9()
    pass

if __name__=="__main__":
    main()
    pass