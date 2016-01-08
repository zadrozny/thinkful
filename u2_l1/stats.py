# #!/usr/bin/python
# # -*- coding: utf-8 -*-

'''
Write a script called "stats.py" that prints the 
mean, median, mode, range, variance, and standard deviation 
for the Alcohol and Tobacco dataset with full text 
(ex. "The range for the Alcohol and Tobacco dataset is ..."). 
'''

import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]


column_names = data[0] # Header
data_rows = data[1:]   # Rows

# Load data
df = pd.DataFrame(data_rows, columns=column_names)

# Convert strings to floats
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


features = ['mean', 'median', 'mode', 'range', 
            'variance', 'standard deviation']


def get_feature(attr, col, df):
    if attr == 'mean':
        return df[col].mean()
    if attr == 'median':
        return df[col].median()
    if attr == 'mode':
        return stats.mode(df[col])[0][0]            
    if attr == 'range':
    	return max(df[col]) - min(df[col])
    if attr == 'variance':
        return df[col].var()  
    if attr == 'standard deviation':
        return df[col].std()           	


for f in features:
    a = round(get_feature(f, 'Alcohol', df), 2)
    t = round(get_feature(f, 'Tobacco', df), 2)
    print("The {} for the Alcohol and Tobacco dataset is {} for alcohol and {} for tobacco.\n".format(f, a, t))