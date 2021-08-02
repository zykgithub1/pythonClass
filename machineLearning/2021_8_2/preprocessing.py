from sklearn.preprocessing import MinMaxScaler,StandardScaler
import pandas as pd
data = pd.read_csv("./dating.txt")
def minmax_demo():
    """
    X'= x-min
        -----               X''=X'*(mx-mi)+mi
        max-min
    :return:
    """
    #  instantiation
    transfer=MinMaxScaler(feature_range=(3,5))
    #  fir_transform
    ret_data=transfer.fit_transform(data[["milage","Liters","Consumtime","target"]])
    print(ret_data)

def stand_demo():
    transfer=StandardScaler()
    ret_data=transfer.fit_transform(data[["milage","Liters","Consumtime","target"]])
    print("after standardization:\n",ret_data)
    print("fangcha of each col:->",transfer.var_)
    print("average of each col:->",transfer.mean_)


stand_demo()