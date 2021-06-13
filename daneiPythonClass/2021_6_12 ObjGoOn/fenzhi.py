# class Class:
#     def __init__(self,age):
#         self.age=age
#
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,age):
#         if age>12:
#             raise ValueError("false")
#         self.__age=age
#     pass
# c1=Class(13)
# print(c1.age)
# class Car:
#     def run(self,str_position):
#         print("行驶到:",str_position)
#
# p1=Person("老张")
# car=Car()
# p1.drive(car,"东北")
class Person:
    def __init__(self,name,money):
        self.name=name
        self.money=money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    def getMoney(self,bank,value):
        bank.draw_money(self,value)

class Bank:
    def __init__(self,name,money):
        self.name=name
        self.money=money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    def draw_money(self,person,value):
        print("person的钱最开始为",person.money)
        print("bankd的钱最开始为", self.money)
        self.money-=value
        person.money+=value
        print("取钱后person", person.money)
        print("bankd取钱后", self.money)

xm=Person("小明",0)
zsyh=Bank("招商",100000)
xm.getMoney(zsyh,1000)

