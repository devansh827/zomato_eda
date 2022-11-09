#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[6]:


df.columns


# In[8]:


df.info()


# In[9]:


df.describe()

missing values
explore numerical var
explore categorical var
finding relationship b/w features
# In[10]:


df.isnull().sum()


# In[14]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[17]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[19]:


df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[20]:


df.columns


# In[23]:


final_df=pd.merge(df,df_country,on='Country Code',how='left')


# In[24]:


final_df.head(2)


# In[26]:


final_df.dtypes


# In[27]:


final_df.columns


# In[28]:


final_df.Country.value_counts()


# In[63]:


country_names=final_df.Country.value_counts().index


# In[64]:


country_names


# In[40]:


##top 3 countries that use zomato
plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')


# zomato max records or transactions are from india after that from usa and then uk

# In[47]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[48]:


ratings


# In[49]:


##observation 
##when rating is from 4.5 to 9 excellent
##when ratings are bw 4.0 to 3.5 very good
#if rating is bw ...


# In[50]:


ratings.head()


# In[53]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x="Aggregate rating",y="Rating Count",data=ratings)


# In[58]:


sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color',data=ratings,palette=['white','red','orange','yellow','green','green'])


# observation
# max rating 2.5 to 3.4
# no rated count is very high
# 

# In[60]:


sns.countplot(x="Rating color",data=ratings,palette=['white','red','orange','yellow','green','green'])


# In[67]:


final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# max zero ratings are from india

# In[69]:


final_df.groupby(['Country','Currency']).size().reset_index()


# In[72]:


final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts()


# In[77]:


city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[79]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# In[87]:


cuisinestop=.groupby(["Cuisines"]).size().sort_values(ascending=False).head(10).reset_index().rename(columns={0:"Rating_count"})
cuisinestop

