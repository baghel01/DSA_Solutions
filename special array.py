#!/usr/bin/env python
# coding: utf-8

# In[3]:


def productSum(a[],depth=1):
    sum=0;      
    for i in array.length:
        if Array.isArray(array[i]):
            sum+= productSum(array[i],depth+1)
        else:
            sum+= array[i];    
    return (depth)*sum;

productSum(a[],depth)


# In[ ]:




