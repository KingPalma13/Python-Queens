#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.cluster import KMeans
import seaborn as sns


# In[8]:


listings = pd.read_csv("C:/Users/ekaar/Downloads/listings (3).csv")


# In[9]:


listings.head()


# In[10]:


listings2 = listings[['neighbourhood','room_type', 'price', 'minimum_nights', 'number_of_reviews', 'number_of_reviews','availability_365']]


# In[11]:


listings2.head()


# In[12]:


def neighbourhood (series): 
    if series == "Molenbeek-Saint-Jean":
        return 0
    if series == "Woluwe-Saint-Pierre": 
        return 0
    if series == "Ixelles":
        return 1
    if series == "Anderlecht":
        return 1


# In[ ]:




