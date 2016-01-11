#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Write a script called "chi_squared.py" that loads the data, cleans it, performs the chi-squared test, and prints the result. Push your code to GitHub and enter the link below.
'''

import pandas as pd
from collections import Counter
from scipy import stats

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Drop null rows
loansData.dropna(inplace=True)

freq = Counter(loansData['Open.CREDIT.Lines'])

# Perform a Chi-Squared test (scipy.stats.chisquare) to verify your answer.
# In the absence of expected observations, the observations are treated as equally likely by scipy:
# Expected frequencies in each category. By default the categories are assumed to be equally likely.'
chi, p = stats.chisquare(freq.values())

print chi
print p