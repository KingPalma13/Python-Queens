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


# In[36]:


NOC['price'].hist()


# In[37]:


NYC['price'].hist()


# In[38]:


NorthCarC['price'].hist()


# In[39]:


NYC['availability_365'].hist()


# In[40]:


NOC['availability_365'].hist()


# In[41]:


NorthCarC['availability_365'].hist()


# In[53]:


NOC.price[NOC.room_type == 'Entire home/apt'].hist()


# In[52]:


NOC.price[NOC.room_type == 'Hotel room'].hist()


# In[51]:


NOC.price[NOC.room_type == 'Private room'].hist()


# In[50]:


NOC.price[NOC.room_type == 'Shared room'].hist()


# In[54]:


NYC.price[NYC.room_type == 'Entire home/apt'].hist()


# In[55]:


NYC.price[NYC.room_type == 'Private room'].hist()


# In[56]:


NYC.price[NYC.room_type == 'Shared room'].hist()


# In[57]:


NYC.price[NYC.room_type == 'Hotel room'].hist()


# In[58]:


NorthCarC.price[NorthCarC.room_type == 'Hotel room'].hist()


# In[59]:


NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'].hist()


# In[60]:


NorthCarC.price[NorthCarC.room_type == 'Private room'].hist()


# In[61]:


NorthCarC.price[NorthCarC.room_type == 'Shared room'].hist()


# In[64]:


#testing the normality of New Orleans, New York and North Carolina prices then the individual prices entire homes/apt, private rooms, shared rooms and hotel rooms


# In[65]:


#testing normality of avalibility 365 of New Orleans, New York and North Carolina


# In[66]:


NOC.price[NOC.room_type == 'Entire home/apt'].mean()


# In[67]:


NOC.price[NOC.room_type == 'Private room'].mean()


# In[68]:


NOC.price[NOC.room_type == 'Hotel room'].mean()


# In[69]:


NOC.price[NOC.room_type == 'Shared room'].mean()


# In[70]:


#looking at the means of the price via room types in New Orleans


# In[71]:


NYC.price[NYC.room_type == 'Entire home/apt'].mean()


# In[72]:


NYC.price[NYC.room_type == 'Private room'].mean()


# In[73]:


NYC.price[NYC.room_type == 'Hotel room'].mean()


# In[74]:


NYC.price[NYC.room_type == 'Shared room'].mean()


# In[75]:


#looking at the means of the price via room types in New York


# In[76]:


NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'].mean()


# In[77]:


NorthCarC.price[NorthCarC.room_type == 'Private room'].mean()


# In[78]:


NorthCarC.price[NorthCarC.room_type == 'Hotel room'].mean()


# In[79]:


NorthCarC.price[NorthCarC.room_type == 'Shared room'].mean()


# In[80]:


#looking at the means of the price via room types in North Carolina


# In[81]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'], NorthCarC.price[NorthCarC.room_type == 'Hotel room'])


# In[82]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'], NYC.price[NYC.room_type == 'Entire home/apt'])


# In[83]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'], NOC.price[NOC.room_type == 'Entire home/apt'])


# In[ ]:




