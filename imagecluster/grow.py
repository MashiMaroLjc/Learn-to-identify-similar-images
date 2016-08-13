#coding:utf-8

"""
实现IScanNER接口，使用区域生长方式
"""
import numpy
from . feature_interface import IScanner

class Grow(IScanner):

	def _sub_scanned(self,image, T, buff, location, visited, counter):
		"""
		区域生长，基于广度遍历，轮流扫描右，上，左，下
		:param image:
		:param T:
		:param buff:
		:param location:
		:param visited:
		:param counter:
		:return:
		"""
		h, w = location
		# 访问该点
		visited[h][w] = 1
		buff[h][w] = counter
		# BFS
		location_list = [(h, w + 1), (h - 1, w), (h, w - 1), (h + 1, w)]
		for lo in location_list:
			if 0 <= lo[0] < image.shape[0] and 0 <= lo[1] < image.shape[1]:
				if image[lo[0]][lo[1]] < T and not visited[lo[0]][lo[1]]:
					buff, visited = self._sub_scanned(image, T, buff, lo, visited, counter)
		return buff, visited

	def scan(self,img:numpy.ndarray,T):
			"""
			标识图片
			:param image: h*w
			:return: np.ndarray,int(类别数，也是类别的id)
			"""
			buff = numpy.ones(img.shape) * 255
			visited = numpy.zeros(img.shape)
			img[0] = 255  # 第一行置白
			img[0:, 0] = 255  # 第一列置白
			h, w = img.shape

			# 从左往右，从上到下扫描
			counter = 0
			for _h in range(1, h - 1):
				for _w in range(1, w - 1):
					pixel = img[_h][_w]
					if pixel < T and visited[_h][_w] == 0:
						buff, visited = self._sub_scanned(img, T, buff, (_h, _w), visited, counter)
						counter += 1
					# 最后一次回多余一个1出来
			return buff, counter - 1
