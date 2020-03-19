
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

#添加标题

#显示中文
plt.rcParams['font.sans-serif']=[u'SimHei']
# plt.rcParams['axes.unicode_minus']=False

# %matplotlib inline

x=np.arange(0,10)
plt.title('这是一个标题')
plt.plot(x,x**2,color='greenyellow',marker=">")
plt.plot(x,x**3)
plt.plot(x,x**4)
plt.legend(["增长","外国","中国"])
plt.text(6,1000,"这是一个注释")
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.grid()
plt.locator_params('x', nbins=20)
plt.axis(xmin=3,xmax=5,ymin=0,ymax=500)
plt.annotate("备注点",xy=(5.93,1238), xytext=(6,3000),arrowprops={"headwidth":10,"facecolor":"r"})
plt.show()

