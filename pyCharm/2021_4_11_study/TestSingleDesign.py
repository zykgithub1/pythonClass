class SingleLeton:
    __obj=None
    __new_Flag=True

    def __new__(cls, *args, **kwargs):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)
        return cls.__obj

    def __init__(self,name):
        if self.__new_Flag:
            self.name=name
            print("init~~~~~~~~")
            SingleLeton.__new_Flag=False

a=SingleLeton("aa")
b=SingleLeton("bb")
c=SingleLeton("cc")
print(a)
print(b)
print(c)