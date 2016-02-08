#!/usr/bin/python2
# -*- coding: utf-8 -*-


'''
Record the number of bikes available every minute for an hour across 
all of New York City in order to see which station or set of stations 
is the most active in New York City for that hour. 

Activity is defined as the total number of bicycles taken out or returned 
in an hour. So if 2 bikes are brought in and 4 bikes are taken out, 
that station has an activity level of 6. 
'''

import datetime
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
from collections import Counter


con = lite.connect('citi_bike.db')
cur = con.cursor()

df = pd.read_sql_query('''SELECT * FROM available_bikes 
                          ORDER BY execution_time''',
                          con,index_col='execution_time')


station_activity = {}
for station in df.columns.values[1:]:
    col = df[station].tolist()
    station_activity[station] = sum([abs(col[i] - col[i-1]) 
                                    for i in range(1, len(col))])

max_station = sorted(station_activity.items(), 
                     key=lambda x: x[1], reverse=True)[0]


# Get reference information from SQLite
cur.execute('''SELECT id, stationname, latitude, longitude 
               FROM citibike_reference WHERE id = ?''', 
               (max_station[0].strip('_'),))

data = cur.fetchone()
start = datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%d %H:%M:%S')
end = datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%d %H:%M:%S')


print("The most active station is station" 
      "id %s at %s latitude: %s longitude: %s " % data)
print("With %d bicycles coming and going"
      "in the hour between %s and %s" % (max_station[1], start, end,))


inp = Counter(station_activity.values())
plt.title('Stations vs Bike activity')
plt.xlabel('Bike activity')
plt.ylabel('Stations')
plt.bar(inp.keys(), inp.values())
plt.show()