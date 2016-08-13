#coding:utf-8

#提取图像边缘
from . feature_interface import Feature
import numpy as np
from . pattern import Pattern
import scipy.signal as signal
from PIL import Image

"""
先提取图像边缘，
在分别求导，按一定顺序组成特征数组
"""

class Shape(Feature):


	def __init__(self,sigma=1):
		self._sigma = sigma


	# # 生成高斯算子的函数
	def _gauss(self,x,y,sigma):
		return 100*(1/(2*np.pi*sigma))*np.exp(-((x-2)**2+(y-2)**2)/(2.0*sigma**2))

	def _shape(self,img):
		"""
		接受一个图片数组，锐化后返回
		:param img:
		:return: 图片数组
		"""

		operator1 = np.fromfunction(self._gauss, (5, 5), sigma=self._sigma)
		operator2 = np.array([[1, 1, 1],
		                   [1,-8, 1],
	                       [1, 1, 1]])
		image_blur = signal.convolve2d(img, operator1, mode="same")
		# 对平滑后的图像进行边缘检测
		image2 = signal.convolve2d(image_blur, operator2, mode="same")
		if image2.max() != 0:
			image2 = (image2 / float(image2.max())) * 255
		else:
			image2 = np.zeros(image2.shape)
		# 将大于灰度平均值的灰度值变成255（白色），便于观察边缘
		image2[image2>image2.mean()] = 255
		# 其余变成黑色，便于观察边缘
		image2[image2 <=image2.mean()] =0
		return image2

	def call_feature(self, img: np.ndarray, pattern: Pattern, T):
		sub_img = img[pattern.left_top.x:pattern.right_bottom.x+1,
		          pattern.left_top.y:pattern.right_bottom.y+1]
		img_edge = self._shape(sub_img)
		h,w = img_edge.shape

		#Image.fromarray(img_edge).show()
		points = [] #记录物体的黑点即边缘
		for _h in range(h):
			for _w in range(w):
				if img_edge[_h][_w] == 0:
					points.append((h,w))
		try:
			top_point = min(points,key=lambda x:x[0])
			bottom_point = max(points, key=lambda x: x[0])
			left_point = min(points, key=lambda x: x[1])
			right_point = max(points, key=lambda x: x[1])
		except:
			#print(img_edge)
			return False

		left_top_point = right_top_point= left_bottom_point = right_bottom_point = (0,0)
		for _h,_w in points:
			if left_point[0]>_h>top_point[0] and top_point[1]>_w>left_point[1]:
				left_top_point = (_h,_w)
			elif right_point[0]>_h>top_point[0] and right_point[1]>_w>top_point[1]:
				right_top_point = (_h,_w)
			elif bottom_point[0]>_h > left_point[0] and bottom_point[1]>_w>left_point[1]:
				left_bottom_point = (_h,_w)
			elif bottom_point[0]>_h>right_point[0] and right_point[1] >_w> bottom_point[1]:
				right_bottom_point = (_h,_w)
		points = [top_point,left_top_point,left_point,left_bottom_point,
		          bottom_point,right_bottom_point,right_top_point,right_point]
		#求导
		k = []
		for i in range(len(points)-1):
			h1,w1 = points[i]
			h2,w2 = points[i+1]
			try:
				k.append((w2-w1)/(h2-h1))
			except ZeroDivisionError:
				k.append(999)
		pattern.feature = k
		return True