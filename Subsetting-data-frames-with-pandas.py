# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:07:51 2020

@author: Juvette
"""
import pandas as pd
import os

stats = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Demographic-Data.csv')

print(stats)

print(stats.info())

#%%

### Susetting data frame in Pandas
print(stats.head())

#%%
### Susetting data frame in Pandas


print(stats[100:110])

print(stats[185:])

print(stats[:10])

#%%

#Quick exercise: Refresher
#Reverse dataframe
print(stats[::-1])
print(stats[:50])

#%%

print(stats[50::-1])

#%%
stats = stats[::-1]

print(stats)

#%%
#get only every 20th row
print(stats[::20])

#%%
#part 2. Columns
print(stats.columns)

print(stats['Country Name'])

#%%

stats.columns = ['CountryName','CountryCode','BirthRate','InternetUsers','IncomeGroup']

print(stats['CountryName'].head())

#%%

print(stats[['CountryName', 'BirthRate']].head())

print(stats['CountryName'].tail())

#%%

print(stats.BirthRate)
#%%
#Part 3 - combaining the two: rows and columns

print(stats[2:20][['CountryName','BirthRate']])










