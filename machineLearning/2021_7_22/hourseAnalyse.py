import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#get file
file_data=pd.read_csv("lianjia.csv")
#delete duplicate
file_data=file_data.drop_duplicates()
file_data=file_data.dropna()

#area squart convert into double
data_new=np.array([])
data_area=file_data["面积(㎡)"].values
# print(type(data_area[0]))
for i in data_area:
    data_new=np.append(data_new,float(np.array(i[:-2])))
file_data.loc[:,"面积(㎡)"]=data_new
house_data=file_data["户型"]
# print(house_data)
templist=[]
for i in house_data:
    new_info=i.replace("房间","室")
    templist.append(new_info)
file_data.loc[:,"户型"]=templist

new_df=pd.DataFrame({"区域":file_data["区域"].unique(),"数量":0*13})
area_count=file_data.groupby(by="区域").count()
# print(area_count)
new_df["数量"]=area_count.values
new_df=new_df.sort_values(by="数量",ascending=False)
# print(new_df)
# house style analyse
house_data=file_data["户型"]

def all_house1(arr):
    arr=arr.sort_values()
    all_style=arr.values
    result={}
    for k in all_style:
        if k not in result:
            result[k]=1
        else:
            result[k]+=1
    return result
def all_house(arr):
    key=np.unique(arr)
    result={}
    for k in key:
        mask=(arr==k)
        arr_new=arr[mask]
        # print(arr_new)
        v=arr_new.size
        result[k]=v
    return result
house_info=all_house(house_data)
house_type=dict((key,values)for key,values in house_info.items() if values>50)
house_info=pd.DataFrame({'户型':[x for x in house_type.keys()],"数量":[x for x in house_type.values()]})
print(house_info)

plt.show()
#delete small num

