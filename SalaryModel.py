#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd

import joblib

salary = pd.read_csv('SalaryData.csv')

x = salary['YearsExperience'].values.reshape(30,1)

y = salary['Salary']

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x , y)

joblib.dump(model , 'SalaryData.pk1')


# In[ ]:





# In[ ]:




