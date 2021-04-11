class CarFactory:
    __obj=None
    __new_flag=True

    def __new__(cls, *args, **kwargs):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)
        return cls.__obj

    def __init__(self,name):
        if CarFactory.__new_flag:
            self.name=name
            print("init~~~~~")
            CarFactory.__new_flag=False
fa1=CarFactory("汽车梦工厂")
fa2=CarFactory("五菱宏光")
fa3=CarFactory("长安福特")
print(fa1)
print(fa2)
print(fa3)