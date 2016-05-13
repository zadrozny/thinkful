#!/usr/bin/python2
# -*- coding: utf-8 -*-

from pandas import DataFrame
import os
import pandas as pd

FILE_DIR = os.path.dirname(os.path.realpath(__file__))

# DATA FIELDS

'''
    id - a unique Id field which represents a (search_term, product_uid) pair
    	test.csv
    	train.csv
    	sample_submission.csv

    product_uid - an id for the products
    	attributes.csv
    	product_descriptions.csv
    	test.csv
    	train.csv

    product_title - the product title
    	test.csv
    	train.csv
    
    product_description - the text description of the product (may contain HTML content)
    	product_descriptions.csv
    
    search_term - the search query
    	test.csv
    	train.csv

    relevance - the average of the relevance ratings for a given id
    	sample_submission.csv
    	train.csv

    name - an attribute name
    	attributes.csv

    value - the attribute's value
    	attributes.csv
'''

sub = 50

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# relevance_instructions.docx

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PRODUCT DESCRIPTIONS
# 'product_uid' 'product_description'
# 100001	"Not only do angles make joints stronger  they also provide more consistent	 straight corners. Simpson Strong-Tie offers a wide variety of angles in various sizes and thicknesses to handle light-duty jobs or projects where a structural connection is needed. Some can be bent (skewed) to match the project. For outdoor projects or those where moisture is present	 use our ZMAX zinc-coated connectors	 which provide extra resistance against corrosion (look for a ""Z"" at the end of the model number).Versatile connector for various 90 connections and home repair projectsStronger than angled nailing or screw fastening aloneHelp ensure joints are consistently straight and strongDimensions: 3 in. x 3 in. x 1-1/2 in.Made from 12-Gauge steelGalvanized for extra corrosion resistanceInstall with 10d common nails or #9 x 1-1/2 in. Strong-Drive SD screws"

# [124428 rows x 2 columns]
with open(FILE_DIR + '/product_descriptions.csv', 'r') as f:
	product_descriptions = pd.read_csv(f)
	product_descriptions = product_descriptions[['product_uid', 'product_description']] # Drop NaN
	product_descriptions_sub = product_descriptions[:sub]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ATTRIBUTES
# "product_uid"	"name"	"value"
# 100001	"Bullet01"	"Versatile connector for various 90° connections and home repair projects"

with open(FILE_DIR + '/attributes.csv', 'r') as f:
	attributes = pd.read_csv(f)
	attributes_sub = attributes[:sub]

# print list(attributes.columns.values)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TRAIN
# "id"	"product_uid"	"product_title"	"search_term"	"relevance"
# 2	100001	"Simpson Strong-Tie 12-Gauge Angle"	"angle bracket"	3
# 3	100001	"Simpson Strong-Tie 12-Gauge Angle"	"l bracket"	2.5

# [74067 rows x 5 columns]
with open(FILE_DIR + '/train.csv', 'r') as f:
	train = pd.read_csv(f)
	train = train[[0, 1, 2, 3, 4]]
	train_sub = train[:sub]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TEST
# "id"	"product_uid"	"product_title"	"search_term"
# 1	100001	"Simpson Strong-Tie 12-Gauge Angle"	"90 degree bracket"
# 4	100001	"Simpson Strong-Tie 12-Gauge Angle"	"metal l brackets"
# 5	100001	"Simpson Strong-Tie 12-Gauge Angle"	"simpson sku able"
# 6	100001	"Simpson Strong-Tie 12-Gauge Angle"	"simpson strong  ties"
# 7	100001	"Simpson Strong-Tie 12-Gauge Angle"	"simpson strong tie hcc668"
# 8	100001	"Simpson Strong-Tie 12-Gauge Angle"	"wood connectors"

# [166693 rows x 4 columns]
with open(FILE_DIR + '/test.csv', 'r') as f:
	test = pd.read_csv(f)
	test_sub = test[:sub]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# SAMPLE SUBMISSION
# 'id' 'relevance'
# 1	1
# 4	1
# 5	1
# 6	1
# 7	1
# 8	1

# [166693 rows x 2 columns]
with open(FILE_DIR + '/sample_submission.csv', 'r') as f:
	sample = pd.read_csv(f)
	sample_sub = sample[:sub]

# print pd.concat([attributes, product_descriptions, train], axis=1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# print attributes_sub, product_descriptions_sub, train_sub, test_sub, sample_sub

# print attributes_sub[:5]
print train_sub['product_title'][:5]