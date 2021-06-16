class Skill:
    pass

class SkillIterartor:
    def __init__(self,skills):
        self.__skills=skills
        self.__index=-1
    def __next__(self):
        if self.__index>len(self.__skills)-1:
            raise StopIteration
        else:
            self.__index += 1
            return self.__skills[self.__index]


class SkillManager:
    def __init__(self):
        self.__skilllist=[]

    def addSkill(self,skill):
        self.__skilllist.append(skill)

    def __iter__(self):
        return SkillIterartor(self.__skilllist)
manager=SkillManager()
for i in range(3):
    manager.addSkill(Skill())
itrator=manager.__iter__()
while True:
    try:
        item=itrator.__next__()
        print(item)
    except:
        break
