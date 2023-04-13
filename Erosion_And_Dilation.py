#!/usr/bin/env python
# coding: utf-8

# ### Morphological operations are a set of operations that process images based on shapes. They apply a structuring element to an input image and generate an output image.

# #### The most basic morphological operations are two: Erosion and Dilation 
#  

# ### Basics of Erosion: 

# 1.Erodes away the boundaries of the foreground object
# 
# 2.Used to diminish the features of an image.

# #### Working of erosion:  

# 1.A kernel(a matrix of odd size(3,5,7) is convolved with the image.
# 
# 2.A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel are 1, otherwise, it is eroded (made to zero).
# 
# 3.Thus all the pixels near the boundary will be discarded depending upon the size of the kernel.
# 
# 4.So the thickness or size of the foreground object decreases or simply the white region decreases in the image.

# ### Basics of dilation:  

# 1.Increases the object area
# 
# 2.Used to accentuate features

# ### Working of dilation:

# 1.A kernel(a matrix of odd size(3,5,7) is convolved with the image
# 
# 2.A pixel element in the original image is ‘1’ if at least one pixel under the kernel is ‘1’.
# 
# 3.It increases the white region in the image or the size of the foreground object increases 

# In[1]:


import cv2
import numpy as np


# In[2]:


img=cv2.imread("geek.png")


# In[3]:


#taking a matrix of size 5 as the kernel
kernel=np.ones((5,5),np.uint8)


# In[12]:


# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
erosion=cv2.erode(img,kernel,iterations=1)
dilation=cv2.dilate(img,kernel,iterations=10)


# In[13]:


cv2.imshow("Original",img)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ### Uses of Erosion and Dilation

# ## Erosion

# 1.It is useful for removing small white noises.
# 
# 2.Used to detach two connected objects etc.

# ## Dilation

# 1.In cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
# 
# 2.It is also useful in joining broken parts of an object.

# In[ ]:




