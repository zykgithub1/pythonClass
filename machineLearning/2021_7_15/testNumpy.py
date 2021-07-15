import numpy as np
import random,time
# socore = np.array([[1, 2, 3, 4],
#                    [4, 5, 6, 5],
#                   [1, 2, 3, 4],
#                   [4, 5, 6, 5]])
# print(socore)
a=[]
for i in range(10000000):
    a.append(random.random())
start=time.time()
sum1=sum(a)
endtime=time.time()
print("cost=",str(endtime-start))

start=time.time()
b=np.array(a)
num2=sum(a)
endtime=time.time()
print("cost=",str(endtime-start))