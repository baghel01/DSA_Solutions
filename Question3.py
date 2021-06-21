#!/usr/bin/env python
# coding: utf-8

# In[42]:


def pattern(height):
    i,j=height-1,1
    while j<=height:
        print(i*" ",j*"* ")
        i=i-1
        j=j+1
        
pattern(10)


# In[ ]:




