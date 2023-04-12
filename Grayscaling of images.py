#!/usr/bin/env python
# coding: utf-8

# ### Grayscaling is the process of converting an image from other color spaces e.g. RGB, CMYK, HSV, etc. to shades of gray. It varies between complete black and complete white.

# ### Importance of grayscaling 
# 
# ##### Dimension reduction:
# For example, In RGB images there are three color channels and three dimensions while grayscale images are single-dimensional.
# 
# #### Reduces model complexity: 
# Consider training neural articles on RGB images of 10x10x3 pixels. The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input nodes for grayscale images.
# 
# #### For other algorithms to work: 
# Many algorithms are customized to work only on grayscale images e.g. Canny edge detection function pre-implemented in the OpenCV library works on Grayscale images only.

# #### Method 1:Using the cv2.cvtColor() function

# In[1]:


import cv2


# In[2]:


image=cv2.imread("group.jpg")


# In[3]:


grayscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# In[4]:


cv2.imshow("original",image)
cv2.imshow("Gray scale",grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()


# #### Method2: Using the cv2.imread function with flag=0

# In[6]:


im=cv2.imread("group.jpg",0)
cv2.imshow("Image",im)
cv2.waitKey(0)
cv2.destroyAllWindows()


# #### Method3: Using the pixel manipulation(Average method)

# In[8]:


#obtain the dimension of the image array using the shape method
(row,col)=image.shape[0:2]


# In[9]:


#Take the average of pixel values of the BGR channels 
#to convert the colored image to grayscale image
for i in range(row):
    for j in range(col):
        #find the average of the BGR pixel values
        image[i,j]=sum(image[i,j])*0.33

cv2.imshow("Grayscale image",image) 
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




