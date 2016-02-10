#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
https://courses.thinkful.com/data-001v2/project/4.1.4

Use the following code to generate a toy regression dataset, 
and split the data into 70% training and 30% testing data. 

Using mean squared error as a metric, compare the performance of 
different polynomial curves in the training set and in the testing set. 
'''

# Not working: poly_linear.predict(test_df['X']) taking 300 and output 1000 samples. What's going on?


import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# http://stackoverflow.com/a/18623635
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Set seed for reproducible results
np.random.seed(414)

# Gen toy data
X = np.linspace(0, 15, 1000)
y = 3 * np.sin(X) + np.random.normal(1 + X, .2, 1000)

train_X, train_y = X[:700], y[:700]
test_X, test_y = X[700:], y[700:]

train_df = pd.DataFrame({'X': train_X, 'y': train_y})
test_df = pd.DataFrame({'X': test_X, 'y': test_y})


# Linear Fit
poly_linear = smf.ols(formula='y ~ 1 + X', data=train_df).fit()
y_actual = test_df['y']
y_predicted = poly_linear.predict({'X': test_df['X']}) # Pass DF that matches the formula (Kyle's code)
rms = mean_squared_error(y_actual, y_predicted)
mas = mean_absolute_error(y_actual, y_predicted)
r2 = r2_score(y_actual, y_predicted)
print rms, mas, r2

# QUADRATIC FIT
poly_quadratic = smf.ols(formula='y ~ 1 + X + I(X**2)', data=train_df).fit()
y_actual = test_df['y']
y_predicted = poly_quadratic.predict({'X': test_df['X']})
rms = mean_squared_error(y_actual, y_predicted)
mas = mean_absolute_error(y_actual, y_predicted)
r2 = r2_score(y_actual, y_predicted)
print rms, mas, r2