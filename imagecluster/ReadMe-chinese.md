##Scripts

[English](ReadMe.md)

+ imagecluster 

  +  feature_interface
	 封装了两个接口，一个是用于扫描物体的```IScanner```接口，一个是用于提取特征的```Feature```接口

  +  grow  
    利用区域生长的方法扫描物体
  
  +  shape
   通过求导的方法粗略判断物体的特征
  
  +  blackpoint
   通过物体的黑点数来判断物体的特征
  
  +  pattern
   用于描述物理的类
  
  +  feature 
   装有可用于本地或网络获取图片并提取特征的函数
  
  +  calculate
   装有计算相似度的```similar```类


+  ```example.py```
   按照区域生长方法获取物体位置，然后按照物体轮廓获取特征，最后用欧式距离判断相似度。
   在判读物品相似度后将相似物品标出。
   <br/>
  <img src="demo.jpg" style="width:725px"/>
  before
  <br/>
  ![after](after.jpg)
  after