#coding:utf-8


import numpy as np
import numpy.linalg as la

def calc(v1,v2,opt):
	"""
	根据opt返回布尔值,v1 opt v2
	:param opt:
	:return:
	"""
	if opt =="<":
		return v1 < v2
	elif opt =="<=":
		return v1 <= v2
	elif opt == ">":
		return v1 > v2
	elif opt == ">=":
		return v1 >= v2
	else:
		raise ValueError("Illegal opt")


class Similar(object):

	"""
	负责计算相似度，内置计算函数
	"""
	# 欧式距离,1表示100%，越接近0表示越不相似
	def _ecl_sim(cls,inA, inB):
		return 1.0 / (1.0 + la.norm(inA - inB))

	# 皮尔逊相关系数,范围-1->+1， 越大越相似
	def _pears_sim(cls,inA, inB):
		if len(inA) < 3:
			return 1.0
		return 0.5 + 0.5 * np.corrcoef(inA, inB, rowvar=0)[0][1]

	# 余弦相关范围-1->+1 越大越相似
	def _cos_sim(cls,inA, inB):
		num = float(inB * inA.T)
		de_nom = la.norm(inA) * la.norm(inB)
		return 0.5 + 0.5 * (num / de_nom)

	@classmethod
	def _similar(cls,feature1,feature2,fun_name):
		inA = np.matrix(feature1)
		inB = np.matrix(feature2)


		if fun_name not in cls._set:
			raise ValueError("Unknown fun_name.You only can choose %s"%(list(cls._set.keys())))
		else:
			#选A中各类与B中各类最相似的结果
			func = cls._set[fun_name][0]
			opt = cls._set[fun_name][1]
			limit = cls._limit_set[opt]
			for class_A in inA:
				for class_B in inB:
					if class_A.shape == (1,0) or class_B.shape == (1,0):
						score = cls._limit_set[opt]
					else:
						score = func(cls,class_A,class_B)
						limit = score
			return limit

	_set = {
		"ecl":(_ecl_sim,">"),
		"cos":(_cos_sim,">"),
		"pears":(_pears_sim,">")
	}

	_limit_set = {
		"<":np.inf ,#越少越好
		"<=":np.inf,
		">":-np.inf, #越大越好
		">=":-np.inf
	}


	@classmethod
	def similar(cls,feature1,feature2,fun_name,T=None):
		"""
		按照fun_name去获取内置函数来计算相似度
		:param feature1:2d
		:param feature2:2d
		:param fun_name:
		:param T: 阈值，给出时按照函数自动返回布尔值
		:return:
		"""
		score = cls._similar(feature1,feature2,fun_name)
		if  T:
			opt = cls._set.get(fun_name)[1] #获取符号
			calc(score,T,opt)
		else:
			return score

