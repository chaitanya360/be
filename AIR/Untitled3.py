#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas
import numpy
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

data = pandas.read_csv('diabetes.csv')
train = numpy.array(data.iloc[0:700])
test = numpy.array(data.iloc[700:768])


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(train[:,0:8], train[:,8])
predicted = model.predict(test[:,0:8])
# print(test[:,8])
print(predicted)
count =0
for i in range(68):
    if(predicted[i] == test[i,8]):
        count = count + 1
print(count/68)


# In[52]:





# In[ ]:






# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




