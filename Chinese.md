[English](README.md)

这些是我学习如何识别相似图片的python代码，算法都是我在网络上看到，正在尝试自己一步步的实现。

放在github一是用来记录，二是希望帮助到一些和我一样在识别相似图片方面的初学者。

会在学习期间保持更新。

最终的目的是希望这些算法用在我的爬虫上，用来爬取特定的图片。你也有兴趣的话，欢迎交流
和指点。

点赞神马的当然是最好的。

##脚本目录：

+ ```aHash.py```  &nbsp; 用平均哈希法实现识别相似图片。
+ ```histogram.py``` &nbsp; 用计算直方图实现识别相似图片。
+ ```histogram2.py```&nbsp; 用计算直方图实现识别相似图片。与```histogram.py```的那个不同的是,
他会把图片分隔成16个小块，然后分别比较，最后综合比较结果，从而提高比较的准确率。
+ ```pHash.py``` &nbsp;通过对图片矩阵进行离散余弦变换来识别相似图片，效果有所提高。
+ ```dHash.py ```&nbsp;利用dHash算法进行识别，有人能告诉我dHash的全称叫神马吗？
+ ```face1.py``` &nbsp;基于openCV和Haar特征来识别出人脸的位置。
+ ```face2.py``` &nbsp;在```face1.py```的基础上，判断两张人脸是否相似。

##实验环境

+ [python3.4](https://www.python.org/)
+ [pillow](https://pypi.python.org/pypi/Pillow)
+ [openCV](http://opencv.org/)


<br>
<b>未完待续……</b>
