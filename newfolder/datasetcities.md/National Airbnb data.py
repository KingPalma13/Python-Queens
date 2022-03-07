#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


# In[ ]:


#getting ready to pull datasets and run analysis


# In[2]:


NO = pd.read_csv('C:/Users/racqu/OneDrive/Documents/New Orleans listing.csv')


# In[3]:


NOC= NO[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[4]:


NorthCarolina = pd.read_csv('C:/Users/racqu/Downloads/North Carolina.csv')


# In[5]:


NorthCarC= NorthCarolina[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[7]:


NY= pd.read_csv('C:/Users/racqu/Downloads/New York.csv')


# In[8]:


NYC= NY[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[ ]:


#pulling datasets 


# In[9]:


NOC.head()


# In[10]:


NorthCarC.head()


# In[11]:


NYC.head()


# In[ ]:


#checking to make sure data was pulled properly


# In[12]:


def room_type (series):
    if series == "Entire home/apt":
        return 0
    if series == "Private room":
        return 1
    if series == "Hotel room":
        return 2
    if series == "Shared room":
        return 3
    
NOC['RT'] = NOC['room_type'].apply(room_type)


# In[13]:


def room_type (series):
    if series == "Entire home/apt":
        return 0
    if series == "Private room":
        return 1
    if series == "Hotel room":
        return 2
    if series == "Shared room":
        return 3
    
NorthCarC['RT'] = NorthCarC['room_type'].apply(room_type)


# In[14]:


def room_type (series):
    if series == "Entire home/apt":
        return 0
    if series == "Private room":
        return 1
    if series == "Hotel room":
        return 2
    if series == "Shared room":
        return 3
    
NYC['RT'] = NYC['room_type'].apply(room_type)


# In[ ]:


#recoding room types from words to integers using 0-3 in order to run analysis later on


# In[15]:


NOC.head()


# In[16]:


NorthCarC.head()


# In[35]:


NYC.head()


# In[18]:


#checking to make sure the recoding was done correctly and that the new column was added correctly


# In[ ]:




