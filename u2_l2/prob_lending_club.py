#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Write a script...that: reads in the loan data, cleans it, and loads it into a pandas DataFrame. 

Use the script to generate and save a boxplot, histogram, and QQ-plot for the values in the "Amount.Requested" column. 

Be able to describe the result and how it compares with the values from the "Amount.Funded.By.Investors". 
'''

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


# loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Automatically loads data into DataFrame object pd.DataFrame() not necessary
loansData = pd.read_csv('loansData.csv') # From the local file

# Clean the data
loansData.dropna(inplace=True)

# Get the count, mean, std, min, quartiles, max
column = loansData["Amount.Funded.By.Investors"]
s = pd.Series(column)
print s.describe()


# Boxplot
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.savefig("Lending Club--Amount Funded By Investors--Boxplot.png")
plt.show()


# Histogram: Does it look normally distributed?
loansData.hist(column='Amount.Funded.By.Investors', histtype='bar')
plt.ylabel('Frequency')
plt.xlabel('Amount')
plt.title('Amount Funded by Investors')
plt.savefig("Lending Club--Amount Funded By Investors--Histogram.png")
plt.show()


# QQ plot: How well the data fits a normal distribution
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("Lending Club--Amount Funded By Investors--QQ.png")
plt.show()

