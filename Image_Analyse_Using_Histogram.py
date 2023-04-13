#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 
import matplotlib.pyplot as plt


# In[20]:


image=plt.imread("nature.png",0)


# In[21]:


img=cv2.imread("nature.png",0)
plt.hist(img.ravel(),256,[0,256])
plt.show()


# In[22]:


image=cv2.imread("flower.png",0)


# In[23]:


hist=cv2.calcHist([image],[0],None,[256],[0,256])


# In[24]:


plt.plot(hist)
plt.show()


# In[ ]:




