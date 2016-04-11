
# coding: utf-8

# In[ ]:

# Simple Linear Regression with Hour


# In[58]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import csv as csv
get_ipython().magic('matplotlib inline')
import pip
from sklearn.linear_model import LinearRegression


# In[ ]:




# In[59]:

#read training data
df = pd.read_csv('train.csv', header=0)
df['hour']=df['datetime'].map( lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S').tm_hour )
df2 = df[['hour','count']]
df2['workingday']=0;


# In[60]:

#train
df2.plot(kind='scatter', x='hour', y='count')


# In[61]:

lm = LinearRegression()
lm.fit(df2[['hour','workingday']], df2['count'])
lm.coef_

lm.intercept_


# In[65]:

#read test data and write predictions
df_test = pd.read_csv('test.csv', header=0)
df_test['hour']=df_test['datetime'].map( lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S').tm_hour );
#predict

df_test['workingday']=0
df_test['count'] = lm.predict(df_test[['hour','workingday']])
df_test.head()
#plt.plot(df2['count'])
#df2['predict'] = df2['hour'] * 10.49 + 70;

#plt.plot(df2['predict'].head(n=300), 'ro')
#plt.plot(df2['count'].head(n=300), 'bo')



# In[63]:

#write result
df_result =pd.concat([df_test['datetime']],axis=1)
type(df_result)
df_result['count']=df_test['count'];
df_result.to_csv(path_or_buf='model1.csv', index=False)


# In[64]:




# In[ ]:




# In[ ]:



