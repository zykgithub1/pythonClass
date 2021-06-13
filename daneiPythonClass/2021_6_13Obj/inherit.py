from abc import *

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.socre=score

class Vehicle:
    @abstractmethod
    def do(self):
        pass
class Car(Vehicle):
    def do(self):
        print("驾驶")
class Airplane(Vehicle):
    pass
s1=Student("zyk",11,400)
a1=Airplane()
a1.do()
c1=Car()
c1.do()