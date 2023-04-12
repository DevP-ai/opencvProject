#!/usr/bin/env python
# coding: utf-8

# ### Scaling 

# In[3]:


import cv2


# In[4]:


img=cv2.imread("noise.png")


# In[5]:


try:
    #get number of pixel horizontally and vertically
    (height,width)=img.shape[:2]
    
    #specify the size of image along with interpolation methods.
    #cv2.INTER_AREA is used for shrinking,whereas cv2.INTER_CUBIC 
    #is used for zooming
    
    res=cv2.resize(img,(int(width/2),int(height/2)),interpolation=cv2.INTER_CUBIC)
    
    cv2.imshow("Original",img)
    cv2.imshow("result",res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  
except IOError:
    print("Error while reading file ")


# #### Rotating an image 

# In[6]:


try:
    #shape of image in terms of pixels
    (row,col)=img.shape[:2]
    
    #getRotationMatrix2D creates a matrix needed for transformation
    #we want matrix for rotation w.r.t center to 180 degree without scaling
    M=cv2.getRotationMatrix2D((col/2,row/2),180,1)
    res=cv2.warpAffine(img,M,(col,row))
    
    cv2.imshow("Original",img)
    cv2.imshow("Roatate",res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except IOError:
    print("Error while reading image")


# #### Shifting an Image 

# In[7]:


import numpy as np
# Create translation matrix.
# If the shift is (x, y) then matrix would be
# M = [1 0 x]
#     [0 1 y]
# Let's shift by (100, 50).
M = np.float32([[1, 0, 100], [0, 1, 50]])


# In[8]:


try:
    (row,col)=img.shape[:2]
    
    #warpAffine does appropriate shifting given the translation matrix
    res=cv2.warpAffine(img,M,(col,row))
    
    cv2.imshow("Original",img)
    cv2.imshow("Shift",res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except IOError:
    print("Error while reading image")


# #### Edge detection in an image 

# In[9]:


image=cv2.imread("img1.jpg")


# In[11]:


try:
    #Canny edge detection
    edge=cv2.Canny(image,100,200)
    
    cv2.imshow("Original",image)
    cv2.imshow("Edges",edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except IOError:
    print("Error while reading image")


# In[ ]:




