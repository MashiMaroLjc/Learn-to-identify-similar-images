#!/usr/bin/python3

#================================================================
#   Copyright (C) 2018 Sangfor Ltd. All rights reserved.
#
#   filename：test.py
#   author：ljx (jiaxinustc#gmail.com)
#   date：2018.12.11
#   description：传入两张图片，检测其相似与否
#
#================================================================
from PIL import Image
from aHash import classify_aHash
from dHash import classify_dHash
from pHash import classify_DCT
from histogram import classify_histogram
from histogram2 import classify_histogram_with_split
import sys


if __name__=="__main__":

    #phash dhash ahash
    #method="ahash"
    #method="dhash"
    #method="phash"
    #method="histogram"
    method="histogram2"

    image1=Image.open(sys.argv[1])
    image2=Image.open(sys.argv[2])
    if method=="ahash":
        re=classify_aHash(image1,image2)
        if(re):
            print(sys.argv[1],sys.argv[2])
    elif method=="dhash":
        re=classify_dHash(image1,image2)
        if(re<30):
            print(sys.argv[1],sys.argv[2])
    elif method=="phash":
        re=classify_DCT(image1,image2)
        if(re<=10):
            print(sys.argv[1],sys.argv[2])
    elif method=="histogram":
        re=classify_histogram(image1,image2)
        if(re>0.8):
            print(sys.argv[1],sys.argv[2])
    elif method=="histogram2":
        re=classify_histogram_with_split(image1,image2)
        if(re>0.55):
            print(sys.argv[1],sys.argv[2])
            #print(re)
