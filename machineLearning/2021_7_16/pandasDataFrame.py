import pandas as p
import numpy as np


# print(p.DataFrame(np.random.randn(2,3)))
socre=np.array(np.random.randint(40,90,size=(10,5)))
subjects=["语文","数学","英语","化学","物理"]
stu=["同学%s"%i for i in range(socre.shape[0])]
print(stu)
socre_df=p.DataFrame(socre,columns=subjects,index=stu)
# print(socre_df.T.T)
# print(socre_df.index)
# print(socre_df.shape)
# print(socre_df.columns)
# print(socre_df.head())
stu=["同学_%s"%i for i in range(socre.shape[0])]
socre_df.index=stu

print(socre_df.reset_index(drop=True))
print("-------------------------------")
df=p.DataFrame({"month":[1,4,7,9],
               "year":[2012,2014,2013,2014],
               "sale":[55,40,84,31]})
print(df)
#set the first col index by the specific col
print(df.set_index("year"))
df=df.set_index(["year","month"])
print(df.index.names)
print(df.index.levels)
print("--------------MultiIndex---------------------")
arrays=[[1,1,2,2],["r","b","r","b"]]
print(p.MultiIndex.from_arrays(arrays,names=("num","col")))
print("------------------------------------------------------------------------")

