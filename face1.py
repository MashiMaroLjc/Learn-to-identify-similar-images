import os
import cv2
import numpy as np
import urllib.request as request
from PIL import Image,ImageDraw,ImageColor


#This module can clasify the image based on faces.
#
#author MashiMaroLjc
#version 2016-2-26

def detectFaces(image_path):
    """
    Open the image based on the image_path and find all faces in the image.
    Finally, return the coordinates , width and height as a list
    """
    img = cv2.imread(image_path)

    face_cascade = cv2.CascadeClassifier("cvdata\\haarcascades\\haarcascade_frontalface_default.xml")
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img 

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(10,10),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    result = []

    for (x,y,width,height) in faces:
        result.append((x,y,x+width,y+height))
    return result


def drawFaces(image_path,new_path):
    """
    Open the image based on the image_path and draw a rectangle on the faces.
    Save to new_path after draw.
    """
    faces = detectFaces(image_path)
    if faces:
        img = Image.open(image_path)
        draw_instance = ImageDraw.Draw(img)
        for (x1,y1,x2,y2) in faces:
            draw_instance.rectangle((x1,y1,x2,y2), outline=(255, 0,0))
        img.save(new_path)

__all__ = [drawFaces]


if __name__ == '__main__':
    path = "00212599.jpg"
    drawFaces(path,"1.jpg")