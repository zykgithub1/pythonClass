"""
如果有list01
而后新建个List02=list01
修改list01的值会修改list02  因为List02指向list01的指向

但是通过list01切片 得到的list02
虽然list01中的元素和 list02中元素指向相同 (list01[0]和List02[0]指向的元素相同)
但是修改01不会影响02  因为list02是01新的copy的地址  不是指向的01的指向

如果是list01=list02  就会影响
但是简单数据类型不会 因为简单数据类型都是新建对象

->浅拷贝只复制一层~~~
->深拷贝 全部复制（所有深层变量）

列表注意 直接赋值02=01 和02=01.copy 不一样
"""
import copy
def fun1():
    list01 = ["张无忌", "曾易凯"]
    list02 = list01
    list01[0] = "曾二凯"
    a = 10
    b = a
    a = 20
    print(b)
    print(list02[0])

def fun3():
    list01=[500,800]
    list02=list01[:]
    print(id(list01[0]),"lis01-<01")
    print(id(list02[0]),"lis02->01")
    list01[0]=555
    print(list01[0],list02[0])
    list01=[600]
    print(list02)
    list03 = list02.copy()
    print("lis03" ,list03)
    pass

def fun2():
    list01 = ["张无忌", "曾易凯"]
    list02=list01
    list01=["Haha "]
    print(list01)
    list03=list02.copy()
    print("lis03"+list03)
    pass
#浅拷贝 拷贝不进列表里面的复杂元素类型
def fun4():
    print(chr(12))
    list01=[800,[1000,500]]
    list02=list01
    print(id(list01))
    print(id(list02))
    print("修改前地址",id(list01[1][0]))
    list01[1][0]=900
    print("修改后地址",id(list01[1][0]))
    print(list02[1][0])
    print("修改后地址", id(list02[1][0]))
    pass
#浅拷贝：这是切片copy的list02
#没有拷贝List01里面的list[1]（列表）
#而是还是用的这个地址
def fun5():
    print(chr(12))
    list01=[800,[1000,500]]
    list02=list01[:]
    print(id(list01))
    print(id(list02))
    print("修改前地址",id(list01[1][0]))
    list01[1][0]=900
    print("修改后地址",id(list01[1][0]))
    print(list02[1][0])
    print("修改后地址", id(list02[1][0]))
    pass
def fun6():
    list01 = [800, [1000, 500]]
    list02 = copy.deepcopy(list01)
    print(id(list01))
    print(id(list02))
    print("修改前地址", id(list01[1][0]))
    list01[1][0] = 900
    print("修改后地址", id(list01[1][0]))
    print(list02[1][0])
    print("修改后地址", id(list02[1][0]))
    pass

def fun7():
    list01=[1,2,3,4,5,6,7]
    list02=copy.deepcopy(list01)
    list01[0]=1111
    print(list02[0])

if __name__=="__main__":
    fun7()
    pass
