#!/usr/bin/env python
# coding: utf-8

# ### Image Blurring refers to making the image less clear or distinct. It is done with the help of various low pass filter kernels.
# 
# ### Advantages of blurring:
# 
# #### It helps in Noise removal. As noise is considered as high pass signal so by the application of low pass filter kernel we restrict noise.
# 
# #### It helps in smoothing the image.
# 
# #### Low intensity edges are removed.
# 
# #### It helps in hiding the details when necessary

# In[1]:


import cv2 


# In[2]:


image=cv2.imread("devajit.png")


# In[3]:


cv2.imshow("Original image",image)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# ### Gaussian Blurring

# Gaussian blur is the result of blurring an image by a Gaussian function. It is a widely used effect in graphics software, typically to reduce image noise and reduce detail. It is also used as a preprocessing stage before applying our machine learning or deep learning models.

# cv2.GaussianBlur(src, kernelsize, sigmaX[, dst[, sigmaY[, borderType=BORDER_DEFAULT]]] )

# In[7]:


gaussian=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("Gaussian view",gaussian)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# ### Median Blur

# The Median Filter is a non-linear digital filtering technique, often used to remove noise from an image or signal. Median filtering is very widely used in digital image processing because, under certain conditions, it preserves edges while removing noise. It is one of the best algorithms to remove Salt and pepper noise.

# In[9]:


noise=cv2.imread("noise.png")
cv2.imshow("original image",noise)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[11]:


median=cv2.medianBlur(noise,5)
cv2.imshow("Median view",median)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[13]:


import cv2
import numpy as np
from skimage.util import random_noise
 
# Load an image
im_arr = cv2.imread("noise.png")
 
# Add salt and pepper noise to the image
noise_img = random_noise(im_arr, mode="s&p",amount=0.3)
noise_img = np.array(255*noise_img, dtype = 'uint8')
 
# Apply median filter
median = cv2.medianBlur(noise_img,5)
 
# Display the image
cv2.imshow('blur',noise_img)
cv2.imshow('blur1',median)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ### Bilateral Blur

#  A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels. This weight can be based on a Gaussian distribution. Thus, sharp edges are preserved while discarding the weak ones.

# In[14]:


bilateral = cv2.bilateralFilter(image, 9, 75, 75)


# In[15]:


cv2.imshow("Bilateral view",bilateral)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[ ]:




