#测试可调用方法
#
# class SalaryAccout:
#     '''计算工资'''
#     def __init__(self,salary):
#         self.salary=salary
#     def __call__(self):
#         print("算工资啦")
#         yearSalary=self.salary*12
#         daySalary=self.salary/22.5
#         hourSalary=daySalary/8
#         return dict(yearSalary=yearSalary,monthSalary=self.salary,daySalary=daySalary,hourSalary=hourSalary)
#     def countSalary(self):
#         print("算工资啦")
#         yearSalary=self.salary*12
#         daySalary=self.salary/22.5
#         hourSalary=daySalary/8
#         return dict(yearSalary=yearSalary,monthSalary=self.salary,daySalary=daySalary,hourSalary=hourSalary)
#     def countSalary(self,salary):
#         print("算工资啦")
#         yearSalary=salary*12
#         daySalary=salary/22.5
#         hourSalary=daySalary/8
#         return dict(yearSalary=yearSalary,monthSalary=salary,daySalary=daySalary,hourSalary=hourSalary)
#
# zyk=SalaryAccout(30000)
# print(zyk.__call__())
#
# print(zyk.countSalary(30000))
class Person:
    def work(self):
        print("努力学习")

def paly(s):
    print(str(type(s))+"在玩游戏")

# pp=Person
# pp.palyGame=paly;
# zyk=pp()
# zyk.work()
# pp.palyGame("zyk")

Person.palyGame=paly
zyk=Person()
zyk.work()
zyk.palyGame()


