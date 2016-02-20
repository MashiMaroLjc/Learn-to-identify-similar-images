from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

#This module can classfy the image by Average Hash Method
#The Hash Method is too strict,so this moudel suitable for finding image by Thumbnail
#
#author MashiMaroLjc
#version 2016-2-17

def getCode(img,size):

	pixel = []
	for x in range(0,size[0]):
		for y in range(0,size[1]):
			pixel_value = img.getpixel((x,y))
			pixel.append(pixel_value)

	avg = sum(pixel)/len(pixel)

	cp = []

	for px in pixel:
		if px > avg:
			cp.append(1)
		else:
			cp.append(0)
	return cp



def compCode(code1,code2):
	num = 0
	for index in range(0,len(code1)):
		if code1[index] != code2[index]:
			num+=1
	return num 

def classfiy_aHash(image1,image2,size=(8,8),exact=25):
	''' 'image1' and 'image2' is a Image Object.
	You can build it by 'Image.open(path)'.
	'Size' is parameter what the image will resize to it and then image will be compared by the algorithm.
	It's 8 * 8 when it default.  
	'exact' is parameter for limiting the Hamming code between 'image1' and 'image2',it's 25 when it default.
	The result become strict when the exact become less. 
	This function return the true when the 'image1'  and 'image2' are similar. 
	'''
	image1 = image1.resize(size).convert('L').filter(ImageFilter.BLUR)
	image1 = ImageOps.equalize(image1)
	code1 = getCode(image1, size)
	image2 = image2.resize(size).convert('L').filter(ImageFilter.BLUR)
	image2 = ImageOps.equalize(image2)
	code2 = getCode(image2, size)

	assert len(code1) == len(code2),"error"
	
	return compCode(code1, code2)<=exact



__all__=[classfiy_aHash]

