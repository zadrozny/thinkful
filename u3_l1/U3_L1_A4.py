#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Unit 3, lesson 1, assignment 4


import collections
import pandas as pd
import requests
import time
import sqlite3 as lite
from dateutil.parser import parse 
from pandas.io.json import json_normalize


with lite.connect('citi_bike.db') as con:
    cur = con.cursor()
    for foo in range(60):
        r = requests.get('http://www.citibikenyc.com/stations/json')
        # df = json_normalize(r.json()['stationBeanList'])

        exec_time = parse(r.json()['executionTime']) 
        cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

        id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station
        #loop through the stations in the station list
        for station in r.json()['stationBeanList']:
            id_bikes[station['id']] = station['availableBikes']

        
        for k, v in id_bikes.iteritems():
            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")    
        
        time.sleep(60)