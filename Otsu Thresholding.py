#!/usr/bin/env python
# coding: utf-8

# **Simple Thresholding** and **Adaptive Thresholding** were explained. In Simple Thresholding, the global value of threshold was used which remained constant throughout. In Adaptive thresholding, the threshold value is calculated for smaller regions with different threshold values for different regions with respect to the change in lighting.

# In **Otsu Thresholding**, a value of the threshold isn’t chosen but is determined automatically. A bimodal image (two distinct image values) is considered. The histogram generated contains two peaks. So, a generic condition would be to choose a threshold value that lies in the middle of both the histogram peak values.
# 
# 

# In[1]:


import cv2 


# In[15]:


image=cv2.imread("student.jpg")
image=cv2.resize(image,(540,440))


# In[16]:


img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# In[17]:


#applying Otsu thresholding as an extra flag in binary thresholding
ret,thresh=cv2.threshold(img,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# In[18]:


cv2.imshow("Image",image)
cv2.imshow("Otsu",thresh)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[ ]:




