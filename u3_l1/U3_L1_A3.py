#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Unit 3, lesson 1, assignment 3



from __future__ import division 
import matplotlib.pyplot as plt
import pandas as pd
import requests
from pandas.io.json import json_normalize

r = requests.get('http://www.citibikenyc.com/stations/json')

# Explore some functions
# r.text
# r.json()
# print r.json().keys()

key_list = [] # unique list of keys for each station listing
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)

# Explore some functions
# print r.json()['executionTime']            
# print r.json()['stationBeanList'][0]            


# Load into Pandas and explore
df = json_normalize(r.json()['stationBeanList'])


df['availableBikes'].hist()
plt.show()


df['totalDocks'].hist()
plt.show()


# Explore the other data variables. Are there any test stations?

condition = (df['testStation'] == True)
test = len(df[condition]['totalDocks'])
print 'There are {} test stations.'.format(test)


# How many stations are "In Service"?

condition = (df['statusValue'] == 'In Service')
in_service = len(df[condition]['totalDocks'])
print 'There are {} stations in service.'.format(in_service)


# How many are "Not In Service"?

condition = (df['statusValue'] == 'Not In Service')
in_service = len(df[condition]['totalDocks'])
print 'There are {} stations not in service.'.format(in_service)


# Any other interesting variables values that need to be accounted for?



# What is the mean number of bikes in a dock?

mean = df['availableBikes'].mean()
print 'Stations have a mean of {} bikes.'.format(mean)


# What is the median?

median = df['availableBikes'].median()
print 'Stations have a median of {} bikes.'.format(median)


# How does this change if we remove the stations that aren't in service?

condition = (df['statusValue'] == 'In Service')
mean = df[condition]['totalDocks'].mean()

median = df[condition]['totalDocks'].median()

print 'The mean and median number of bikes for stations ' \
       'that are in service is {mean} and {median}, respectively.'.format(mean=mean, median=median)


