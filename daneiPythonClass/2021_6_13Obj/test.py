class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

class Player:
    def __init__(self,atk):
        self.atk=atk

    def attack(self,other):
        other.damage(self.atk)


class Enemy:
    def __init__(self,hp):
        self.hp=hp

    def damage(self,value):
        self.hp-=value
        if self.hp<0:
            self.__death()

    def __death(self):
        print("死亡")
        print("掉装备")
        print("加分")


def main():
    p01=Player(10)
    e01=Enemy(1000)
    while(e01.hp>=0):
        p01.attack(e01)
    pass


if __name__ == "__main__":
    main()
    pass
