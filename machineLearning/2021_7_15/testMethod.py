import numpy as np
import random,time
socore = np.array([[[[1, 2, 3, 4],
                   [4, 5, 6, 5],
                  [1, 2, 3, 4],
                  [4, 5, 6, 5]],
                   [[1, 2, 3, 4],
                   [4, 5, 6, 5],
                  [1, 2, 3, 4],
                  [4, 5, 6, 5]]],[[[1, 2, 3, 4],
                   [4, 5, 6, 5],
                  [1, 2, 3, 4],
                  [4, 5, 6, 5]],
                   [[1, 2, 3, 4],
                   [4, 5, 6, 5],
                  [1, 2, 3, 4],
                  [4, 5, 6, 5]]]])
# print(socore.shape)
# print(socore.ndim)
# print(socore.size)
# print(socore.itemsize)
# print(socore.dtype)
#
# ones=np.ones([4,8])
# ones_like=np.ones_like(ones)
# print(ones)
# print(ones_like)
one=np.linspace(0,100,9)
print(one)
two=np.logspace(0,5,6)
print(two)
#(start,endm,num）
print(np.linspace(9,10,11))
print(np.arange(0,50,2))