#!/usr/bin/env python
# coding: utf-8

# 
# # Car Dataset

# In[1]:


import pandas as pd


# In[4]:


car = pd.read_csv(r"C:\Users\Nabeel\Downloads\2. Cars Data1.csv")
# it wil show you uncode error if u don't put r before commas
# after succcessful step it means that it has imported the data successfully


# In[5]:


car.head()
# top values


# In[7]:


# check shape
# no need to write tuple after wrting shape

car.shape


# In[8]:


# for checking  null values

car.isnull()
# not any null value is clearly visible


# In[15]:


car.isnull().sum()
# now we can see that wehave soo many null values
# you can see cylinder is 0 when we have compalted our below statement


# In[14]:


car["Cylinders"].fillna(car["Cylinders"].mean(),inplace =True)
# it will show u data of cylinders that is filled with the mean
# but to make changes permanent we will also use ,inplace=True to make changes permanent


# In[19]:


""" Show  the ["Make"] and the value.counts() """

car["Make"].value_counts()
# now you can see that it has shown us the Make which is actually the models and the value counts as well.


# In[21]:


car.head(10)
# it has shown us the top 10 values


# In[25]:


"""We have to find their Origins which are specifically in ASIA AND EUROPE"""
# Use isin function for checking the values in origins

car[car["Origin"].isin(["Asia","Europe"])]
# use . isin not , and write the values in the squarebracets


# In[27]:


car[car["Origin"].isin(["USA"])]
# of u don't use the cars [    ------ ]at the start then ut will show you the values where USA is not the Origin


# In[29]:


""" Remove the records where the weight is above 3500"""

car["Weight"]>3500
# as I have told you earlier that if you won't put car [car["Weight"]>3500].. then it will show you values in the T/F


# In[30]:


car[car["Weight"]>3500]


# In[31]:


# No we will remove values which are more than 3500

car[~(car["Weight"]>3500)]
# and yes as you can see that it has removed all of those values which were more than 3500


# In[32]:


car.shape
# First we had 432 rows ..now we have 230 rows after removing which are more than 3500


# In[34]:


car["MPG_City"]=car["MPG_City"].apply(lambda x:x+3)


# In[35]:


car
#the values in mpg city is increased by 3 becuase of this


# In[ ]:




