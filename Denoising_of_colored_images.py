#!/usr/bin/env python
# coding: utf-8

# **Denoising** of an image refers to the process of reconstruction of a signal from noisy images. Denoising is done to remove unwanted noise from image to analyze it in better form. It refers to one of the major pre-processing steps.

# In[1]:


import cv2


# In[2]:


image=cv2.imread("student.jpg")
image=cv2.resize(image,(540,440))


# In[30]:


dst = cv2.fastNlMeansDenoisingColored(image, None, 15,30,20,20)


# In[31]:


cv2.imshow("image",image)
cv2.imshow("Denoise",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




