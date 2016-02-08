#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
Download data from an API using Python.
Clean, process, store, and visualize weather data for 5 major cities in the U.S.
'''

import requests
import datetime
from time import time
import sqlite3 as lite
from key import apikey

url = 'https://api.forecast.io/forecast/'+apikey+'/' # + ','.join(LATITUDE,LONGITUDE,TIME)

cities = {'New_York': '40.663619,-73.938589',
          'Los_Angeles': '34.019394,-118.410825',
          'Boston': '42.331960,-71.020173',
          'Chicago': '41.837551,-87.681844',
          'San_Francisco': '37.727239,-123.032229'
         }


end_date = datetime.datetime.now()

# the current value being processed
query_date = end_date - datetime.timedelta(days=30) 


con = lite.connect('weather.db')
cur = con.cursor()

with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)


for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #query for the value
        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))

        with con:
            #insert the temperature max to the database
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

        query_date += datetime.timedelta(days=1)


con.close() # a good practice to close connection to database            




# start_date = datetime.datetime.now() - datetime.timedelta(days=30)
# for city in cities:
# 	for day in range(30):
# 		u = url + cities[city] + ',' + start_date.strftime('%Y-%m-%dT12:00:00')
# 		print u
# 		# print requests.get(u).text
# 		start_date += datetime.timedelta(days=1)
# 		break
# 	break 


# ​https://api.forecast.io/forecast/a86a039479d9b4862789e9c0cf591826/37.8267,-122.423,1454965260