#!/usr/bin/python
# -*- coding: utf-8 -*-


# Note: Unclear what the "data in this lesson" is

'''
Write a script called "prob.py" that outputs frequencies, 
as well as creates and saves a boxplot, a histogram, and a QQ-plot 
for the data in this lesson. 
Make sure your plots have names that are reasonably descriptive.
'''

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats


data = [1, 4, 5, 6, 9, 9, 9]

c = Counter(data)

# calculate the number of instances in the list
count_sum = sum(c.values())

# Output frequencies
for k,v in c.iteritems():
    print k, round(float(v) / count_sum, 3)


# Boxplot
plt.boxplot(data)
plt.savefig("boxplot.png")
plt.show()


# Histogram
plt.hist(data, histtype='bar')
plt.savefig("histogram.png")
plt.show()


# QQ plot  
plt.figure()
graph1 = stats.probplot(data, dist="norm", plot=plt)
plt.savefig("qq.png")
plt.show()
