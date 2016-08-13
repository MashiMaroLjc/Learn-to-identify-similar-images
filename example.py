#coding:utf-8

#一个example，选出1.bmp里面相似的图像

from imagecluster.feature import get_feature
from imagecluster.calculate import Similar
from imagecluster.blackpoint import BlackPoint
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from imagecluster.shape import Shape
path = "demo.jpg"
resize = (128,128)
my_image = Image.open(path).resize(resize)
patterns,feature=get_feature(path,resize=resize)

def picture(image,exampless,colors):
	"""

	:param img:
	:param example:
	:return:
	"""
	plt.imshow(image)
	ax = plt.gca()
	i = 0
	for examples in exampless:
		for exa in examples:
			rect = Rectangle((exa.left_top.x,exa.left_top.y), exa.right_bottom.x-exa.left_top.x,
			                 exa.right_bottom.y - exa.left_top.y, fill=None, color=colors[i],linewidth=3)
			ax.add_patch(rect)
		i += 1
	plt.show()
	#plt.clf()


#example1
example = patterns[0]
example_feature = feature[0]


#example2
example2 = patterns[2]
example_feature2 = feature[2]

#
test = patterns
test_feature = feature



ok = []
ok2 = []
for i in range(len(test_feature)):
	res = Similar.similar(example_feature,test_feature[i],"ecl")
	if res > 0.9:
		ok.append(test[i])
	res = Similar.similar(example_feature2, test_feature[i], "ecl")
	if res > 0.9:
		ok2.append(test[i])


picture(my_image,[ok,ok2],colors=["blue","red"])

