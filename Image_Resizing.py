#!/usr/bin/env python
# coding: utf-8

# ## Image Resizing

# In[1]:


import cv2
import matplotlib.pyplot as plt


# In[2]:


img=cv2.imread("img1.jpg")


# In[3]:


half=cv2.resize(img,(0,0),fx=0.1,fy=0.1)
bigger=cv2.resize(img,(1050,1610))
stretch=cv2.resize(img,(780,540),interpolation=cv2.INTER_AREA)


# In[4]:


title=["Original","Half","Bigger","Interpolation Nearest"]


# In[5]:


images=[img,half,bigger,stretch]


# In[6]:


count=4
for i in range(count):
    plt.subplot(2,2,i+1)
    plt.title(title[i])
    plt.imshow(images[i])

plt.show()    

