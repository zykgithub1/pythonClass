class EmployeeMent:
    def __init__(self):
        self.__employees=[]

    def get_total_salary(self):
        total=0
        for it in self.__employees:
            total+=it.calulater()
        return total

    def add_employee(self,emp):
        self.__employees.append(emp)
class Student:
    def __init__(self,name="zyk",age=0,score=0,id=111):
        self.name=name
        self.age=age
        self.score=score
        self.id=id

    def __str__(self):
        return self.name

class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name=name
        self.hp=hp
        self.atk=atk
        self.defense=defense


    def __repr__(self):
        return "Enemy('%s',%d,%d,%d)"%(self.name,self.hp,self.atk,self.defense)
#
# e1=Enemy("zyk",111,11,111)
# # e2=eval(repr(e1))
# # print('e2:',e2)
# print(e1)
# e2=eval(repr(e1))
# print(e2)
list01=[1]
print("list01",id(list01))
re=list01+[2]
print("re",id(re))
list01+=[2]
print("lis01",id(list01))