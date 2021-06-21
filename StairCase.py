#!/usr/bin/env python
# coding: utf-8

# In[26]:


def stair(h):
    s=2
    #a=1
    #b=2
    for i in range(3,h+1):
        t= stair(h-s)
        return(t)
    
stair(3)


# In[ ]:




