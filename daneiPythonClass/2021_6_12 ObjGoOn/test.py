class Vecter:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    @staticmethod
    def left():
        return Vecter(0,-1)
    @staticmethod
    def rigth():
        return Vecter(0,1)

    @staticmethod
    def up():
        return Vecter(-1, 0)

    @staticmethod
    def down():
        return Vecter(1, 0)

class DoubleListHelper:
    @staticmethod
    def getElemt(target,vect_pos,vect_dir,count):
        result=[]
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            result.append(target[vect_pos.x][vect_pos.y])
        return result

class Enimy:
    def __init__(self,name,blood,attack,offend):
        self.name=name
        self.blood=blood
        self.attack=attack
        self.offend=offend

    def action(self):
        print("姓名：%s,血量: %d ,attack :%d offend :%d"%(self.name
        ,self.blood,self.attack,self.offend))

class Enimy_managerment:
    def __init__(self,enimy_list):
        self.enimy_list=enimy_list

    def findByName(self,target):
        for item in self.enimy_list:
            if item.name==target:
                return item
        print("未找到该敌人")

    def findDead(self):
        ans=[]
        for item in self.enimy_list:
            if item.blood<=0:
                ans.append(item)
        return ans

    def calulateAttackAvg(self):
        total=0
        for item in self.enimy_list:
            total+=item.attack
        return total/len(self.enimy_list)

    def findWeaker(self):
        for i in range(len(self.enimy_list)-1,-1,-1):
            if self.enimy_list[i].offend<=100:
                self.enimy_list.remove(self.enimy_list[i])

    def strongAll(self,target):
        for item in self.enimy_list:
            item.attack+=target

    def showEnimyList(self):
        print("遍历")
        for it in self.enimy_list:
            it.action()

def fun():
    # ans=DoubleListHelper.getElemt(list01,Vecter(1,3),Vecter.left(),3)
    # print(ans)
    mieba=Enimy("mieba",100,1000,1000)
    jiutoushe=Enimy("九头蛇",100,100,200)
    small_guaiwu1=Enimy("小怪兽",10,40,40)
    big_guaishou=Enimy("小怪兽",10,40,40)
    enimy_list=[mieba,jiutoushe,small_guaiwu1,big_guaishou]
    manage=Enimy_managerment(enimy_list)
    manage.showEnimyList()
    ans1=manage.findByName("mieba")
    print("找灭吧")
    ans1.action()
    ans2=manage.findDead()

    if ans2!=[]:
        print("死亡敌人：")
        for it in ans2:
            it.action()
    else:
        print("没有死亡敌人")
    ans3=manage.calulateAttackAvg()
    print("avg Ataack",ans3)
    manage.findWeaker()
    manage.strongAll(50)
    manage.showEnimyList()
    print(manage.__dict__)
    pass

list01=[
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]

if __name__=="__main__":
    fun()
    pass