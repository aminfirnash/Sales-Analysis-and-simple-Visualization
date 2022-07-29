#!/usr/bin/env python
# coding: utf-8

# # Sales Analysis on Store products

# In[2]:


#Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import plotly.offline as pyo
import plotly.graph_objs as go


# ### Load in Dataset 

# In[4]:


df = pd.read_csv('train 2.csv')
df.sample(10)


# In[13]:


s2 = df.groupby(['date', 'item'])['sales'].sum()
s2.head(10)


# In[18]:


s3 = s2.unstack()
#s2.loc[s2['item']==1]


# In[19]:


s3.head()


# In[25]:


s3=s3.transpose()


# In[26]:


s3.head()


# In[30]:


sales1 = pd.DataFrame()
sales1['item1'] = s3.iloc[0].values


# In[40]:


for i in range(2,51):
    sales1[f'item{i}'] = s3.iloc[i-1].values
    
sales1.head()


# In[34]:


sales1.set_index(s3.columns, inplace=True)
sales1.head()


# In[36]:


sales1.index


# In[38]:


data = go.Scatter(x=sales1.index, y=sales1.item1, mode='lines')

layout = go.Layout(title='Sales Graph on item 1', xaxis ={'title': 'Date'},
                  yaxis={'title':'No of Sales'})

fig = go.Figure(data=data, layout=layout)

pyo.iplot(fig)


# In[41]:


data = go.Scatter(x=sales1.index, y=sales1.item42, mode='lines')

layout = go.Layout(title='Sales Graph on item 42', xaxis ={'title': 'Date'},
                  yaxis={'title':'No of Sales'})

fig = go.Figure(data=data, layout=layout)

pyo.iplot(fig)


# ## Observation:
# - Every year the sale of the product increases gradually
# - Each product follows the same pattern.
#     - Sale peaks during mid of the year
#     - Sale at the end of the year drops than the mid, however stays up than the start of the year.

# In[ ]:




