#coding:utf-8
#实现在物体中提取特征的抽象类
import numpy
from . pattern import Pattern
class Feature:

	def call_feature(self,img:numpy.ndarray,pattern:Pattern,T):
		"""
		在图像中的物体提取特征
		:param img: 图像的numpy.array表现形式
		:param pattern: 物体，为feature._Pattern
		:param T: 阈值
		:return: 布尔值，真值时为该物品下产生的特征可取，假值则相反
		"""
		raise Exception("%s don't implement the "
			          "call_feature interface"%(self.__class__.__name__))

class IScanner:

	def scan(self,img:numpy.ndarray,T):
		raise Exception("%s don't implement the "
			          "scan interface"%(self.__class__.__name__))