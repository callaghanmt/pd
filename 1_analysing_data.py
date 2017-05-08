
# coding: utf-8

# ## Analysing data with Python and numpy

# In[1]:

import numpy


# In[2]:

numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')


# ### Introducing variables

# In[3]:

weight_kg = 55


# In[4]:

print (weight_kg)


# In[5]:

print ("Weight in pounds: ", 2.2 * weight_kg)


# In[6]:

weight_kg = 57.5


# In[7]:

print ("Weight in pounds is now: ", 2.2 * weight_kg)


# In[8]:

get_ipython().magic('whos')


# In[9]:

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter = ',')


# In[10]:

get_ipython().magic('whos')


# In[11]:

print (data)


# In[12]:

# Find out what type of thing data is
print (type(data))


# In[13]:

print (data.dtype)


# In[14]:

# Finding the shape of an array
print (data.shape)


# In[ ]:

# This is 60 ROWS by 40 COLUMNS


# In[15]:

print (data[0,0])


# In[16]:

print (data[30,20])


# ## Slicing arrays

# In[17]:

# Get the first 4 rows (patients) and the first 10 columns (days)
print (data[0:4, 0:10])

# Starts at 0 and goes up to but not including the 4th row


# In[18]:

print (data[13:18, 5:10])


# In[19]:

# We don't need to include the upper and lower bound
print (data[:4, :10])


# In[20]:

# If you don't include an upper bound, it assumes we go right to the end
print (data[:4, 36:])


# In[21]:

# If we want to work out the average down each column (axis = 0)
print (numpy.mean (data, axis = 0))


# In[ ]:

# This is a mean for every column, as opposed to:
print (numpy.mean (data))


# In[22]:

# As a sanity check, we can check the shape of a result
print (numpy.mean (data, axis = 0))
print (numpy.mean (data, axis = 0).shape)


# ## Quick visualisations

# In[24]:

import matplotlib.pyplot


# In[25]:

get_ipython().magic('matplotlib inline')


# In[27]:

image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()


# In[28]:

# Let's look at average inflammation over time
avg_inflammation = numpy.mean (data, axis = 0)
avg_plot = matplotlib.pyplot.plot (avg_inflammation)
matplotlib.pyplot.show()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



