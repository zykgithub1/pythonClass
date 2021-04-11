import copy
class MibblePhone:
    def __init__(self,CPU,Screen):
        self.CPU=CPU
        self.Screen=Screen
class CPU:

    def caculate(self):
        print("计算")
class Screen:
    def show(self):
        print("显示屏幕")
c1=CPU()
s1=Screen()
print("浅赋值")
m1=MibblePhone(c1,s1)
m2=copy.copy(m1)
print(m1,m1.CPU,m1.Screen)
print(m2,m2.CPU,m2.Screen)

print("深复制")
m3=copy.deepcopy(m1)
print(m3.CPU,m3.Screen)
print(m1.CPU,m1.Screen)


