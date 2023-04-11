#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# ### cv2.copyMakeBorder() method is used to create a border around the image like a photo frame. 
# 
# ###### Syntax: cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)
# 
# ##### Parameters: 
# 
# ###### src: It is the source image. 
# 
# ###### top: It is the border width in number of pixels in top direction. 
# 
# ###### bottom: It is the border width in number of pixels in bottom direction. 
# 
# ###### left: It is the border width in number of pixels in left direction.  
# 
# ###### right: It is the border width in number of pixels in right direction. 
# 
# ###### borderType: It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc 
# 
# ##### dest: It is the destination image
# 
# ###### value: It is an optional parameter which depicts color of border if border type is cv2.BORDER_CONSTANT.
# 
# ###### Return Value: It returns an image. 

# In[2]:


image=cv2.imread("noise.png")
cv2.imshow("original",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Example 1

# In[3]:


border1=cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,None,value=0)


# In[4]:


cv2.imshow("Border",border1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Example2

# In[21]:


border2=cv2.copyMakeBorder(image,100,100,50,50,cv2.BORDER_REFLECT)


# In[22]:


cv2.imshow("Border",border2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




