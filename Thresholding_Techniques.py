#!/usr/bin/env python
# coding: utf-8

# ####  Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the threshold value provided. In thresholding, each pixel value is compared with the threshold value. 
# 
# #### If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255). Thresholding is a very popular segmentation technique, used for separating an object considered as a foreground from its background. A threshold is a value which has two regions on its either side i.e. below the threshold or above the threshold. 
# 

# #### In Computer Vision, this technique of thresholding is done on grayscale images. So initially, the image has to be converted in grayscale color space. 
#  

# ### pseudo code

# if f(x,y)<T:
# 
#     then f(x,y)=0
#     
# else:
# 
#     f(x,y)=255
# 
# 
# 
# Where, f(x,y)=Coordinate pixel Value
#        T=Threshold value

# In[ ]:




