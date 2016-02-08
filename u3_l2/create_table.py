#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
Create table for project.
'''

import sqlite3 as lite

con = lite.connect('weather.db')
cur = con.cursor()

sql = '''CREATE TABLE daily_temp ( day_of_reading INT, 
	                                 New_York REAL, 
                                   Los_Angeles REAL, 
                                   Boston REAL, 
                                   Chicago REAL, 
                                   San_Francisco REAL);'''

with con:
    cur.execute(sql)