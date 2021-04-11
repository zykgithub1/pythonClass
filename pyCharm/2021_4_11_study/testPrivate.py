# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#
#     def __word(self):
#         print("goodgood study")
# e=Employee("zyk",25)
# print(e.name,e._Employee__age)
# e._Employee__word()

class Employee:
    @property   #等于getter
    def salary(self):
        print("salary run...")
        return 30000
    @salary.setter
    def salary(self,salary):
        self.salary=salary

e=Employee()
print(e.salary)