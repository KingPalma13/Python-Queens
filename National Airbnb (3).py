#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.cluster import KMeans
import seaborn as sns
from scipy.stats import norm
from scipy import stats


# In[2]:


AirbnblistingsSanFrancisco = pd.read_csv("C:/Users/ekaar/Documents/R/listings.csv")
AirbnblistingsDenver = pd.read_csv("C:/Users/ekaar/Downloads/listings (5).csv")


# In[3]:


AirbnblistingsSanFrancisco .head()
AirbnblistingsDenver.head()


# In[4]:


AirbnblistingsSanFrancisco2 = AirbnblistingsSanFrancisco[['id','host_id','neighbourhood','latitude','longitude','room_type', 'price', 'minimum_nights', 'number_of_reviews','availability_365']]
AirbnblistingsDenver2 = AirbnblistingsDenver[['id','host_id','neighbourhood','latitude','longitude','room_type', 'price', 'minimum_nights', 'number_of_reviews','availability_365']]


# In[5]:


AirbnblistingsSanFrancisco2.head()
AirbnblistingsDenver2.head()


# In[6]:


NationalAirbnb =pd.concat([AirbnblistingsSanFrancisco,AirbnblistingsDenver],axis=1)


# In[7]:


#Test Assumpton
NationalAirbnb['price'].hist()


# In[8]:


NationalAirbnb['calculated_host_listings_count'].hist()


# In[9]:


NationalAirbnb['number_of_reviews'].hist()


# In[10]:


AirbnblistingsSanFrancisco['number_of_reviews'].hist()


# In[11]:


AirbnblistingsDenver['number_of_reviews'].hist()


# In[12]:


#Running The Analysis
stats.ttest_1samp(AirbnblistingsSanFrancisco['number_of_reviews'],100)


# In[13]:


stats.ttest_1samp(AirbnblistingsDenver['number_of_reviews'],100)


# In[ ]:




