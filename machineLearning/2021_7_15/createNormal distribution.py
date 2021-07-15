import numpy as np
import random
import matplotlib.pyplot as p
from pylab import mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

#create random array(average   standard deviation   nums)
# x1=np.random.normal(1.75,5,10000000)
# p.figure(figsize=(20,8),dpi=100)
# p.hist(x1,1000)
# p.show()
y=range(10)
# stock_change=np.random.normal(0,1,20)
stock_change=[]
for i in y:
    stock_change.append(random.random())
p.figure(figsize=(20,8),dpi=100)
p.plot(stock_change,y[::1])
p.show()