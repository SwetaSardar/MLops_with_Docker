#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib


# In[2]:


model = joblib.load('SalaryData.pk1')


# In[6]:


year_exp = float(input("\nEnter your Experience:  "))


# In[7]:


result = model.predict([[ year_exp ]])


# In[8]:


print(result)


# In[ ]:





# In[ ]:




