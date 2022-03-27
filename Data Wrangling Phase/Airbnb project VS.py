#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np


# In[63]:


hawaii = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Hawaii listings.csv')


# In[64]:


hawaii.head()


# In[12]:


Barcelona = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Barcelona listing.csv')


# In[13]:


Barcelona.head()


# In[14]:


Tokyo = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Tokyo Listing.csv')


# In[15]:


Tokyo.head()


# In[16]:


Athens = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Athens listings.csv')


# In[17]:


Athens.head()


# In[18]:


Sydeny = pd.read_csv('C:/Users/racqu/OneDrive/Documents/Sydeny listing.csv')


# In[19]:


Sydeny.head()


# In[20]:


NO = pd.read_csv('C:/Users/racqu/OneDrive/Documents/New Orleans listing.csv')


# In[21]:


NO.head()


# In[22]:


Barcelona.drop(['neighbourhood_group'], axis=1)


# In[23]:


Sydeny.drop(['neighbourhood_group'], axis=1)


# In[24]:


Athens.drop(['neighbourhood_group'], axis=1)


# In[25]:


Tokyo.drop(['neighbourhood_group'], axis=1)


# In[26]:


NO.drop(['last_review'], axis=1)


# In[27]:


Tokyo.drop(['last_review'], axis=1)


# In[28]:


Barcelona.drop(['last_review'], axis=1)


# In[29]:


Sydeny.drop(['last_review'], axis=1)


# In[30]:


Athens.drop(['last_review'], axis=1)


# In[31]:


NO.drop(['reviews_per_month'], axis=1)


# In[32]:


Tokyo.drop(['reviews_per_month'], axis=1)


# In[33]:


Sydeny.drop(['reviews_per_month'], axis=1)


# In[34]:


Barcelona.drop(['reviews_per_month'], axis=1)


# In[35]:


Athens.drop(['reviews_per_month'], axis=1)


# In[36]:


Athens.head()


# In[37]:


AthensC= Athens[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[38]:


SydenyC= Sydeny[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[39]:


TokyoC= Tokyo[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[40]:


BarcelonaC= Barcelona[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[41]:


NOC= NO[['id', 'name', 'host_id', 'host_name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']]


# In[42]:


AthensC.head()


# In[48]:


SydenyC.head()


# In[49]:


TokyoC.head()


# In[43]:


BarcelonaC.head()


# In[44]:


NOC.head()


# In[45]:


def room_type (series):
    if series == "Entire home/apt":
        return 0
    if series == "Private room":
        return 1
    if series == "Hotel room":
        return 2
    if series == "Shared room":
        return 3
    
AthensC['RT'] = AthensC['room_type'].apply(room_type)


# In[46]:


AthensC.head()


# In[47]:


def room_type (series):
    if series == "Entire home/apt":
        return 0
    if series == "Private room":
        return 1
    if series == "Hotel room":
        return 2
    if series == "Shared room":
        return 3
    
SydenyC['RT'] = SydenyC['room_type'].apply(room_type)


# In[48]:


def room_type (series):
    if series == "Entire home/apt":
        return 0
    if series == "Private room":
        return 1
    if series == "Hotel room":
        return 2
    if series == "Shared room":
        return 3
    
BarcelonaC['RT'] = BarcelonaC['room_type'].apply(room_type)


# In[49]:


def room_type (series):
    if series == "Entire home/apt":
        return 0
    if series == "Private room":
        return 1
    if series == "Hotel room":
        return 2
    if series == "Shared room":
        return 3
    
TokyoC['RT'] = TokyoC['room_type'].apply(room_type)


# In[50]:


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


# In[51]:


NOC.head()


# In[52]:


SydenyC.head()


# In[53]:


TokyoC.head()


# In[54]:


BarcelonaC.head()


# In[55]:


C1= pd.merge(AthensC, SydenyC, how = "left")


# In[56]:


C1.head(100)


# In[57]:


AthensC.head(100)


# In[58]:


SydenyC.head(10)


# In[59]:


C2= pd.merge(C1, TokyoC, how= "right")


# In[60]:


C2.head()


# In[61]:


C3= pd.merge(C2, BarcelonaC, how= "right")


# In[62]:


C3.head()


# In[63]:


C4= pd.merge(C3, NOC, how= "right")


# In[64]:


C4.head()


# In[69]:


import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy import stats
import matplotlib.pyplot as plt


# In[1]:


sudo apt-get install python-scipy


# In[2]:


pip sudo apt-get install python-scipy


# In[3]:


pip install scipy


# In[68]:


pip install matplotlib


# In[71]:


C4['price'].hist()
#testing normality of price


# In[72]:


C4['availability_365'].hist()
#testing normality of availability 365


# In[77]:


C4.price[C4.room_type == 'Entire home/apt'].hist()
#testing normality of price of entire home/apt


# In[80]:


C4.price[C4.room_type == 'Private room'].hist()
#testing normality of price of private room


# In[81]:


C4.price[C4.room_type == 'Hotel room'].hist()
#testing normality of price of hotel room


# In[82]:


C4.price[C4.room_type == 'Shared room'].hist()
#testing normality of price of shared room


# In[84]:


C4.price[C4.room_type == 'Entire home/apt'].mean()


# In[85]:


C4.price[C4.room_type == 'Private room'].mean()


# In[86]:


C4.price[C4.room_type == 'Hotel room'].mean()


# In[87]:


C4.price[C4.room_type == 'Shared room'].mean()


# In[ ]:


#finding the means of each room type's price
#the mean of entire home/apt is 220.79
#the mean of private room is 149.28
#the mean of hotel room is 187.79
#the mean of shared room is 76.32


# In[89]:


from scipy.stats import ttest_ind


# In[90]:


ttest_ind(C4.price[C4.room_type == 'Entire home/apt'], C4.price[C4.room_type == 'Private room'])


# In[91]:


ttest_ind(C4.price[C4.room_type == 'Hotel room'], C4.price[C4.room_type == 'Shared room'])


# In[92]:


ttest_ind(C4.price[C4.room_type == 'Hotel room'], C4.price[C4.room_type == 'Private room'])


# In[93]:


ttest_ind(C4.price[C4.room_type == 'Entire home/apt'], C4.price[C4.room_type == 'Shared room'])


# In[94]:


#testing independent ttest of entire and private room
#testing independent ttest of hotel and shared room
#testing independent ttest of hotel room and private room
#testing independent ttest of entire and shared room


# In[ ]:




