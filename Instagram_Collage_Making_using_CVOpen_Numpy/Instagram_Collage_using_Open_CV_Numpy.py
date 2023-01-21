#!/usr/bin/env python
# coding: utf-8

# ## Installing the Open-CV for Python

# In[1]:


pip install opencv-python


# ## Imports

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# ## Getting Five Images

# In[2]:


img_top_left = cv2.imread("Images/top_left.jpg") 
img_top_right = cv2.imread("Images/top_right.jpg")
img_bottom_left = cv2.imread("Images/bottom_left.jpg")
img_bottom_right = cv2.imread("Images/bottom_right.jpg")
img_centre = cv2.imread("Images/center.jpeg")


# ## Resizing Four Image to (200,200) and Centre image to (100,100)

# In[5]:


resized_img_top_left = cv2.resize(img_top_left,(200,200))
resized_img_top_right = cv2.resize(img_top_right,(200,200))
resized_img_bottom_left = cv2.resize(img_bottom_left,(200,200))
resized_img_bottom_right = cv2.resize(img_bottom_right,(200,200))
resized_img_centre = cv2.resize(img_centre,(100,100))


# ## Converting OpenCV BGR to RGB

# In[6]:


fin_img_top_left = cv2.cvtColor(resized_img_top_left,cv2.COLOR_BGR2RGB)
fin_img_top_right = cv2.cvtColor(resized_img_top_right,cv2.COLOR_BGR2RGB)
fin_img_bottom_left = cv2.cvtColor(resized_img_bottom_left,cv2.COLOR_BGR2RGB)
fin_img_bottom_right = cv2.cvtColor(resized_img_bottom_right,cv2.COLOR_BGR2RGB)
fin_img_centre = cv2.cvtColor(resized_img_centre,cv2.COLOR_BGR2RGB)


# ## Creating black color border for four images and One for Centre Image

# In[7]:


h_border = np.zeros((200, 10, 3), dtype = np.uint8)
h_border = h_border*255
v_border = np.zeros((10, 430, 3), dtype = np.uint8)
v_border = v_border*255
h_border_cen = np.zeros((100, 10, 3), dtype = np.uint8)
h_border_cen = h_border_cen*255
v_border_cen = np.zeros((10, 120, 3), dtype = np.uint8)
v_border_cen = v_border_cen*255


# ## Combining Images using hstack and vstack (4 images with border)

# In[9]:


Horizontal1=np.hstack([h_border,fin_img_top_left,h_border,fin_img_top_right,h_border])
Horizontal2=np.hstack([h_border,fin_img_bottom_left,h_border,fin_img_bottom_right,h_border])
Vertical_attachment=np.vstack([v_border,Horizontal1,v_border,Horizontal2,v_border])
plt.imshow(Vertical_attachment)


# ## Add image to its centre

# In[11]:


Horizontal3 = np.hstack([h_border_cen,fin_img_centre,h_border_cen])
Vertical_attachment_cen = np.vstack([v_border_cen,Horizontal3,v_border_cen])
Vertical_attachment[155:275,155:275] =  Vertical_attachment_cen
plt.imshow(Vertical_attachment)


# In[ ]:




