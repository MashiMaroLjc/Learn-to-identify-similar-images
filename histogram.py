from PIL import Image

#This module can classify the image by histogram.
#This method is easy for someone who is a beginner in Image classification.
#
#author MashiMaroLjc
#version 2016-2-16

def classfiy_histogram(image1,image2,size = (256,256)):
	''' 'image1' and 'image2' is a Image Object.
	You can build it by 'Image.open(path)'.
	'Size' is parameter what the image will resize to it.It's 256 * 256 when it default.  
	This function return the similarity rate betweene 'image1' and 'image2'
	'''
	image1 = image1.resize(size).convert("RGB")
	g = image1.histogram()

	image2 = image2.resize(size).convert("RGB")
	s = image2.histogram()

	assert len(g) == len(s),"error"

	data = []

	for index in range(0,len(g)):
		if g[index] != s[index]:
			data.append(1 - abs(g[index] - s[index])/max(g[index],s[index]) )
		else:
			data.append(1)
	
	return sum(data)/len(g)


