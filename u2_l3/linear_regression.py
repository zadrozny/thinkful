#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Convert FICO scores into numerical value & save it in a new column called FICO.Score. 
# Since the ranges are small, pick the first number to represent the range

# converted = [int(n.split('-')[0]) for n in loansData['FICO.Range']]
# loansData['FICO.Score'] = pd.Series(converted, index=loansData.index)
# converted = map(lambda x: x.split('-')[0], loansData['FICO.Range'])
# loansData['FICO.Score'] = converted

# .map() seems to be preferred way: http://stackoverflow.com/a/12555491/1366410
# http://pandas.pydata.org/pandas-docs/stable/cookbook.html#new-columns
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x.split('-')[0]))

# HISTOGRAM 
plt.figure()
p = loansData['FICO.Score'].hist()
plt.title('FICO Scores')
plt.xlabel('Score')
plt.ylabel('Count')
plt.show()

# SCATTERPLOT
plt.figure()
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()

# InterestRate = b + a1(FICOScore) + a2(LoanAmount)

intrate = [float(ir.strip('%')) for ir in loansData['Interest.Rate']] # Clean 
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']


# Reshape data: Convert from Series datatype

# The dependent variable
y = np.matrix(intrate).transpose()


# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()


# Join columns to create an input matrix 
# One column per independent variable
x = np.column_stack([x1,x2])


# Build linear model:
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit() 


# Output results summary:
print f.summary()