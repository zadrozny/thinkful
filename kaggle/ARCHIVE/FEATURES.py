
# coding: utf-8

# In[3]:

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import re
from math import log
from collections import OrderedDict
from collections import Counter


# In[4]:

# product_descriptions = pd.read_csv('DATA/product_descriptions.csv', header=0, encoding = "ISO-8859-1")
# attributes = pd.read_csv('DATA/attributes.csv', header=0, encoding = "ISO-8859-1")
# train = pd.read_csv('DATA/train.csv', header=0,  encoding = "ISO-8859-1")
# test = pd.read_csv('DATA/test.csv', header=0,  encoding = "ISO-8859-1")
from DATA import product_descriptions, attributes, train, test


# # FEATURES

# ### EXACT MATCH, between search term (as phrase) and product title, allowing only differences in case

# In[5]:

# A boolean

train['exact'] = pd.Series([True if st.lower() in pt.lower() else False 
                      for st, pt in zip(train['search_term'], train['product_title'])])


# ### OVERLAPPING WORDS, allowing for differences in case

# In[6]:

# A count >= 0

train['overlapping_words'] = pd.Series([len(set(st.lower().split()) & set(pt.lower().split()))
                      for st, pt in zip(train['search_term'], train['product_title'])])


# ### PERCENTAGE OVERLAPPING WORDS, allowing for differences in case

# In[7]:

train['percentage_overlapping_words'] = pd.Series([len(set(st.lower().split()) & 
                                                       set(pt.lower().split()))/float(len(st.split()))
                                                       for st, pt in zip(train['search_term'], train['product_title'])])


# # TF-IDF

# In[8]:

# Function for calculating TF-IDF score for doc, query pair

def calc(doc, query, N=1, D={}):
    doc = [w.lower() for w in doc.split()]
    counts = Counter(doc)
    query = query.lower().split()
    return sum([counts[word] * log(N / (1+D[word])) for word in set(query) & set(doc)]) # 1 to avoid div by 0


# ## TF-IDF: product descriptions (all) + product titles

# In[9]:

# Number of documents
N = len(set(product_descriptions['product_uid'] + train['product_uid']))


# In[10]:

# Dictionary of word-count pairs
words_product_descriptions = ''.join(product_descriptions['product_description']).split()
words_train = ''.join(train['product_title']).split()
D = Counter(words_product_descriptions + words_train) # Not lowercased


# In[11]:

# Test
# frequent = sorted(d.items(), key=lambda x: x[1])[:50:-1]
# frequent


# In[12]:

scores = OrderedDict()

for row in zip(train['id'], train['product_uid'], train['product_title'], train['search_term']):
    _id, pid, pt, st = row
    TF = Counter(pt.split())
    score = sum([calc(pt, word, N, D) for word in st.lower().split()])
    scores[_id] = score


# In[13]:

# Vector
tf_idf = list(scores.values())
train['tf_idf'] = tf_idf
train.head()


# ## TF-IDF: product descriptions (not all -- only those with product titles) + product titles

# ## TF-IDF: product titles alone (no descriptions)

# ## TF-IDF: product titles, descriptions, and attributes

# ## TF-IDF sans stopwords (does it make any difference?)

# In[14]:

# Dictionary of word-count pairs
words_product_descriptions = ''.join(product_descriptions['product_description']).split()
words_train = ''.join(train['product_title']).split()
d = Counter(words_product_descriptions + words_train) # Not lowercased


# In[15]:

# Function for calculating TF-IDF score for doc, query pair

def calc(doc, query):
    doc = [w.lower() for w in doc.split()]
    counts = Counter(doc)
    query = query.lower().split()
    return sum([counts[word] * log(N / (1+d[word])) for word in set(query) & set(doc)]) # 1 to avoid div by 0


# In[16]:

scores = OrderedDict()

for row in zip(train['id'], train['product_uid'], train['product_title'], train['search_term']):
    _id, pid, pt, st = row
    TF = Counter(pt.split())
    score = sum([calc(pt, word) for word in st.lower().split()])
    scores[_id] = score


# ## QUERIES CONTAINING WORDS NOT IN DICTIONARY

# In[ ]:




# ## TF-IDF sans stopwords (any difference?)

# In[17]:

from nltk.corpus import stopwords
stopwords = stopwords.words('english')


# ## JACCARD DISTANCE

# In[18]:

# def jaccard_dist(phrase1, phrase2):
#     '''Returns the Jaccard distance for two phrases, eg, search query and product title'''
#     lst1, lst2 = set(phrase1.lower().split()), set(phrase2.lower().split())
#     return float(len(lst1 & lst2)) / len(lst1 | lst2)

# def words_shared(st, pt):
#     st_list = re.split('\s', st.lower())
#     pt_list = re.split('\s', pt.lower())
#     dist = jaccard_dist(st_list, pt_list)
#     return dist

# train['jaccard'] = pd.Series([words_shared(st, pt) 
#                       for st, pt in zip(train['search_term'], train['product_title'])])


# In[19]:

# What do 3's have in common?


# In[ ]:

# What do 1's have in common?


# ### BAG OF WORDS: product descriptions, attributes, titles -- product by product

# In[ ]:




# In[ ]:




# ### DEFAULT PENALTY: products that appear too many times -- and have low relevance -- suggesting that they are defaults for when the search engine is stumped

# In[20]:

# Aggregate on product ID's themselves and penalize too popular products.
from collections import Counter
d = Counter(train['product_uid'])
for pid in d: 
    if d[pid] > 5:
        pass
#         print(pid, d[pid],) 


# In[ ]:



