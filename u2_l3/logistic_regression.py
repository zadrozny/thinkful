#!/usr/bin/python
# -*- coding: utf-8 -*-

# logistic_regression.py

# Needs review. Uploading for reference. 

'''
In this lesson, we're going to be looking at the same data as the last lesson, 
but we're going to ask a different question, one that has a binary outcome: 
What is the probability of getting a loan from the Lending Club for $10,000 
at an interest rate ≤ 12% with a FICO score of 750?
'''

import math
import pandas as pd
import statsmodels.api as sm


# Load clean data from last lesson 
loansData = pd.read_csv('loansData_clean.csv')

# print list(loansData.columns.values) # Scaffolding

'''
Add a column to your dataframe indicating whether the interest rate 
is < 12%. This would be a derived column that you create from the 
interest rate column. You name it IR_TF. It would contain binary values, 
i.e.'0' when interest rate < 12% or '1' when interest rate is >= 12%
'''
ir_tf = loansData['IR_TF'] = loansData['Interest.Rate'].map(
	            lambda x: 0 if float(x.strip('%')) < 12 else 1)


# CANNOT REPLICATE:
# print loansData[loansData['Interest.Rate'] == 10].head() # should all be True
# print loansData[loansData['Interest.Rate'] == 13].head() # should all be False


'''
Statsmodels needs an intercept column in your dataframe, 
so add a column with a constant intercept of 1.0.
'''
intercept = loansData['intercept'] = loansData['Interest.Rate'].map(lambda x: 1.0)


'''
Convert FICO scores into a numerical value, and save it in a new 
column called FICO.Score. Since the ranges are small, we're going 
to go ahead and pick the first number to represent the range.
https://courses.thinkful.com/data-001v2/assignment/2.3.2
'''
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x.split('-')[0]))


'''
Create a list of the column names of our independent variables, 
including the intercept, and call it ind_vars
'''
# Which is the amount we're using, requested or funded?
ind_vars = ['intercept', 'FICO.Score', 'Amount.Requested'] 
ind_vars = ['intercept', 'FICO.Score', 'Amount.Funded.By.Investors']


'''Define the logistic regression model'''
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])


'''Fit the model'''
result = logit.fit()


'''Get the fitted coefficients from the results.'''
coeff = result.params
b, a1, a2 = coeff # 60.1250452808 -0.0874232156551 0.000174027967496


'''
Write a function called logistic_function that will take a FICO Score and 
a Loan Amount of this linear predictor, and return p. (Try not to hardcode 
any values if you can! Hint: pass the coefficients object to the function 
as an argument.)
'''
# Values at https://courses.thinkful.com/data-001v2/project/2.4.3:
# b, a1, a2 = -60.125, 0.087423, 0.000174 

def logistic_function(FicoScore, LoanAmount, b, a1, a2):
    '''p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))'''
    return 1/(1 + math.e**(b + a1*FicoScore - a2*LoanAmount))

print(logistic_function(720, 10000, 72.8828, 0.087423, 0.000174))


# QUESTIONS:
# Should I be transposing?
# https://courses.thinkful.com/data-001v2/project/2.3.3

# # # The independent variables shaped as columns
# # x1 = np.matrix(ir_tf).transpose()
