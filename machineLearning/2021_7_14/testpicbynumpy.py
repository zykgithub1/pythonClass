import numpy as np
import matplotlib.pyplot as plt
import random
from pylab import mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False
x=np.linspace(0,10,1000)
y=np.sin(x)
plt.figure(figsize=(20,8),dpi=100)

plt.plot(x,y)
plt.grid(True,linestyle="--",alpha=1)
plt.show()
