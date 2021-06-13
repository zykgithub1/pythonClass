class photo:
    def calculoater(self):
        raise NotImplementedError
import math
class Circle(photo):
    def __init__(self,r):
        self.r=r

    def calculoater(self):
        return self.r**2*math.pi

class Angle(photo):
    def __init__(self,len,width):
        self.len=len
        self.width=width
    def calculoater(self):
        return self.len*self.width
class pic_manager:
    def cal(self,pic):
        if not isinstance(pic,photo):
            raise ValueError("不是图形")
        return pic.calculoater()
manager=pic_manager()
ang1=Angle(10,20)
cir1=Circle(10)
ans=manager.cal(ang1)
print(ans)
