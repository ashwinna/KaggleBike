
# coding: utf-8

# In[224]:




# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
get_ipython().magic('matplotlib inline')


# In[6]:

df = pd.read_csv('train.csv', header=0)
df['hour']=df['datetime'].map( lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S').tm_hour )
df.head()

#grouped.head()





# In[14]:




# In[70]:

#Anayze hour
grouped_hour=df.groupby(['hour'])
#hour_count = grouped_hour.sum()
hour_axis = list(range(0, 24))
#grouped_hour.head(n=1)
total_hourly_sum = grouped_hour['count'].sum()
plt.plot(total_hourly_sum)
total_reg_sum = grouped_hour['registered'].sum()
plt.plot(total_reg_sum)
total_cas_sum =  grouped_hour['casual'].sum()
plt.plot(total_cas_sum)
#Analyze hour and weekday

#df_mean_x = grouped[grouped['holiday']==1]['season']
#df_mean_casual_0=grouped[grouped['holiday']==0]['casual']
#df_mean_casual_1=grouped[grouped['holiday']==1]['casual'].mean()
#df_mean_registered_0=grouped[grouped['holiday']==0]['registered'].mean()
#df_mean_registered_1=grouped[grouped['holiday']==1]['registered'].mean()
#df_mean_reset=df_mean_registered_1.reset_index()['registered']+df_mean_registered_0.reset_index()['registered']+df_mean_casual_1.reset_index()['casual']+df_mean_casual_0.reset_index()['casual']
#df_mean_casual_0
#plt.plot(hour_axis, hour_count)


# In[90]:

#hour, workingday=1
grouped_hour=df[df['workingday']==1].groupby(['hour'])
#hour_count = grouped_hour.sum()
hour_axis = list(range(0, 24))
#grouped_hour.head(n=1)
total_hourly_sum = grouped_hour['count'].sum()
plt.plot(total_hourly_sum)
total_reg_sum = grouped_hour['registered'].sum()
plt.plot(total_reg_sum)
total_cas_sum =  grouped_hour['casual'].sum()
plt.plot(total_cas_sum)




# In[89]:

#hour, workingday=0
grouped_hour=df[df['workingday']==0].groupby(['hour'])
#hour_count = grouped_hour.sum()
hour_axis = list(range(0, 24))
#grouped_hour.head(n=1)
total_hourly_sum = grouped_hour['count'].sum()
plt.plot(total_hourly_sum)
total_reg_sum = grouped_hour['registered'].sum()
plt.plot(total_reg_sum)
total_cas_sum =  grouped_hour['casual'].sum()
plt.plot(total_cas_sum)


# In[91]:

#hour, workingday=0
grouped_hour=df[df['workingday']==0].groupby(['hour'])
#hour_count = grouped_hour.sum()
hour_axis = list(range(0, 24))
#grouped_hour.head(n=1)
total_hourly_sum = grouped_hour['count'].sum()
#plt.plot(total_hourly_sum)
total_reg_sum = grouped_hour['registered'].sum()
plt.plot(total_reg_sum)
total_cas_sum =  grouped_hour['casual'].sum()
#plt.plot(total_cas_sum)
#hour, workingday=0
grouped_hour=df[df['workingday']==1].groupby(['hour'])
#hour_count = grouped_hour.sum()
hour_axis = list(range(0, 24))
#grouped_hour.head(n=1)
total_hourly_sum = grouped_hour['count'].sum()
#plt.plot(total_hourly_sum)
total_reg_sum = grouped_hour['registered'].sum()
plt.plot(total_reg_sum)
total_cas_sum =  grouped_hour['casual'].sum()
#plt.plot(total_cas_sum)


# In[ ]:



