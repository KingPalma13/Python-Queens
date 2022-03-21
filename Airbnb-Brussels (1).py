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


listings = pd.read_csv("C:/Users/ekaar/Downloads/listings (3).csv")


# In[3]:


listings.head()


# In[4]:


listings2 = listings[['neighbourhood','room_type', 'price', 'minimum_nights', 'number_of_reviews', 'number_of_reviews','availability_365']]


# In[5]:


listings2.head()


# In[6]:


def neighbourhood (series): 
    if series == "Molenbeek-Saint-Jean":
        return 0
    if series == "Woluwe-Saint-Pierre": 
        return 0
    if series == "Ixelles":
        return 1
    if series == "Anderlecht":
        return 1


# In[7]:


listings2['price'].hist()


# In[8]:


listings2['number_of_reviews'].hist()


# In[9]:


#Running The Analysis
stats.ttest_1samp(listings2['number_of_reviews'],100)


# In[10]:


stats.ttest_1samp(listings2['price'],100)


# In[ ]:




