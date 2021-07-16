import pandas as p
import numpy as np
"""
create Series(one_dimensional array)
"""
str_1=p.Series(["haha","ea"])
print(str_1)
print(p.Series(np.arange(9)))
print("-------------!!!!!!this------------------")
print(p.Series([1.2,2.3,3.4,4.5,5.0],index=range(len([1.2,2.3,3.4,4.5,5.0]))))
print("--------------------------------")
color_count=p.Series({"red":"what","blue":20,"yellow":30})
print(type(color_count.index))
print(color_count.values)
print("0000-----000")
print(color_count["red":],"!!!")


