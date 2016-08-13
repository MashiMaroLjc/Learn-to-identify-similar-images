##Scripts

[中文](ReadMe-chinese.md)

+ imagecluster 

  +  feature_interface
  	Provide two interfaces,one was named ```IScanner```, which used to scan something from image，another was named
     ```Feature```,which used to find the feature. 
	 

  +  grow  
    Implement the ```IScanner``` interface.It will scan the object by region growing.
  
  +  shape
   Implement the ```Feature``` interface.It will find the feature by the shape of object.
  
  
  +  blackpoint
  Implement the ```Feature``` interface.It will find the feature by the number of black point of object.
   
  
  +  pattern
   Record the information object from image.
  
  +  feature 
  Provide the function which find the feature from net or location
 
  
  +  calculate
  Provide a class to calculate the similarity  from two list of feature which from two images.



+  ```example.py```
	Get the feature by shape after scan the object by region growing.Then get the similarity
	by calculate euclidean distance.Finally ,mark the similar object on the image.


   <br/>
  <img src="demo.jpg" style="width:725px"/>
  before
  <br/>
  ![after](after.jpg)
  after