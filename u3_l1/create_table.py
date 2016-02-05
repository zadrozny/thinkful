#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Unit 3, lesson 1, assignment 4

import requests
import sqlite3 as lite
from pandas.io.json import json_normalize


con = lite.connect('citi_bike.db')
cur = con.cursor()

with con:
    cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')


    r = requests.get('http://www.citibikenyc.com/stations/json')
    df = json_normalize(r.json()['stationBeanList'])
    #extract the column from the DataFrame and put them into a list
    station_ids = df['id'].tolist() 
    #add the '_' to the station name and also add the data type for SQLite
    station_ids = ['_' + str(x) + ' INT' for x in station_ids]
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")   