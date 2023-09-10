#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 

df = pd.read_csv("C:/Users/Kimchiyeon/Desktop/khuda/a/LDGMENT_MERGE.csv")
df1 = pd.DataFrame(df)

df1.corr(method = 'pearson')


# In[3]:


df1.head()


# In[8]:


df1.drop(['Unnamed: 0','RESPOND_ID','EXAMIN_YM','OVSEA_TOUR_TY_VALUE'], axis =1,inplace = True)


# In[13]:


df1.head()


# In[15]:


import seaborn as sns
sns.countplot(x = 'SEXDSTN_FLAG_CD', data = df1)


# In[22]:


sns.scatterplot(x = 'AGRDE_FLAG_NM', y = 'HSHLD_INCOME_DGREE_NM', data = df1, hue = 'SEXDSTN_FLAG_CD')


# In[52]:


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df1['sex'] = encoder.fit_transform(df['SEXDSTN_FLAG_CD'])
df1.head()


# In[64]:


salary_mapping = {
    '300만원 미만': 2500000, 
    '300이상500만원 미만':4000000,
    '500이상700만원 미만': 6000000,
    '700만원 이상': 7500000
}

df1['급여수치'].apply(lambda x: salary_mapping[x])

print(df1)


# In[ ]:




