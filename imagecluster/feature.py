#coding：utf-8

#获取图像特征

from PIL import Image
from io import BytesIO
from . shape import  Shape
from . grow import Grow
import urllib.request as request
import numpy as np
from . pattern import Pattern


def _index(array,x,y,T):
	"""
	:param x:
	:param y:
	:param T:
	:return:
	"""
	return array[x][y]<T





from . pattern import _point


def _get_m_pattern(counter,scanned,size,fea_n):
	m_pattern = []
	for i in range(counter):
		pattern= Pattern(i, size[0], size[1],fea_n=fea_n)
		m_pattern.append(pattern)
		#t = i + 1 #物理下标转逻辑下标
	for t in range(1,counter+1):
		for h in range(1, size[1] - 1):
			for w in range(1, size[0] - 1):
				if scanned[h][w] == t:
					if m_pattern[t-1].left_top.x > w:
						m_pattern[t-1].left_top.x = w
					if m_pattern[t-1].left_top.y > h:
						m_pattern[t-1].left_top.y = h
					if m_pattern[t-1].right_bottom.x < w:
						m_pattern[t-1].right_bottom.x = w
					if m_pattern[t-1].right_bottom.y < h:
						m_pattern[t-1].right_bottom.y = h
	return m_pattern




def get_feature(path,sca_call=Grow(), fea_call=Shape(),T=128,from_net_timeout=None,
                fea_n = 49,resize=(64,64)):
	"""
	获取指定路径的图片的特征矩阵
	:param path: 图片路径
	:param T 二值阈值
	:param from_net_timeout:给出时会把path当成url进行访问
	:param fea_n 单个特征的长度
	:return: np.array
	"""
	if not hasattr(sca_call, "scan"):
		raise ValueError("the feature call must be implement the IScanner")
	if not hasattr(fea_call,"call_feature"):
		raise  ValueError("the feature call must be implement the Feature")
	if not from_net_timeout:
		image = Image.open(path)
	else:
		r= request.urlopen(path, timeout=from_net_timeout)
		img_data = BytesIO(r.read())
		image= Image.open(img_data)
	image = image.convert("L")
	#缩小图片规模,避免递归过深
	image = image.resize(resize)
	size = image.size  # (w,h)
	img = np.array(image)
	scanned,counter =sca_call.scan(img,T)
	#Image.fromarray(scanned).show()
	m_pattern = _get_m_pattern(counter,scanned,size,fea_n=fea_n)
	to_feature = []
	for i in range(counter):
		#flag是一个标志位，代表真值时，取该物体特征
		flag = fea_call.call_feature(img,m_pattern[i],T)
		if flag :
			to_feature.append(m_pattern[i])
	feature = [pattern.feature for pattern in to_feature]
	return to_feature,np.array(feature)