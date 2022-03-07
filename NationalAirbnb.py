#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.cluster import KMeans
import seaborn as sns


# In[2]:


AirbnblistingsSanFrancisco = pd.read_csv("C:/Users/ekaar/Documents/R/listings.csv")
AirbnblistingsDenver = pd.read_csv("C:/Users/ekaar/Downloads/listings (5).csv")


# In[3]:


AirbnblistingsSanFrancisco .head()
AirbnblistingsDenver.head()


# In[5]:


AirbnblistingsSanFrancisco2 = AirbnblistingsSanFrancisco[['id','host_id','neighbourhood','latitude','longitude','room_type', 'price', 'minimum_nights', 'number_of_reviews', 'number_of_reviews','availability_365']]
AirbnblistingsDenver2 = AirbnblistingsDenver[['id','host_id','neighbourhood','latitude','longitude','room_type', 'price', 'minimum_nights', 'number_of_reviews', 'number_of_reviews','availability_365']]


# In[6]:


AirbnblistingsSanFrancisco2.head()
AirbnblistingsDenver2.head()


# In[7]:


NationalAirbnb =pd.concat([AirbnblistingsSanFrancisco,AirbnblistingsDenver],axis=1)


# In[ ]:




