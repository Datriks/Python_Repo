# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:43:06 2020

@author: Juvette
"""
import numpy as np
np.random.seed(0)
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import warnings
warnings.simplefilter('ignore')
sns.set(style='darkgrid', color_codes=True)
plt.rcParams['figure.figsize']=10,4

movies = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Movie-Ratings.csv')
movies.columns = ['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']

movies.Genre = movies.Genre.astype('category')
movies.Film = movies.Film.astype('category')
movies.Year = movies.Year.astype('category')

#%%
#Violinplots


z = sns.violinplot(data=movies,x='Genre',y='CriticRating')

#%%
#Boxplots

w = sns.boxplot(data=movies,x='Genre',y='CriticRating')

#%%

w = sns.boxplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating')

#%%

z = sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating')
















