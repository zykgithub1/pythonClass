class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name,other.name)
        else:
            return "Not the Same"
    def __str__(self):
        return "name"+str(self.name)+"age"+str(self.age)

zyk=Person("增益开",25)
zyk2=Person("曾2凯",23)
zyk3=Person("曾3凯",24)
c=zyk+zyk2
print(zyk)
print(zyk.__dict__)
print(zyk.__class__)
print(Person.__bases__)
print(Person.mro())
print(dir(Person))
print(dir(zyk))