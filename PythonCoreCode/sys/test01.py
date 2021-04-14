"""
哪些模块可以被引入
sys.path.append(\\=/)
被引入的模块更新问题
"""
import sys
from abc import ABCMeta,abstractmethod
def toBin(c):
    c=c//1
    ans=[]
    while(c !=0):
        ans.append(str(c%2))
        c//=2
    # for a in ans:
    #     if a=='0':
    #         ans.remove(a)
    ans=list(reversed(ans))
    ans2="0b"
    for a in ans:
        ans2+=a
    return ans2
print(toBin(0))
print(bin(0))
print(int("0b1000000",2))

print(2>>10)
print(int("0o17",8))
print(oct(1000))
class student:
    @abstractmethod
    def wh(self):
        pass
    

    __name=10
print(dir(student))
print(student._student__name)
print(student.__mro__)