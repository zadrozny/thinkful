
# coding: utf-8

# In[16]:

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np


# In[17]:

train = pd.read_csv('DATA/train.csv', header=0, encoding = "ISO-8859-1")


# # Features / vectors: 

# In[18]:

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


# In[19]:

# Prepare to divide the dataset into test, train (lifted from sklearn Iris example)
train['is_train'] = np.random.uniform(0, 1, len(train)) <= .75

# Split data into training and test
train_data, test_data = train[train['is_train']==True], train[train['is_train']==False]


# In[20]:

features = train.columns[[7, 8, 9]] # Whether it's an exact match or not

# clf = RandomForestClassifier(n_jobs=2)
clf = RandomForestClassifier(n_jobs=2, class_weight = 'balanced', oob_score = False, criterion = 'entropy')

y, _ = pd.factorize(train_data['relevance_rounded']) # 0, 1, 2

clf.fit(train_data[features], y)

# Predicting on those features will output predictions that match y
preds = clf.predict(test_data[features])

# target_names = test['relevance_rounded']
target_names = ['1', '2', '3']
out = [target_names[pred] for pred in preds]

# preds = target_names[clf.predict(test[features])]

preds = clf.predict(test_data[features])

# preds.index = range(len(preds))
# pd.crosstab(test['relevance_rounded'], preds, rownames=['actual'], colnames=['preds'])
print(pd.crosstab(test_data['relevance_rounded'], np.asarray(out), rownames=['actual'], colnames=['preds']))


# In[8]:

ct = pd.crosstab(test['relevance_rounded'], np.asarray(out), rownames=['actual'], colnames=['preds'])
print(ct)


# In[10]:

row = ct.ix[1]
col = ct['1']
print(row)
print(col)


# In[21]:

index = list(pd.crosstab(test_data['relevance_rounded'], preds))
total = 0
for i in list(ct):
    total += sum(list(ct[i]))

true_positives = 0
false_positives = 0
false_negatives = 0
true_negatives = 0

for i in zip(list(ct), range(1, len(ct)+1)): 
    print(i)
    row = list(ct.ix[i[1]])
    column = list(ct[i[0]])
    
    tp = row[i[1]-1]
    true_positives  += tp
    false_negatives += sum(row)-tp
    false_positives += sum(column) - tp
    true_negatives = total - tp
    
print(true_positives, false_positives, false_negatives, true_negatives)


# In[22]:

f1 = float(2*true_positives) / (2 * true_positives + false_positives + false_negatives)
f1

