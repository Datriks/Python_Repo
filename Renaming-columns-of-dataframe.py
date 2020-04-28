# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:36:55 2020

@author: Juvette
"""
import pandas as pd
import os

#Renaming-columns-of-dataframe
stats = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Demographic-Data.csv')

print(stats)
print(stats.tail())
print(stats.head())
#%%
print(stats.info())
print(stats.columns)
print(len(stats.columns))

#%%

print(stats.describe().transpose())

#%%

print(stats.head())

#%%
stats.columns = ['a','b','c','d','e']
print(stats.head())

#%%
stats.columns = ['CountryName', 'CountryCode', 'Birthrate', 'Internetusers',\
       'IncomeGroup']

print(stats.head())












