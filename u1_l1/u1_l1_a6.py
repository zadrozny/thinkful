#!/usr/bin/python
# -*- coding: utf-8 -*-


from collections import defaultdict
import csv


with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    keys = next(inputFile).split(',')
    print keys
    # ['Continent', 'ElevationZone', 'UrbanRuralDesignation', 'Population1990', 'Population2000', 'Population2010', 'Population2100', 'LandArea\n']
    total = 0
    continents = defaultdict(int)
    areas = defaultdict(int)
    for line in inputFile:
        # total += int(line.split(',')[-1].rstrip('\n'))
        # print int(line.split(',')[-1])
        row = line.split(',')
        continent, pop2010, pop2100, area = row[0], int(row[-3]), int(row[-2]), int(row[-1].rstrip('\n'))
        continents[continent] += pop2100# - pop2010)
        areas[continent] += area 
        

print sorted(continents.items(), key=lambda x: x[1], reverse=True)         
print sum(v for k,v in continents.items())


for k in continents:
	print k, continents[k] / float(areas[k])

