class GraphicManager:
    def __init__(self):
        self.__graphics=[]

    def add_grahic(self,*args):
        for item in args:
            if isinstance(item, Graphic):
                self.__graphics.append(item)


    def get_total_area(self):
        tatol=0
        for item in self.__graphics:
            tatol+=item.calculate_area()
        return tatol

class Graphic:
    def calculate_area(self):
        raise NotImplementedError

class Circle(Graphic):
    def __init__(self,r):
        self.r=r

    def calculate_area(self):
        return self.r**2*3.14

class Rectangle(Graphic):
    def __init__(self,len,width):
        self.len=len
        self.width=width

    def calculate_area(self):
        return self.len*self.width

manager=GraphicManager()
c1=Circle(1)
ang1=Rectangle(1,1)
c2=Circle(10)
manager.add_grahic(c1,ang1,c2,c2,c2)
ans=manager.get_total_area()
print(ans)