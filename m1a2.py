#!/usr/bin/python
"""
=========================================================
Selection by location 
=========================================================
pd.dataframe.iloc[] allows selection by position by
reference to rows and columns. .loc[2:3 --> rows, 'col3' columns]

"""

import pandas as pd
df = pd.read_csv('C:/Users/Admin/DAT210x/Module2/Datasets/tutorial.csv')
print (df.describe(percentiles=None, include=None, exclude=None))
print (df.loc[2:4,'col3'])

# 