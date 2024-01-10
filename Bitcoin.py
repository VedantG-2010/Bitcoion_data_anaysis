#!/usr/bin/env python
# coding: utf-8

# In[48]:


import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[49]:


os.listdir(r"D:\Data Analyst\project\bitcoin")


# In[50]:


data = pd.read_csv("D:/Data Analyst/project/bitcoin/bitcoin_price_Training - Training.csv")


# In[51]:


data.columns


# In[52]:


data.shape


# In[53]:


data.info()


# In[54]:


data.describe().T


# In[55]:


#convert date datatype object to datetime
data['Date'] = pd.to_datetime(data['Date'])
data['Date'].min()


# In[56]:


data['Date'].max()


# In[57]:


data.head()


# In[58]:


data.tail()


# In[59]:


data.sort_index(ascending=False).reset_index()


# In[60]:


#Analyze change in price of the bitcoin overtime
data.columns


# In[61]:


plt.figure(figsize=(20,12))
for index, col in enumerate (['Open', 'High', 'Low', 'Close'],1):
    plt.subplot(2,2,index)
    plt.plot(data['Date'],data[col])
    plt.title(col)


# In[62]:


#Analyze bitcoin prize using candle Stick chart
data.shape


# In[63]:


bitcoin_sample = data[0:50]


# In[64]:


get_ipython().system('pip install chart_studio')
get_ipython().system('pip install plotly')


# In[65]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot


# In[66]:


init_notebook_mode(connected=True)


# In[67]:


trace = go.Candlestick(x = bitcoin_sample['Date'],
             high = bitcoin_sample['High'], 
             open = bitcoin_sample['Open'],
             close=  bitcoin_sample['Close'],
             low  =  bitcoin_sample['Low'])


# In[68]:


candle_data = [trace]
layout = {
    'title':'Bitcoin historical Price',
    'axis':'Date'
}


# In[71]:


fig = go.Figure(data=candle_data, layout = layout)
fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()


# In[72]:


data['Close']


# In[73]:


#Analysing closing price in depth
data['Close'].plot()


# In[74]:


data.set_index('Date',inplace = True)


# In[75]:


data


# In[76]:


#Analysing closing price in depth
data['Close'].plot()


# In[79]:


plt.figure(figsize = (20,6))

plt.subplot(1,2,1)
data['Close'].plot()
plt.title('No scalinng')

plt.subplot(1,2,2)
np.log1p(data['Close']).plot()
plt.title('Log Scalling')
plt.yscale('Log')


# In[80]:


#resample data
#Closing price on yeaarly basis
data['Close'].resample('Y').mean()


# In[81]:


data['Close'].resample('Y').mean().plot()


# In[82]:


#Closing price on quaterly basis
data['Close'].resample('Q').mean()


# In[83]:


#Closing price on quaterly basis
data['Close'].resample('M').mean().plot()


# In[84]:


#Closing price on quaterly basis
data['Close'].resample('M').mean()


# In[85]:


#Closing price on quaterly basis
data['Close'].resample('M').mean().plot()


# In[86]:


#Analyze daily change in closing price
data['Close']


# In[91]:


data['Close_price_pct_change']=data['Close'].pct_change()*100
data['Close_price_pct_change']


# In[92]:


data['Close_price_pct_change'].plot()


# In[93]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot
init_notebook_mode(connected = True)



# In[94]:


pip install cufflinks


# In[95]:


import cufflinks as cf


# In[96]:


cf.go_offline()


# In[97]:


data['Close_price_pct_change']


# In[98]:


data['Close_price_pct_change'].iplot()


# In[ ]:





# In[ ]:




