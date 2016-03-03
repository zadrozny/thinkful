#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
Take the loan data and process it as you did previously to build your linear regression model.

Break the data-set into 10 segments following the example provided here in KFold .

Compute each of the performance metric (MAE, MSE or R2) for all the folds. 
The average would be the performance of your model.

Comment on each of the performance metric you obtained.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# for example, if k=10, we are implementing 10-fold cross validation

k = 10

n = len(loansData['Interest.Rate'])

kf = KFold(n, n_folds=k) 

for train, test in kf:
    print("%s\n %s" % (train, test)) # How are train and test being generated?

rms = mean_squared_error(y_actual, y_predicted)
mas = mean_absolute_error(y_actual, y_predicted)
r2 = r2_score(y_actual, y_predicted)

# Mean Squared Error
# Mean absolute error
# R-squared