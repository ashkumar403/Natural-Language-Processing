#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Starting a Practical use case of Natural Text Processing (NLP)


# In[3]:


import numpy as np


# In[4]:


import pandas as pd


# In[22]:


import sklearn as skl


# In[25]:


#skl.show_versions()
from sklearn.model_selection import train_test_split


# In[7]:


df=pd.read_csv('moviereviews5.csv')


# In[11]:


df


# In[18]:


overview=df['overview']


# In[19]:


print(overview)


# In[16]:


vote_average=df['vote_average']


# In[17]:


print(vote_average)


# In[26]:


Overview_train,Overview_test, vote_average_train, vote_average_test=train_test_split(overview,vote_average, test_size=0.25)


# In[29]:


print (Overview_train)


# In[31]:


print (Overview_test)


# In[ ]:




