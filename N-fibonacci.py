#!/usr/bin/env python
# coding: utf-8

# In[13]:


def fib(n):
    l = [0, 1]
    if n==0:
        return(l[0])
    elif n==1:
        return(l[1])
    else:
        #adding value to list
        for i in range(2, n+1):
            l.append(l[i-1] + l[i-2])
        return (l[n-1],l[0:n])
fib(100)


# In[ ]:





# In[ ]:





# In[ ]:




