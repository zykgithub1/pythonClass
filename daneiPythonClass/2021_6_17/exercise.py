def my_enumerate(list01):
    # i=0
    # for item in list01:
    #     yield (i,item)
    #     i+=1
    for i in range(len(list01)):
        yield (i,list01[i])
list01=[3,4,55,6]
list02=["孙悟空","曾驿凯","凯撒","拿破仑"]
list03=["如来","苍天","大地","君主"]
for item in my_enumerate(list01):
    print(item)

def my_zip(*args):
    index=0
    minIndex=len(args[0])
    for item in args:
        minIndex=min(minIndex,len(item))
    for i in range(minIndex):
        ans = []
        for j in range(len(args)):
            ans.append(args[j][i])
        yield tuple(ans)

# for item in my_zip(list01,list02,list03):
#     print(item)
class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id=id
        self.name=name
        self.atk_ratio=atk_ratio
        self.duration=duration

list_skill=[
    SkillData(101,"乾坤",5,10),
    SkillData(102,"降龙",8,5),
    SkillData(103,"葵花",10,2),
]
def get_ratio():
    for item in list_skill:
        if item.atk_ratio>=6:
            yield item
