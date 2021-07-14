import matplotlib.pyplot as plt
import random
from pylab import mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False


x=range(60)
y_shanghai=[random.uniform(15,18)for i in x]
y_beijing=[random.uniform(1,3)for i in x]
#设置窗体比例
plt.figure(figsize=(20,8),dpi=100)
#绘制图像
plt.plot(x,y_shanghai,label="上海")
plt.plot(x,y_beijing,color="r",linestyle="--",label="北京")
#show legend
plt.legend(loc="center")
#设置x，y轴刻度
x_tick_lable=["11点{}分".format(i)for i in x]
y_tick=range(40)
#修改x,y 坐标刻度显示
#坐标刻度不可直接字符串更改
plt.xticks(x[::5],x_tick_lable[::5])
plt.yticks(y_tick[::2])
#添加网格显示
plt.grid(True,linestyle="--",alpha=1)
#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("中午11点-12点某城市温度变化图",fontsize=30)
#保存在当前目录下
plt.savefig("./test.png")
plt.show()