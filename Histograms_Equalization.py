#!/usr/bin/env python
# coding: utf-8

# ### Histogram equalization is a method in image processing of contrast adjustment using the image’s histogram.

# This method usually increases the global contrast of many images, especially when the usable data of the image is represented by close contrast values. Through this adjustment, the intensities can be better distributed on the histogram. This allows for areas of lower local contrast to gain a higher contrast. Histogram equalization accomplishes this by effectively spreading out the most frequent intensity values. The method is useful in images with backgrounds and foregrounds that are both bright or both dark.

# In[1]:


import cv2
import numpy as np


# In[19]:


image=cv2.imread("nature.png",0)


# In[20]:


#Creating a histogram Equalization of a image using cv2.equalizeHist()
equ=cv2.equalizeHist(image)


# In[21]:


#Stacking images side-by-side
res=np.hstack((image,equ))


# In[22]:


cv2.imshow("Hist",res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




