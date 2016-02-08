#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Unit 3, lesson 3, assignment 3

'''
Create a table with the country name, the male school life expectancy, 
the female school life expectancy and the year of the analysis. 
'''


import sqlite3 as lite


con = lite.connect('UN.db')
cur = con.cursor()


with con:
    cur.execute('CREATE TABLE indicators (id INT PRIMARY KEY, country TEXT, year INT, total INT, men INT, women INT)')
    cur.execute('CREATE TABLE gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010)')

    con.commit()
