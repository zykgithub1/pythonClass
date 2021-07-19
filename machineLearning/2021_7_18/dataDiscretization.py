import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("data/stock_day.csv")
p_change=data["p_change"]
#automatic seperate into group
q_cut=pd.qcut(p_change,10)
# print(q_cut)
# print(q_cut.value_counts())
bins=[-100,-7,-5,-3,0,3,5,7,100]
bins_count=pd.cut(p_change,bins)
# print(bins_count)
# print(bins_count.value_counts())
dummies=pd.get_dummies(bins_count,prefix="rise")
print(dummies)