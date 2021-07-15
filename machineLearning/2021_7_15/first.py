import matplotlib.pyplot as p
from pylab import mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False
x=[1,2,3,4,5,6,7]
y=[5,4,7,9,8,2,4]
p.figure(figsize=(20,8),dpi=100)
p.scatter(x,y)
p.show()
