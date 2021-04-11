# class Student:
#     name="ZYK"
#     def __init__(self,name1):
#         self.name1=name1
#     @classmethod
#     def printName(cls):
#         print(cls.name)
#     def printName1(self):
#         print(self.name1)
# s1=Student("selfZyk")
# s1.printName()
# Student.printName1(s1)
# s1.printName1()
def sum(a,b):
    return a+b
str="sum(10,20)"
c=eval(str)
print(c)