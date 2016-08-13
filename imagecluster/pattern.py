#coding:utf-8


class _point(object):

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return "<%s,%s>"%(self.x,self.y)



class Pattern(object):

	def __init__(self,index,w,h,fea_n):
		self.index = index + 1
		self.category =0
		self.left_top = _point(w,h)
		self.right_bottom = _point(0,0)
		self.fea_n = fea_n
		self.feature = [0 for _ in range(fea_n)]

	def __str__(self):
		return "index: %s  " \
	"category:%s  "\
	"left_top:%s  "\
	"right_bottom:%s  "%(self.index,self.category,self.left_top,self.right_bottom)



