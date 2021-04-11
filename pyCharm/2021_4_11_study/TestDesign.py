class CarFactory:
    def creat_Car(self,brand):
        if brand=="奔驰":
            return Benz()
        elif brand=="BWM":
            return BWM()
        elif brand=="BYD":
            return BYD()
        else:
            return "外形车"

class Benz:
    pass
class BWM:
    pass
class BYD:
    pass
factory=CarFactory()
c1=factory.creat_Car("奔驰")
print(c1)