import pandas as pd

#csv
# data=pd.read_csv("./data/stock_day.csv",usecols=["open","close"])
#
# data.to_csv("test.csv",columns=["close"],index=False)
#
# print(pd.read_csv("test.csv"))

#json
data=pd.read_json("data/Sarcasm_Headlines_Dataset.json",orient="records",lines=True)
print(data.head())
data.to_json("test_json.json",orient="records",lines=True)


