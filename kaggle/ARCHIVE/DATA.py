
# coding: utf-8

# In[6]:

import pandas as pd
import numpy as np


# In[7]:

product_descriptions = pd.read_csv('DATA/product_descriptions.csv', header=0, encoding = "ISO-8859-1")
attributes = pd.read_csv('DATA/attributes.csv', header=0, encoding = "ISO-8859-1")
train = pd.read_csv('DATA/train.csv', header=0,  encoding = "ISO-8859-1")
test = pd.read_csv('DATA/test.csv', header=0,  encoding = "ISO-8859-1")


# In[8]:

# Since relevance is an aggregate, values are continuous rather than discrete
# It appears the classifier can only handle a limited number of values
# So we round up
train['relevance_rounded'] = train['relevance'].map(lambda x: round(x))


# In[9]:

train.head()


# # DATA FILES & FIELDS
# 
# ## product_descriptions.csv
# * product_uid
# * product_description
# 
# ## attributes.csv
# * product_uid
# * name
# * value
# 
# ## train.csv
# * id
# * product_uid
# * product_title
# * search_term
# * relevance
# 
# ## test.csv
# * id
# * product_uid
# * product_title
# * search_term
# 
# ## sample_submission.csv
# * id
# * relevance

# # DATA FIELDS & FILES
# 
# 
# ## id - a unique Id field which represents a (search_term, product_uid) pair
# * test.csv
# * train.csv
# * sample_submission.csv
# 
# ## product_uid - an id for the products
# * attributes.csv
# * product_descriptions.csv
# * test.csv
# * train.csv
# 
# ## product_title - the product title
# * test.csv
# * train.csv
#     
# ## product_description - the text description of the product (may contain HTML content)
# * product_descriptions.csv
#     
# ## search_term - the search query
# * test.csv
# * train.csv
# 
# ## relevance - the average of the relevance ratings for a given id
# * sample_submission.csv
# * train.csv
# 
# ## name - an attribute name
# * attributes.csv
# 
# ## value - the attribute's value
# * attributes.csv
