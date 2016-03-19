# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:49:02 2016

@author: aaron
"""

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import re

df = pd.read_csv('train.csv', header=0)


df.dropna(inplace=True, how='any')


# Divide the dataset into test, train
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df['relevance_rounded'] = df['relevance'].map(lambda x: round(x))

df['exact'] = pd.Series([True if st.lower() in pt.lower() else False 
                      for st, pt in zip(df['search_term'], df['product_title'])])

def jaccard_dist(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    return float(len(lst1 & lst2)) / len(lst1 | lst2)

def words_shared(st, pt):
    st_list = re.split('\s', st.lower())
    pt_list = re.split('\s', pt.lower())
    dist = jaccard_dist(st_list, pt_list)
    return dist

df['jaccard'] = pd.Series([words_shared(st, pt) 
                      for st, pt in zip(df['search_term'], df['product_title'])])


train, test = df[df['is_train']==True], df[df['is_train']==False]

features = ['exact','jaccard']

clf = RandomForestClassifier(n_jobs=2, class_weight = 'balanced', oob_score = True, criterion = 'entropy')

y, _ = pd.factorize(train['relevance_rounded']) # 0, 1, 2

clf.fit(train[features], y)


# Predicting on those features will output predictions that match y
preds = clf.predict(test[features])

target_names = ['1', '2', '3']

out = [target_names[pred] for pred in preds]

pd.crosstab(test['relevance_rounded'], preds, rownames=['actual'], colnames=['preds'])

pd.crosstab(test['relevance_rounded'], np.asarray(out), rownames=['actual'], colnames=['preds'])
