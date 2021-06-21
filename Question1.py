#!/usr/bin/env python
# coding: utf-8

# In[13]:


def salary(basic):
    dearness=((40*basic)/100)
    basic=basic+dearness
    rent=((20*basic)/100)
    gross=basic+rent
    
    return('{} is gross salary of ramesh'.format(gross))

basic=int(input())
salary(basic)


# In[ ]:




