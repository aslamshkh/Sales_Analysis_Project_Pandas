#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing lybraries


# In[1]:


import pandas as pd


# In[ ]:


# Uploading data


# In[9]:


pd.read_csv(r"C:\Users\aslam\OneDrive\Desktop\Python\Data Analytics Panda\Diwali Sales Data.csv")


# In[7]:


# Saving the dataset as df


# In[3]:


df = pd.read_csv(r"C:\Users\aslam\OneDrive\Desktop\Python\Data Analytics Panda\Diwali Sales Data.csv")
df


# In[ ]:


# Checkign the shape of the dataset


# In[12]:


df.shape


# In[ ]:


# Checking the top values of the datset which will be 5 by default


# In[13]:


df.head()


# In[ ]:


# Checking the top 7 values of the dataset


# In[15]:


df.head(7)


# In[ ]:


# Checking the details of the entire dataset


# In[16]:


df.info()


# In[ ]:


# Found 2 columns "Status" & "unnamed1" with no data. Hence, they are being deleted


# In[18]:


df.drop(columns = 'Status')


# In[19]:


df = df.drop(columns = 'Status')
df


# In[20]:


df = df.drop(columns = 'unnamed1')
df


# In[ ]:


# Checkign if there is any null values in the data set


# In[21]:


df.isnull().sum()


# In[ ]:


# Deleting all the null values found in "Amount" column


# In[22]:


df.dropna()


# In[ ]:


# Saving the changes


# In[26]:


df = df.dropna()


# In[ ]:


# Ceckign if the desired rows are deleted or not


# In[27]:


df.isnull().sum()


# In[ ]:


# CHecking all the discription os the dataset


# In[31]:


df.describe()


# In[ ]:





# In[39]:


# Exploratory Data Analysis (EDA)


# In[41]:


df.columns


# In[ ]:


# Checkign the spent amount based on genders


# In[62]:


df.groupby('Gender')['Amount'].sum()


# In[ ]:


# Cheking spent based on age group


# In[4]:


df.groupby('Age Group')['Amount'].sum()


# In[ ]:


# Checking total orders statewise


# In[68]:


df.groupby('State')['Orders'].sum().sort_values(ascending=False)


# In[ ]:


# Checkign the same information by adding the amount as well


# In[80]:


df.groupby('State').agg({'Amount': 'sum', 'Orders': 'sum'}).sort_values(by='Amount', ascending=False)


# In[ ]:


# Checking the sales count based on Martial Status


# In[81]:


df.groupby('Marital_Status')['Orders'].sum().sort_values(ascending=False)


# In[ ]:


# Checkign spent based on maritial status


# In[82]:


df.groupby('Marital_Status')['Amount'].sum().sort_values(ascending=False)


# In[ ]:


# Checkign which purchansed the most


# In[83]:


df.groupby('Occupation')['Amount'].sum().sort_values(ascending=False)


# In[ ]:


# Checking top 5 product catagory based on order count and total amount


# In[85]:


df.groupby('Product_Category').agg({'Amount': 'sum', 'Orders': 'sum'}).sort_values(by='Amount', ascending=False).head()


# In[ ]:





# In[ ]:




