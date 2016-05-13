
# coding: utf-8

# In[12]:

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np


# In[13]:

train = pd.read_csv('DATA/train.csv', header=0,  encoding = "ISO-8859-1")


# # Features / vectors: 

# In[14]:

# Since relevance is an aggregate, values are continuous rather than discrete
# It appears the classifier can only handle a limited number of values
# So we round up
train['relevance_rounded'] = train['relevance'].map(lambda x: round(x))

# Create the feature 'exact match', allowing only for differences in case
train['exact'] = pd.Series([True if st.lower() in pt.lower() else False 
                      for st, pt in zip(train['search_term'], train['product_title'])])

# Create the feature 'overlapping words', allowing for differences in case
train['overlapping_words'] = pd.Series([len(set(st.lower().split()) & set(pt.lower().split()))
                      for st, pt in zip(train['search_term'], train['product_title'])])

# Feature: percentage 'overlapping words', allowing for differences in case
train['percentage_overlapping_words'] = pd.Series([len(set(st.lower().split()) & set(pt.lower().split()))/float(len(st.split()))
                      for st, pt in zip(train['search_term'], train['product_title'])])

# Feature: jaccard distance
def jaccard_dist(phrase1, phrase2):
    '''Returns the Jaccard distance for two phrases, eg, search query and product title'''
    lst1, lst2 = set(phrase1.lower().split()), set(phrase2.lower().split())
    return float(len(lst1 & lst2)) / len(lst1 | lst2)

train['jaccard'] = pd.Series([jaccard_dist(st, pt) 
                      for st, pt in zip(train['search_term'], train['product_title'])])


# In[15]:

# Prepare to divide the dataset into test, train (lifted from sklearn Iris example)
train['is_train'] = np.random.uniform(0, 1, len(train)) <= .75

# Split data into training and test
train_data, test_data = train[train['is_train']==True], train[train['is_train']==False]


# In[16]:

features = train.columns[[7, 8, 9, 10]] # Whether it's an exact match or not

# clf = RandomForestClassifier(n_jobs=2)
clf = RandomForestClassifier(n_jobs=2, class_weight = 'balanced', oob_score = False, criterion = 'entropy')

y, _ = pd.factorize(train_data['relevance_rounded']) # 0, 1, 2

clf.fit(train_data[features], y)

# Predicting on those features will output predictions that match y
preds = clf.predict(test_data[features])

# target_names = test['relevance_rounded']
target_names = ['1', '2', '3', '4']
out = [target_names[pred] for pred in preds]

# preds.index = range(len(preds))
# pd.crosstab(test['relevance_rounded'], preds, rownames=['actual'], colnames=['preds'])
ct = pd.crosstab(test_data['relevance_rounded'], np.asarray(out), rownames=['actual'], colnames=['preds'])
print (ct)


# # Crosstab summation

# In[17]:

index = list(pd.crosstab(test_data['relevance_rounded'], preds))
total = 0
for i in list(ct):
    total += sum(list(ct[i]))

true_positives  = 0
false_positives = 0
false_negatives = 0
true_negatives  = 0

for i in zip(list(ct), range(1, len(ct)+1)):
    row = list(ct.ix[i[1]])
    column = list(ct[i[0]])
    tp = row[i[1]-1]
    true_positives  += tp
    false_negatives += sum(row)-tp
    false_positives += sum(column) - tp
    true_negatives += total - tp
    
print(true_positives, false_positives, false_negatives, true_negatives)


# In[18]:

# https://en.m.wikipedia.org/wiki/F1_score

f1 = float(2*true_positives) / (2 * true_positives + false_positives + false_negatives)
f1


# # Naive Bayes

# In[19]:

clf_nb = GaussianNB()
clf_nb.fit(train_data[features], y)

preds = clf_nb.predict(test_data[features])

target_names = ['1', '2', '3', '4']
out = [target_names[pred] for pred in preds]

# Predicting on those features will output predictions that match y

print(pd.crosstab(test_data['relevance_rounded'], np.asarray(out), rownames=['actual'], colnames=['preds']))


# In[20]:

ct = pd.crosstab(test_data['relevance_rounded'], preds)
print(ct)


# In[ ]:



