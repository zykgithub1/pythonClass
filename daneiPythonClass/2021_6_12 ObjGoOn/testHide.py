class Wife:
    def __init__(self,name,age,weight):
        self.name=name
        self.set_age(age)
        self.__weight=weight


    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

    name = property(get_name, set_name)
    def set_age(self,age):
        if age<=30:
            print("age=:",age)
            self.__age=age
            pass
        else:
            raise ValueError("NO")

w1=Wife("林志玲",21,33)
# print(w1.__age)
print(w1.__dict__)