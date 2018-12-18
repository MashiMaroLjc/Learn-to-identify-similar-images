#!/bin/bash

#================================================================
#   Copyright (C) 2018 Sangfor Ltd. All rights reserved.
#
#   filename：test.sh
#   author：ljx (jiaxinustc#gmail.com)
#   date：2018.12.11
#   description：比较$1目录下所有图片，找出相似图片
#
#================================================================

#export PYTHONPATH=`pwd`
#图片数目
s=0

for file in $1/*
do
    filelist[$s]=$file
    #echo ${filelist[$i]}
    ((s++))
done

for((i=0;i<s;i++))
do
    for((j=i+1;j<s;j++))
    do
        #echo ${filelist[$i]} ${filelist[$j]}
        python3 test.py ${filelist[$i]} ${filelist[$j]}
    done
done

#运行结果定向到result，然后将第二列移走即可，第二列都是相似图片。
#cat result| awk '{printf("mv %s s/\n",[)}''])}'
