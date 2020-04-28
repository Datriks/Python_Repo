# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:36:23 2020

@author: Juvette
"""
import numpy as np
import pandas as pd
np.random.seed(0)
import seaborn as sns
sns.set(style='white',color_codes=True)
import warnings
warnings.simplefilter('ignore')
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize']= 10,4
sns.set(style='darkgrid',color_codes=True)

movies = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Movie-Ratings.csv')
movies.columns=['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']

movies.Genre = movies.Genre.astype('category')
movies.Film = movies.Film.astype('category')
movies.Year = movies.Year.astype('category')

#%%

k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating)

#%% plot-subplots

f,axes = plt.subplots(1,2,figsize=(12,6),sharex=True,sharey=True)

k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0])
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[1])
k1.set(xlim=(-40,160))














