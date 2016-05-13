
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


# In[7]:

from FEATURES import train # train.csv + relevance_rounded vector


# In[8]:

train.head()


# In[14]:

# Prepare to divide the dataset into test, train (lifted from sklearn Iris example)
train['is_train'] = np.random.uniform(0, 1, len(train)) <= .75

# Split data into training and test
train_data, test_data = train[train['is_train']==True], train[train['is_train']==False]

features = train.columns[[7, 8, 9, 10]] # Whether it's an exact match or not, and overlapping words

clf = RandomForestClassifier(n_jobs=2)
y, _ = pd.factorize(train_data['relevance_rounded']) # 0, 1, 2

clf.fit(train_data[features], y)

# Predicting on those features will output predictions that match y
preds = clf.predict(test_data[features])

target_names = test_data['relevance_rounded']
preds = target_names[clf.predict(test_data[features])]
preds.index = range(len(preds))
pd.crosstab(test_data['relevance_rounded'], preds, rownames=['actual'], colnames=['preds'])


# In[ ]:



