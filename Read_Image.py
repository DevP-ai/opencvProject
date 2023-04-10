#!/usr/bin/env python
# coding: utf-8

#  Read color Image

# In[10]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#Color Image read
img=cv2.imread("group.jpg",0)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Size of the image

# In[2]:


#image shape
img.shape


# In[ ]:


im=cv2.imread("group.jpg")
plt.imshow(img)

#hold the window
plt.waitforbuttonpress()
plt.close('all')


# In[2]:


import cv2 


# Convert BGR to RGB

# In[14]:


#Convert BGR to RGB format
img=cv2.imread("group.jpg",1)
RGB_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Image",RGB_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[11]:


#GrayScale
img=cv2.imread("group.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[15]:


img.shape


# In[16]:


import os


# Write(save) image

# In[18]:


img=cv2.imread("group.jpg",0)
cv2.imwrite("write.jpg",img)


# In[11]:


im=cv2.imread("color.png")
B,G,R=cv2.split(im)
cv2.imshow("original",im)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


#im=cv2.imread("group.jpg")
#B,G,R=cv2.split(im)
cv2.imshow("Blue",B)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[13]:


#im=cv2.imread("group.jpg")
#B,G,R=cv2.split(im)
cv2.imshow("Green",G)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[14]:


cv2.imshow("Red",R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[15]:


import numpy as np


# ## Arithmetic operation set-1

# Subtract one image from another image (both images shape should  be  same)

# In[20]:


img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")


# In[21]:


weightedSum=cv2.addWeighted(img1,0.5,img2,0.4,0)


# In[22]:


cv2.imshow("WeightedImage",weightedSum)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[23]:


cv2.imwrite("filter.jpg",weightedSum)


# In[3]:


image1=cv2.imread("star.jpg")
image2=cv2.imread("shape.jpg")


# In[25]:


sub=cv2.subtract(image1,image2)


# In[26]:


cv2.imshow("Subtract",sub)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# cv2.imwrite("subtract.png",sub)

# In[4]:


img3=cv2.imread("subtract.png")


# In[5]:


sub1=cv2.subtract(image1,img3)


# In[6]:


cv2.imshow("sub",sub1)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[7]:


cv2.imwrite("small.jpg",sub1)


# ## Arithmetic operation set-2

# In[13]:


import cv2 


# In[14]:


import numpy as np


# Bitwise_AND

# In[15]:


img1=cv2.imread("moon.png")
img2=cv2.imread("dark.png")


# In[21]:


dest_and=cv2.bitwise_and(img2,img1,mask=None)


# In[22]:


cv2.imshow("Bitwise AND ",dest_and)
if cv2.waitKey(0)& 0xff==27:
    cv2.destroyAllWindows()


# In[18]:


cv2.imwrite("BitwiseAnd.jpg",dest_and)


# Bitwise_OR

# In[31]:


bit_or=cv2.bitwise_or(img2,img1,mask=None)


# In[32]:


cv2.imshow("Bitwise OR",bit_or)
if cv2.waitKey(0)&0xff==27:
    cv2.destroyAllWindows()


# In[34]:


cv2.imwrite("BitwiseOR.jpg",bit_or)


# Bitwise_XOR

# In[35]:


bit_xor=cv2.bitwise_xor(img2,img1,mask=None)


# In[36]:


cv2.imshow("Bitwise XOR",bit_xor)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[37]:


cv2.imwrite("BitwiseXOR.jpg",bit_xor)


# In[39]:


bit_not1=cv2.bitwise_not(img1,mask=None)
cv2.imshow("Image1 BitwiseNOT",bit_not1)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[40]:


cv2.imwrite("moonnot.jpg",bit_not1)


# In[43]:


bit_not2=cv2.bitwise_not(img2,mask=None)
cv2.imshow("Image2 BitwiseNOT",bit_not2)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()


# In[42]:


cv2.imwrite("notdark.jpg",bit_not2)


# In[ ]:




