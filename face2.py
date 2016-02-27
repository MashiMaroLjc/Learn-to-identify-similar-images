import cv2
import numpy as np
import urllib.request as request
from PIL import Image,ImageDraw,ImageColor
import pHash

XML_PATH1 = "cvdata\\haarcascades\\haarcascade_frontalface_default.xml"


#This module can clasify the image based on faces.
#
#author MashiMaroLjc
#version 2016-2-26


def detect_faces(image):

    face_cascade1 = cv2.CascadeClassifier(XML_PATH1)
    if image.ndim == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image 

    faces = face_cascade1.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(10,10),
                                     flags=cv2.CASCADE_SCALE_IMAGE)


    result=[]
    
    for (x,y,width,height) in faces :
        result.append((x,y,x+width,y+height))
    return result


def PILMat_to_cvMat(image):
	'''
	Change the matrix from the format of PIL to openCV.
	'''
    mat =[]
    for l in image:
        x=[]
        for l2 in l:
            r,g,b = l2[0],l2[1],l2[2]
            x.append([b,g,r])
        mat.append(x)

    new_image = np.asarray(mat)
    return new_image



def split_imgae(image,xy):
	sub_image_list = []
	for (x1,y1,x2,y2) in  xy:
		sub_image = image.crop((x1,y1,x2,y2)).copy()
		sub_image_list.append(sub_image)

	return sub_image_list



def comp_faces(faces1,faces2,size,part_size):
	min_code = 1000 
	for face1 in faces1:
		for face2 in faces2:
			code = pHash.classify_DCT(face1, face2,size=size,part_size=part_size)
			if  code < min_code:
				min_code = code
	return min_code



def classify_faces(image1,image2,size=(32,32),part_size = (8,8)):
	"""
	image1' and 'image2' is a Image Object.
	You can build it by 'Image.open(path)'.
	'Size' is parameter what the image will resize to it and then image will be compared by the pHash.
	It's 32 * 32 when it default.  

	'part_size' is a size of a part of the matrix after Discrete Cosine Transform,which need to next steps.
	It's 8 * 8 when it default. 

	The function will return the hamming code,less is correct. 
	"""
	img= np.asarray(image1)
	img = PILMat_to_cvMat(img)
	faces = detect_faces(img) 
	if faces:
		every_face1 = split_imgae(image1, faces)
	else:
		return 1000  #False

	img= np.asarray(image2)
	img = PILMat_to_cvMat(img)
	faces = detect_faces(img) 
	if faces:
		every_face2 = split_imgae(image2, faces)
	else:
		return 1000	 #False

	return comp_faces(every_face1, every_face2,size,part_size)

__all__=[classify_faces]

