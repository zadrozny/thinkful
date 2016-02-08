#!/usr/bin/python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import numpy as np
import sqlite3 as lite


url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

header = soup.find(attrs={'class': 'lheader'}).text.split('\n')

table = []
for country in soup.findAll(attrs={'class': 'tcont'}):
    table.append(country.text.encode('utf-8').split('\n'))


df = pd.DataFrame(table)[0:93] # 93
df = df.replace('', np.nan)
df = df.transpose()
df = df.dropna(how='any') # Dropping columns seems not to work
df = df.transpose()




con = lite.connect('UN.db')
cur = con.cursor()


# Insert educational attainment into database

sql = "INSERT INTO indicators (id, country, year, total, men, women) VALUES (?,?,?,?,?,?)"
for row in df.itertuples():
	_id, country, year, total, men, women = row
	cur.execute(sql, (_id, country, year, total, men, women))
	con.commit


# Insert GDP into database

with open('gdp/8c7a4208-9d17-460f-9bb3-afdc8423004f_v2.csv','rU') as gdp:
    for _ in range(4): next(gdp) # skip the first four lines
    rows = csv.reader(gdp)

    for r in rows:
        vals = [r[0]] + r[43:-6] # country, years 1999 - 2010
        sql = 'INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
        cur.execute(sql, vals)

con.close()       