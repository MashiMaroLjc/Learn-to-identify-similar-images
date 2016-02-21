from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
#This module can classfy the image by dHash
#
#author MashiMaroLjc
#version 2016-2-16

def getCode(img,size):

	result = []
	for x in range(0,size[0]):
		for y in range(0,size[1]-1):
			now_value = img.getpixel((x,y))
			next_value = img.getpixel((x,y+1))

			if next_value < now_value:
				result.append(1)
			else:
				result.append(0)


	return result



def compCode(code1,code2):
	num = 0
	for index in range(0,len(code1)):
		if code1[index] != code2[index]:
			num+=1
	return num 

def classfiy_dHash(image1,image2,size=(9,8)):
	''' 'image1' and 'image2' is a Image Object.
	You can build it by 'Image.open(path)'.
	'Size' is parameter what the image will resize to it and then image will be compared to another image by the dHash.
	It's 9 * 8 when it default.  

	The function will return the hamming code,less is correct. 
	'''
	image1 = image1.resize(size).convert('L')
	code1 = getCode(image1, size)

	image2 = image2.resize(size).convert('L')
	code2 = getCode(image2, size)

	assert len(code1) == len(code2),"error"
	
	return compCode(code1, code2)



__all__=[classfiy_dHash]


