#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# code from https://www.simplifiedpython.net/python-download-file/


# In[ ]:


# https://www2.erie.gov/sheriff/sites/www2.erie.gov.sheriff/files/uploads/data/InmateList.pdf


# In[9]:


import requests


# In[10]:


print('Download starting...')


# In[11]:


url = 'https://www2.erie.gov/sheriff/sites/www2.erie.gov.sheriff/files/uploads/data/InmateList.pdf'


# In[12]:


r = requests.get(url)


# In[13]:


filename = url.split('/')[-1]


# In[14]:


with open(filename,'wb') as output_file:
    output_file.write(r.content)


# In[15]:


print('Download complete!')


# In[ ]:




