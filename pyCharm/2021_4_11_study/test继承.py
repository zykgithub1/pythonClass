class Person:

    def __init__(self,name,age):
        self.name=name
        self.__age=age
class Student(Person):

    def __init__(self,name,age,school):
        Person.__init__(self,name,age)
        self.school=school

zyk=Student("曾易凯",20,"cqust")
print(zyk.name,zyk._Person__age,zyk.name)
print(Student.mro())
print(dir(zyk))