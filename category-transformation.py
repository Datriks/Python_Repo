# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:41:24 2020

@author: Juvette
"""
import pandas as pd
import os

movies = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Movie-Ratings.csv')

#%%

print(movies.head())

#%%

print(movies.describe().transpose())

#%%

print(movies.info())

#%%

print(movies.columns)

#%%

movies.columns=['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']

#%%

print(movies)

#%%

movies.Film = movies.Film.astype('category')

print(movies.info())

#%%

movies.Genre = movies.Genre.astype('category')

print(movies.info())

#%%

movies.Year = movies.Year.astype('category')

#%%

print(movies.info())

#%%
#What level of category a variable holds

print(movies.Genre.cat.categories)

#%%

print(movies.describe().transpose())

#%%























