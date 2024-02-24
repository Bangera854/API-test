#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
 'start':'1',
 'limit':'15',
 'convert':'USD'
}
headers = {
 'Accepts': 'application/json',
 'X-CMC_PRO_API_KEY': 'e1db00ca-8d53-45a3-8b64-48ee0941034d',
}

session = Session()
session.headers.update(headers)

try:
 response = session.get(url, params=parameters)
 data = json.loads(response.text)
 print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
 print(e)
 


# In[2]:


type(data)


# In[3]:


import pandas as pd


pd.set_option('display.max_columns',None)

pd.set_option('display.max_rows', None)


# In[5]:


#Normalizes the data and makes it all pretty in a dataframe
df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df_append = pd.DataFrame(df)
df2 = pd.concat([df,df_append])


# In[6]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'e1db00ca-8d53-45a3-8b64-48ee0941034d',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.to_datetime('now')
    df2
    
    #_append = pd.DataFrame(df2)
    #df2 = pd.concat([df,df_append])
    
    if not os.path.isfile(r'C:\Users\Sandarsh\OneDrive\Documents\Fake\API.csv'):
        df.to_csv(r'C:\Users\Sandarsh\OneDrive\Documents\Fake\API.csv', header='column_names')
    else:
        df.to_csv(r'C:\Users\Sandarsh\OneDrive\Documents\Fake\API.csv', mode = 'a', header='False')
        


# In[7]:


import os
from time import time
from time import sleep

for i in range(150):
    api_runner()
    print('API runner completed')
    sleep(60)
exit()


# In[8]:


df72 = pd.read_csv(r'C:\Users\Sandarsh\OneDrive\Documents\Fake\API.csv')
df72


# In[9]:


df3=df.groupby('name',sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3


# In[10]:


df4 = df3.stack()
df4


# In[39]:


type(df4)


# In[40]:


df5 = df4.to_frame(name='values')
df5


# In[41]:


type(df5)


# In[43]:


df5.count()


# In[44]:


index = pd.Index(range(90))
df6 = df5.reset_index()
df6


# In[46]:


df7 = df6.rename(columns={'level_1':'percent_change'})
df7


# In[59]:


df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1','24h','7d','30d','60d','90d'])
df7


# In[60]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[63]:


sns.catplot(x='percent_change',y='values',hue='name',data=df7,kind='point', height = 10, aspect=0.8)


# In[68]:


df10 = df2[['name','quote.USD.price','timestamp']]
df10 = df10.query("name == 'Solana'")
df10


# In[69]:


sns.set_theme(style="darkgrid")
sns.lineplot(x='timestamp', y='quote.USD.price', data=df10)


# In[ ]:




