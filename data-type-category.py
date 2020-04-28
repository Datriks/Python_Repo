# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:05:33 2020

@author: Juvette
"""
#Movie Rating------Category Data Type

import pandas as pd
import os

print(os.getcwd())

os.chdir('D:\\OneDrive - office365hubs.com\\.Python for data science')


print(os.getcwd())


movies = pd.read_csv('Movie-Ratings.csv')

print(movies)
#%%
print(movies.head())

#%%

print(movies.columns)

#%%

movies.columns = ['Film','Genre','CriticRating','AudienceRating','BudgetMillions',
                 'Year']

print(movies.head())

#%%

movies.info()

#%%

print(movies.describe().transpose())

#%%
#convert variables into categorical variables

movies.Film = movies.Film.astype('category')

print(movies)
























