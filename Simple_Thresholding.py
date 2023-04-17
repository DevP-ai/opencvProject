#!/usr/bin/env python
# coding: utf-8

# ### Simple Thresholding

# The basic Thresholding technique is Binary Thresholding.
# 
# For every pixel, the same threshold value is applied. 
# 
# If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value.

# ### The different Simple Thresholding Techniques are: 

# **cv2.THRESH_BINARY:**  If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).

# **cv2.THRESH_BINARY_INV:** Inverted or Opposite case of cv2.THRESH_BINARY.

# **cv.THRESH_TRUNC:** If pixel intensity value is greater than threshold, it is truncated to the threshold. The pixel values are set to be the same as the threshold. All other values remain the same.

# **cv.THRESH_TOZERO:** Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.

# **cv.THRESH_TOZERO_INV:** Inverted or Opposite case of cv2.THRESH_TOZERO.

# In[1]:


import cv2
import numpy as np


# In[2]:


image=cv2.imread("img1.jpg")


# In[3]:


#cv2.cvtColor is applied over the image input with applied parameters
#to convert the image in grayscale
img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# In[4]:


#Applying different thresholding techniques on the input image
#all pixels value above 120 will be set to 255
ret,thresh1=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)


# In[5]:


cv2.imshow("Original colored",image)
cv2.imshow("Original GrayScale",img)
cv2.imshow("Binary Threshold",thresh1)
cv2.imshow("Binary Threshold Inverted",thresh2)
cv2.imshow("Truncated Threshold",thresh3)
cv2.imshow("Set to 0",thresh4)
cv2.imshow("Set to 0 Inverted",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




