
import numpy as np
import time
import csv as csv


# In[ ]:




# In[27]:

#read training data





# In[28]:

#read test data and write predictions
test_file = open('test.csv')
test_file_object = csv.reader(test_file)
header = next(test_file_object)

prediction_file = open("bikesharingoutput.csv", 'w')
prediction_file_object = csv.writer(prediction_file)
prediction_file_object.writerow(["PassengerId", "Survived"])


# In[30]:

prediction_file.close()


# In[90]:




# In[89]:




# In[91]:




# In[ ]:



