#!/usr/bin/env python
# coding: utf-8

# Colour segmentation or color filtering is widely used in OpenCV for identifying specific objects/regions having a specific color. The most widely used color space is RGB color space, it is called an additive color space as the three color shades add up to give color to the image. To identify a region of a specific color, put the threshold and create a mask to separate the different colors. HSV color space is much more useful for this purpose as the colors in HSV space are much more localized thus can be easily separated. Color Filtering has many applications and uses cases such as in Cryptography, infrared analysis, food preservation of perishable foods, etc. In such cases, the concepts of Image processing can be used to find out or extract out regions of a particular color. 
# 

# In[1]:


import cv2 
import numpy as np


# In[2]:


#cap=cv2.VideoCapture(0)


# In[3]:


'''
while(1):
    _,frame=cap.read()
    #convert BGR color space to HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Threshold of blue in HSV space
    lower_blue=np.array([60,35,140])
    upper_blue=np.array([180,255,255])
    
    #preparing the mask to overplay
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    
    #The black region in mask has the value of 0
    #so when multiplied with original image remove all non-blue region
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
cap.release()
 '''


# In[4]:


image=cv2.imread("noise.png")


# In[5]:


cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)


# In[7]:


lower_blue=np.array([60,35,140])
upper_blue=np.array([180,255,255])


# In[8]:


mask=cv2.inRange(hsv,lower_blue,upper_blue)


# In[9]:


result=cv2.bitwise_and(image,image,mask=mask)


# In[ ]:


cv2.imshow("image",image)
cv2.imshow("mask",mask)
cv2.imshow("result",result)
    
cv2.waitKey(0)
    
cv2.destroyAllWindows()


# In[ ]:




