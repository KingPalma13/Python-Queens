#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


# In[5]:


#getting ready to pull datasets and run analysis


# In[6]:


NO = pd.read_csv('C:/Users/racqu/OneDrive/Documents/New Orleans listing.csv')


# In[7]:


NOC= NO[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[8]:


NorthCarolina = pd.read_csv('C:/Users/racqu/Downloads/North Carolina.csv')


# In[9]:


NorthCarC= NorthCarolina[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[10]:


NY= pd.read_csv('C:/Users/racqu/Downloads/New York.csv')


# In[12]:


NYC= NY[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[13]:


#pulling datasets 


# In[14]:


NOC.head()


# In[15]:


NorthCarC.head()


# In[16]:


NYC.head()


# In[17]:


#checking to make sure data was pulled properly


# In[18]:


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


# In[19]:


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


# In[20]:


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


# In[21]:


#recoding room types from words to integers using 0-3 in order to run analysis later on


# In[22]:


NOC.head()


# In[23]:


NorthCarC.head()


# In[24]:


NYC.head()


# In[25]:


#checking to make sure the recoding was done correctly and that the new column was added correctly


# In[26]:


NOC['price'].hist()


# In[27]:


NYC['price'].hist()


# In[28]:


NorthCarC['price'].hist()


# In[29]:


NYC['availability_365'].hist()


# In[30]:


NOC['availability_365'].hist()


# In[31]:


NorthCarC['availability_365'].hist()


# In[32]:


NOC.price[NOC.room_type == 'Entire home/apt'].hist()


# In[33]:


NOC.price[NOC.room_type == 'Hotel room'].hist()


# In[34]:


NOC.price[NOC.room_type == 'Private room'].hist()


# In[35]:


NOC.price[NOC.room_type == 'Shared room'].hist()


# In[36]:


NYC.price[NYC.room_type == 'Entire home/apt'].hist()


# In[37]:


NYC.price[NYC.room_type == 'Private room'].hist()


# In[38]:


NYC.price[NYC.room_type == 'Shared room'].hist()


# In[39]:


NYC.price[NYC.room_type == 'Hotel room'].hist()


# In[40]:


NorthCarC.price[NorthCarC.room_type == 'Hotel room'].hist()


# In[41]:


NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'].hist()


# In[42]:


NorthCarC.price[NorthCarC.room_type == 'Private room'].hist()


# In[43]:


NorthCarC.price[NorthCarC.room_type == 'Shared room'].hist()


# In[44]:


#testing the normality of New Orleans, New York and North Carolina prices then the individual prices entire homes/apt, private rooms, shared rooms and hotel rooms


# In[45]:


#testing normality of avalibility 365 of New Orleans, New York and North Carolina


# In[46]:


NOC.price[NOC.room_type == 'Entire home/apt'].mean()


# In[47]:


NOC.price[NOC.room_type == 'Private room'].mean()


# In[48]:


NOC.price[NOC.room_type == 'Hotel room'].mean()


# In[49]:


NOC.price[NOC.room_type == 'Shared room'].mean()


# In[50]:


#looking at the means of the price via room types in New Orleans


# In[51]:


NYC.price[NYC.room_type == 'Entire home/apt'].mean()


# In[52]:


NYC.price[NYC.room_type == 'Private room'].mean()


# In[53]:


NYC.price[NYC.room_type == 'Hotel room'].mean()


# In[54]:


NYC.price[NYC.room_type == 'Shared room'].mean()


# In[55]:


#looking at the means of the price via room types in New York


# In[56]:


NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'].mean()


# In[57]:


NorthCarC.price[NorthCarC.room_type == 'Private room'].mean()


# In[58]:


NorthCarC.price[NorthCarC.room_type == 'Hotel room'].mean()


# In[59]:


NorthCarC.price[NorthCarC.room_type == 'Shared room'].mean()


# In[60]:


#looking at the means of the price via room types in North Carolina


# In[61]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'], NorthCarC.price[NorthCarC.room_type == 'Hotel room'])
#running independent ttest there is a significant difference bewteeen the prices of North Carolina enitre home/apt and hotel room


# In[62]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'], NYC.price[NYC.room_type == 'Entire home/apt'])
#running independent ttest there is a signifcant difference between North Carolina and New Yorks entire home/apt


# In[63]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Entire home/apt'], NOC.price[NOC.room_type == 'Entire home/apt'])
#running independent ttest there is a signifcant difference between North Carolina and New Orleans entire home/apt


# In[64]:


ttest_ind(NYC.price[NYC.room_type == 'Entire home/apt'], NYC.price[NYC.room_type == 'Hotel room'])
#running independent ttest there is a significant difference between the prices of North York enitre home/apt and hotel room


# In[65]:


ttest_ind(NOC.price[NOC.room_type == 'Entire home/apt'], NOC.price[NOC.room_type == 'Hotel room'])
#running independent ttest there is a significant difference between the prices of New Orleans enitre home/apt and hotel room


# In[66]:


ttest_ind(NYC.price[NYC.room_type == 'Entire home/apt'], NOC.price[NOC.room_type == 'Entire home/apt'])
#running independent ttest there is not a significant differnce between prices of New Orleans and New York entire home/apt


# In[67]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Private room'], NOC.price[NOC.room_type == 'Private room'])
#running independent ttest there is a difference bewteeen the prices of North Carolina and New Orleans private room


# In[68]:


ttest_ind(NYC.price[NYC.room_type == 'Private room'], NOC.price[NOC.room_type == 'Private room'])
#running independent ttest there is a significant differnce between prices of New Orleans and New York private room


# In[69]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Private room'], NYC.price[NYC.room_type == 'Private room'])
#running independent ttest there is not a significant differnce between prices of North Carolina and New York  private room


# In[70]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Hotel room'], NYC.price[NYC.room_type == 'Hotel room'])
#running independent ttest there is no significant difference between the prices of North Carolina and New York hotel room


# In[71]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Hotel room'], NOC.price[NOC.room_type == 'Hotel room'])
#running independent ttest there is a difference between the prices of North Carolina and New Orleans hotel rooms


# In[72]:


ttest_ind(NYC.price[NYC.room_type == 'Hotel room'], NOC.price[NOC.room_type == 'Hotel room'])
#running independent ttest there is a difference between the prices of New York and New Orleans hotel rooms


# In[73]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Shared room'], NOC.price[NOC.room_type == 'Shared room'])


# In[74]:


ttest_ind(NYC.price[NYC.room_type == 'Shared room'], NOC.price[NOC.room_type == 'Shared room'])


# In[75]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Shared room'], NYC.price[NYC.room_type == 'Shared room'])


# In[76]:


ttest_ind(NorthCarC.price[NorthCarC.room_type == 'Shared room'], NYC.price[NYC.room_type == 'Shared room'])


# In[77]:


#running independent ttest there is no significant difference between the prices of New orleans, New York and North Carolina Shared rooms


# In[78]:


NOC['neighbourhood'].value_counts()


# In[79]:


NYC['neighbourhood'].value_counts()


# In[80]:


NorthCarC['neighbourhood'].value_counts()


# In[81]:


NorthCarC.to_csv("C:/Users/racqu/Downloads/NorthCarC.csv")


# In[82]:


NYC.to_csv("C:/Users/racqu/Downloads/NYC.csv")


# In[83]:


NOC.to_csv("C:/Users/racqu/Downloads/NOC.csv")


# In[ ]:




