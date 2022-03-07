#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


Hawaii = pd.read_csv('C:/Users/racqu/Downloads/listings.csv')


# In[43]:


hawaii = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Hawaii listings.csv')


# In[4]:


Hawaii.head()


# In[5]:


Barcelona = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Barcelona listing.csv')


# In[6]:


Barcelona.head()


# In[7]:


Tokyo = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Tokyo Listing.csv')


# In[8]:


Tokyo.head()


# In[9]:


Athens = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Athens listings.csv')


# In[10]:


Athens.head()


# In[11]:


Sydeny = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Sydeny listing.csv')


# In[12]:


Sydeny.head()


# In[14]:


NO = pd.read_csv('C:/Users/racqu/OneDrive/Documents/New Orleans listing.csv')


# In[15]:


NO.head()


# In[16]:


Hawaii.drop(['neighbourhood_group'], axis=1)


# In[17]:


Barcelona.drop(['neighbourhood_group'], axis=1)


# In[18]:


Sydeny.drop(['neighbourhood_group'], axis=1)


# In[19]:


Athens.drop(['neighbourhood_group'], axis=1)


# In[20]:


Tokyo.drop(['neighbourhood_group'], axis=1)


# In[21]:


Hawaii.drop(['last_review'],axis=1)


# In[22]:


NO.drop(['last_review'], axis=1)


# In[23]:


Tokyo.drop(['last_review'], axis=1)


# In[24]:


Barcelona.drop(['last_review'], axis=1)


# In[25]:


Sydeny.drop(['last_review'], axis=1)


# In[26]:


Athens.drop(['last_review'], axis=1)


# In[27]:


Hawaii.drop(['reviews_per_month'],axis=1)


# In[28]:


NO.drop(['reviews_per_month'], axis=1)


# In[29]:


Tokyo.drop(['reviews_per_month'], axis=1)


# In[30]:


Sydeny.drop(['reviews_per_month'], axis=1)


# In[31]:


Barcelona.drop(['reviews_per_month'], axis=1)


# In[32]:


Athens.drop(['reviews_per_month'], axis=1)


# In[33]:


Athens.head()


# In[35]:


AthensC= Athens[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews']]


# In[36]:


SydenyC= Sydeny[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews']]


# In[37]:


TokyoC= Tokyo[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews']]


# In[38]:


BarcelonaC= Barcelona[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews']]


# In[39]:


NOC= NO[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews']]


# In[45]:


hawaiiC = hawaii[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews']]


# In[46]:


AthensC.head()


# In[ ]:




