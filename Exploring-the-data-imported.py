# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 08:08:15 2020

@author: Juvette
"""
#Exploring-the-data-imported
stats = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Demographic-Data.csv')
print(stats)

#%%
print(len(stats))

print(len(stats.columns))

print(stats.columns)

#%% top rows

print(stats.head(10))

#%%  bottom rows

print(stats.tail())

#%% information of the column
print(stats.info()) #like str function in R

#%% get stats on the column

print(stats.describe()) #like the summary in R

#%%
print(stats.describe())
print(stats.describe().transpose())


















