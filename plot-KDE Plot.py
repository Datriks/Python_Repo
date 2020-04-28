# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:58:53 2020

@author: Juvette
"""
#This is the Kernel Density estimate

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

vis1 = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating',
                  fit_reg=False,hue='Genre',size=7,aspect=1)

#%%

k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,
                 shade_lowest=False,cmap='Reds')


k1b = sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='Reds')

#%%













