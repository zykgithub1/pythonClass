import numpy as np
"""
array's calculation
"""
arr=np.array([[1,2,3,2,1,4],[5,6,1,2,3,1]])
arr1=np.array([[1,2,3,2,1,4],[5,6,1,2,3,1]])
ma=np.matrix([[1,2,3],[2,3,4]])
ma1=np.matrix([[1,2],[3,4],[5,6]])
print(ma,ma1,ma*ma1)
print(arr+arr1)
print(arr*arr1)
arr=np.array([[1,2,3,2,1,4],[5,6,1,2,3,1]])
arr1=np.array([[1],[3]])
print(arr.shape,arr1.shape,arr1.size)
print(arr*arr1)