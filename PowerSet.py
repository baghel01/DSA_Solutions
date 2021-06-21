#!/usr/bin/env python
# coding: utf-8

# In[7]:


def power(a):
    l=len(a)
    for i in range(1 << l):
        print([a[j] for j in range(l) if (i & (1 << j))])
    
n=int(input())
a=[]
for i in range(0,n):
    e = int(input())
    a.append(e)
power(a)


# In[ ]:





# In[ ]:




