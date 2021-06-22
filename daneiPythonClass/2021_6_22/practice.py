list01=([1,1,1],[2,2],[3,3,3,3,3,3])
# compa=0
# ans=max(filter(lambda compa,p:max(len(p),compa),list01))
# lens=filter(lambda item:len(item),list01)
# ans=0
# for it in lens:
#     ans=max(len(it),ans)
# print(ans)
ans=max(list01,key=lambda item:len(item))
print(len(ans))