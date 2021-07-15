import numpy as np
import random
import matplotlib.pyplot as p
from pylab import mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

# x2=np.random.uniform(-1,1,1000000)
x1=np.random.normal(1,0.1,(3,3))
# print(x1)
# stock_change=np.random.normal(0,1,(4,5))
# print(stock_change)
# print(stock_change.T)
# print(stock_change.reshape([-1,4]))
# stock_change.astype(np.int32)
# print(type(stock_change.astype(np.int32)))
# print(type(stock_change.tostring()[0]))
a=np.array([[1,2,3,4,5],[2,3,4,5,6]])
ans=np.unique(a)
# a=a.tolist()
print(type(list(a)))


# print(stock_change)
# print(stock_change[0,0::])
# p.figure(figsize=(20,8),dpi=100)
# p.hist(x2,100)
# p.show()
