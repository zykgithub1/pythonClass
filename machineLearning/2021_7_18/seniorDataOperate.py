import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
moive=pd.read_csv("data/IMDB-Movie-Data.csv")
# # print(np.all(pd.notnull(moive)))
# data=moive.dropna()
# # print(np.all(pd.notnull(moive)))
# data_t=data["Revenue (Millions)"]
# me_num=data_t.mean()
# print(me_num)
# data_t.fillna(data_t.mean(),inplace=True)
# print(data)
for i in moive.columns:
    if np.any(pd.isnull(moive[i]))==True:
        print(i)
        moive[i].fillna(moive[i].mean(),inplace=True)
print(np.all(pd.notnull(moive)))
print(np.any(pd.isnull(moive)))
for i in moive.columns:
    if np.any(pd.isnull(moive[i]))==True:
        print(i)

