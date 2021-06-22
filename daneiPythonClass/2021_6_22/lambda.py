# b=lambda item:item//10*7
# print(b(10))
#

from test import Enimy
mieba=Enimy("mieba",101,10010,1000)
jiutoushe=Enimy("九头蛇",101,1010,200)
small_guaiwu1=Enimy("小怪兽",10,40,40)
big_guaishou=Enimy("成昆",10,40,40)
enimy_list=[mieba,jiutoushe,small_guaiwu1,big_guaishou]
info=map(lambda item:(item.name,item.blood),enimy_list)
for it in info:
    print(it)
alives=filter(lambda item:item.attack>100 and item.blood>10,enimy_list)
for it in alives:
    print(it)
map()

# ans=filter(lambda item:item.blood<=10,enimy_list)
# for item in ans:
#     print(item)
#map  映射

# ans=map(lambda item:item.attack,enimy_list)
# ans2=map(lambda item:item.attack,enimy_list)
# print(max(ans))
# print(min(ans2))
# for item in ans:
#     print(item)
# arr=[10,9,8,4,11,3,2,19]
# arr1=[10,9,8,4,11,3,2,19]
# arr.sort()
# arr1=sorted(arr1)
# print(arr)
# print(arr1)
# arr1.sort(reverse=True)
# print(arr1)





