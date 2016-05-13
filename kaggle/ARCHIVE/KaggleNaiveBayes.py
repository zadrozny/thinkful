
# coding: utf-8

# In[30]:

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB


# In[31]:

from DATA import train # train.csv + relevance_rounded vector


# ## Feature 'exact match', allowing only for differences in case

# In[44]:

train['exact'] = pd.Series([True if st.lower() in pt.lower() else False 
                      for st, pt in zip(train['search_term'], train['product_title'])])


# In[45]:

# Prepare to divide the dataset into test, train (lifted from sklearn Iris example)
train['is_train'] = np.random.uniform(0, 1, len(train)) <= .75

# Split data into training and test
train_data, test_data = train[train['is_train']==True], train[train['is_train']==False]


# In[54]:

# features = train.columns[['exact']] # Whether it's an exact match or not

features = ['exact']

clf = GaussianNB()
y, _ = pd.factorize(train_data['relevance_rounded']) # 0, 1, 2

clf.fit(train_data[features], y)

# Predicting on those features will output predictions that match y
preds = clf.predict(test_data[features])

target_names = test_data['relevance_rounded']
preds = target_names[clf.predict(test_data[features])]
preds.index = range(len(preds))
pd.crosstab(test_data['relevance_rounded'], preds, rownames=['actual'], colnames=['preds'])


# In[46]:

# >>> import numpy as np
# >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# >>> Y = np.array([1, 1, 1, 2, 2, 2])
# >>> from sklearn.naive_bayes import GaussianNB
# >>> clf = GaussianNB()
# >>> clf.fit(X, Y)
# GaussianNB()
# >>> print(clf.predict([[-0.8, -1]]))
# [1]
# >>> clf_pf = GaussianNB()
# >>> clf_pf.partial_fit(X, Y, np.unique(Y))
# GaussianNB()
# >>> print(clf_pf.predict([[-0.8, -1]]))
# [1]

