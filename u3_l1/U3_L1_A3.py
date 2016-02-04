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

test = sum([1 for s in r.json()['stationBeanList'] if s[u'testStation'] == True])

print 'There are {} test stations.'.format(test)


# How many stations are "In Service"?

in_service = sum([1 for s in r.json()['stationBeanList'] 
                    if s[u'statusValue'] == "In Service"])

print 'There are {} stations in service.'.format(in_service)


# How many are "Not In Service"?

not_in_service = sum([1 for s in r.json()['stationBeanList'] 
                        if s[u'statusValue'] == "Not In Service"])

print 'There are {} stations not in service.'.format(in_service)


# Any other interesting variables values that need to be accounted for?



# What is the mean number of bikes in a dock?

availableBikes = sum([s[u'availableBikes'] for s in r.json()['stationBeanList']])

mean = availableBikes / in_service

print 'Stations have a mean of {} bikes.'.format(mean)


# What is the median?

df = json_normalize(r.json()['stationBeanList'])

# print df['availableBikes'].mean()
median = df['availableBikes'].median()

print 'Stations have a median of {} bikes.'.format(median)

# How does this change if we remove the stations that aren't in service?

# df['availableBikes'] = [row for row in df if row[u'statusValue'] == "In Service"]

# df['availableBikes'].dropna(inplace=True, subset=[df[u'statusValue'] == "Not In Service"])
df['availableBikes'] = [row[0] for row in zip(df['availableBikes'], df['statusValue']) if row[1] == "In Service"]

mean = df['availableBikes'].mean()
median = df['availableBikes'].median()

print 'The mean and median number of bikes for stations \
       that are in service is {mean} and {median}, respectively'.format(mean=mean, median=median)