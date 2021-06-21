#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def distance(dis):
    meter=dis*1000
    feet = dis * 3280.84
    inch = dis * 39370.1
    centimmeter = dis * 100000
    return ("distance in meter={}, feet={}, inches={} and centimeter={}".format(meter,feet,inch,centimmeter))

km=int(input())
distance(km)


# In[ ]:




