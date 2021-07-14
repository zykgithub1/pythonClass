import matplotlib.pyplot as plt
import random
from pylab import mpl
"""
图对象绘图
"""
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 3) for i in x]
# 设置窗体比例
# plt.figure(figsize=(20,8),dpi=100)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

# 绘制图像
axes[0].plot(x, y_shanghai, label="上海")
axes[1].plot(x, y_beijing, color="r", linestyle="--", label="北京")
#添加刻度
x_tick_lable=["11点{}分".format(i)for i in x]
y_tick=range(40)
#修改x,y 坐标刻度显示
#坐标刻度不可直接字符串更改
axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_tick[::5])
axes[0].set_xticklabels(x_tick_lable[::5])
axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_tick[::5])
axes[1].set_xticklabels(x_tick_lable[::5])
axes[0].grid(True,linestyle="--",alpha=1)
axes[1].grid(True,linestyle="--",alpha=1)
axes[0].set_xlabel("时间")
axes[0].set_ylabel("温度")
axes[0].set_title("中午11点-12点某城市温度变化图",fontsize=20)
axes[1].set_xlabel("时间")
axes[1].set_ylabel("温度")
axes[1].set_title("中午11点-12点某城市温度变化图",fontsize=20)
axes[0].legend(loc=0,fontsize=20)
axes[1].legend(loc=1)
plt.savefig("./test.png")
plt.show()
