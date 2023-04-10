#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 
import numpy as np


# In[22]:


image=cv2.imread("devajit.png")


# In[23]:


kernel=np.ones((5,5),np.uint8)


# In[24]:


erode1=cv2.erode(image,kernel)


# In[25]:


cv2.imshow("Erode1Method",erode1)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[26]:


erode2=cv2.erode(image,kernel,cv2.BORDER_REFLECT)
cv2.imshow("Erode2Method",erode2)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[ ]:




