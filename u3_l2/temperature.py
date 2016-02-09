#!/usr/bin/python2
# -*- coding: utf-8 -*-


'''
Go through the the sequence of temperature readings and calculate 
the change between days and find the greatest range in high temperatures 
in the month you measured. 

Which city had the greatest variation? 

What is the distribution of the difference? 

Does the result surprise you? Why or why not?
'''

import datetime
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
import numpy as np


con = lite.connect('weather.db')
cur = con.cursor()

df = pd.read_sql_query('''SELECT * FROM daily_temp 
                          ORDER BY day_of_reading''',
                          con,index_col='day_of_reading')



tmp_flux = {}
for city in df.columns.values:
    col = df[city].tolist()
    tmp_flux[city] = sum([abs(col[i] - col[i-1]) 
                          for i in range(1, len(col))])



max_flux = sorted(tmp_flux.items(), 
                     key=lambda x: x[1], reverse=True)[0]


start = datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%d %H:%M:%S')
end = datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%d %H:%M:%S')


print("The city with the greatest temp flucuation between %s and %s is %s"
        ", where the temperature fluctuated by %s degrees over 30 days" 
        % (start, end, max_flux[0], max_flux[1]))



N = 5
degrees = tmp_flux.values()

ind = np.arange(N)    
width = .9      

p1 = plt.bar(ind, degrees, width, color='r')
plt.ylabel('Degrees')
plt.title('Temperature fluctuation by city: 2016-01-09 to 2016-02-07')
plt.xticks(ind + width/2., ('New_York', 'Boston', 'Los_Angeles', 'San_Francisco', 'Chicago'))
plt.yticks(np.arange(0, 200, 10))
plt.show()