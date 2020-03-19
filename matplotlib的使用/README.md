#  `matplotlib`简单操作

`matplotlib.pyplot`是一个命令风格函数的集合，使`matplotlib`的机制更像 MATLAB。 每个绘图函数对图形进行一些更改：例如，创建图形，在图形中创建绘图区域，在绘图区域绘制一些线条，使用标签装饰绘图等。

```python
import matplotlib.pyplot as plt
```

以别名方式导入`pyplot`。

##  设置中文标题  

`pyplot`的默认字体并不支持中文，如果需要支持中文则通过以下命令更换为支持中文的字体。

```python
plt.rcParams['font.sans-serif'] = [u'SimHei']
```



##  添加注释  

可以通过`plt.text(x,y,"注释信息")`为绘制的图添加注释，第一二个参数代表注释的坐标位置，第三个参数为要注释的信息。  



##  添加备注点

`matplotlib.pyplot.annotate()`可以为绘制的坐标线添加要注释的点,例

```python
plt.annotate("备注点",xy=(5.93,1238), xytext=(6,3000),arrowprops={"headwidth":10,"facecolor":"r"})
```

表示设置了一个红色箭头指向坐标为（5.93,1238）的点，另外注释信息为"备注点"，注释的坐标位置为（6,3000），`arrowprops`显然是在为箭头设置样式。  



##  设置X轴，Y轴名称  

使用`plt.xlabel()`和`plt.ylabel()`设置X轴与Y轴的名称。  



##   添加图例

可以使用`plt.legend()`为坐标轴上每条线添加每条线的名称，例`plt.legend(["线1","线2","线3"])`  



##  改变坐标轴上线条色彩  

在绘制每条线时可以为线条添加`color`参数为线条设置颜色。

```python
plt.plot(x,color="red")
```



##  线条样式  

在绘制线条时，可以为`plot`传入一个参数`marker`用于设置线条样式。

```python
plt.plot(x,marker='o')
plt.plot(x+1,marker='>')
plt.plot(x+2,marker='s')
```



##  数学公式  

`matplotlib`支持`LaTEX`的数学公式，在设置注释时可以使用`LaTEX`显示数学公式

```python
plt.text(2,4,r'$ \alpha \beta \pi \lambda \omega $',size=25)
plt.text(4,4,r'$ \sin(0)=\cos(\frac{\pi}{2}) $',size=25)
plt.text(2,2,r'$ \lim_{x \rightarrow y} \frac{1}{x^3} $',size=25)
plt.text(4,2,r'$ \sqrt[4]{x}=\sqrt{y} $',size=25)
```

$\alpha \beta \pi \lambda \omega$

$$ \sin(0)=\cos(\frac{\pi}{2}) $$

size表示字号大小



##  设置网格  

`plt.grid()`可以为坐标轴设置网格样式，网格的样式可以通过`grid()`的参数进行调整。  



##  调整坐标轴刻度  

同时调整x轴和y轴：`plt.locator_params(nbins=20)`

只调整x轴：`plt.locator_params('x',nbins=20)`

只调整y轴：`plt.locator_params('y',nbins=20)`  

`nbins`表示坐标轴的刻度是20个。  



##  调整坐标轴范围  

`xlim`：对应参数有`xmin`和`xmax`，分别能调整最大值最小值

`ylim`与`xlim`参数相同， 

`plt.axis()`,4个数字分别代表x轴和y轴的最小坐标，最大坐标,即`plot.xlim()`与`plt.ylim()`的简写模式。  

##  切换样式`-plt.style.use`  

可以输入`plt.style.available`,再通过类似`plt.style.use('ggplot')`这样的语句切换样式。（注：`ggplot`是一种样式，这里举个例子）  



