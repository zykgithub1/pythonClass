import numpy as np
"""
logistical calculation
"""
#(min,max,size(row,col))
socre=np.random.randint(40,100,(10,5))
print(socre)
test_socre=socre[6:,:3]
print(type(test_socre>60))
# test_socre[test_socre>60]=1
print(test_socre)
"""commen judge function
"""
temp=socre[:4,:4]
# temp=np.where(np.logical_and(temp>60,temp<80),1,0)
print(temp)
print(np.mean(temp))
print(np.argmax(temp),"max")
print(temp[-2:,3],"15")
# print(np.all(socre[0:1,:3]>55))
# print(np.where(np.logical_and(socre>50,socre<90),socre,0))
"""counte calculate
   axis=0 ->col     axis=1  ->row 
"""
temp=socre[:4,:]
print(temp)
print(np.max(temp),np.argmax(temp))
print(np.max(temp,axis=0))
print(np.max(temp,axis=1))
print(np.mean(temp))
