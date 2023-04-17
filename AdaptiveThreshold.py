#!/usr/bin/env python
# coding: utf-8

# **In Simple Thresholding, a global value of threshold was used which remained constant throughout. So, a constant threshold value won’t help in the case of variable lighting conditions in different areas. Adaptive thresholding is the method where the threshold value is calculated for smaller regions. This leads to different threshold values for different regions with respect to the change in lighting. We use cv2.adaptiveThreshold for this.**

# In[1]:


import cv2


# In[10]:


image=cv2.imread("book.png")


# In[11]:


cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# In[14]:


cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[16]:


thresh1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY,199,5)


# In[17]:


thresh2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY,199,5)


# In[18]:


cv2.imshow("Original",image)
cv2.imshow("Gray scale",img)
cv2.imshow("Adaptive Mean",thresh1)
cv2.imshow("Adaptive Gaussian",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




