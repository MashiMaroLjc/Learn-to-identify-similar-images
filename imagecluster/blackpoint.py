#coding:utf-8

#实现了特征提取接口，计算物品中少于阈值的点作为特征

from . feature_interface import Feature
import numpy
import math
from . pattern import Pattern

class BlackPoint(Feature):

	def call_feature(self,img:numpy.ndarray,pattern:Pattern,T):
		fea_n = pattern.fea_n
		step = int(math.sqrt(fea_n))
		w = int((pattern.right_bottom.x - pattern.left_top.x)/step)  #将当前物体7x7等分,共49个特征
		h = int((pattern.right_bottom.y- pattern.left_top.y)/step)   #w和h分别为跨度，y为高度，x为宽度
		#遍历7x7个等分区
		for j in range(step):#h
			for i in range(step): #w
				#第i*j个等分区的起点
				count = 0
				ijh = pattern.left_top.y + j*h
				ijw = pattern.left_top.x + i*w

				if w != 0 and h != 0:
					for hig in range(ijh,ijh+h):
						for wei in range(ijw,ijw+w):
							if img[hig][wei] <T:
								count += 1
					pattern.feature[j*7+i] = count/(w*h)  # 单个特征的平均黑点数
					return True
				elif w == 0 and h != 0:
					for hig in range(ijh, ijh+h):
						if img[hig][ijw] <T:
							count += 1
					pattern.feature[j*7+i] = count/h  # 单个特征的平均黑点数
					return True
				elif w != 0 and h == 0:
					for wei in range(ijw, ijw+w):
						if img[ijh][wei] <T:
							count += 1
					pattern.feature[j*7+i] = count/w  # 单个特征的平均黑点数
					return True
				else:
					return False