# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 07:52:51 2020

@author: Juvette
"""
#Facet Grid Creation
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
vis1 = sns.lmplot(data=movies,x='CriticRating',y='AudienceRating',fit_reg=False,
                  hue='Genre',size=6,aspect=1)

#%%

g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')

g = g.map(plt.scatter,'CriticRating','AudienceRating')

#%%
#Can be populated with any type of chart

g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')

g = g.map(plt.hist,'BudgetMillions')

#%%
#Add an aextra argument

g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50, linewidth=0.5,edgecolor='black')
g = g.map(plt.scatter,'CriticRating','AudienceRating',**kws)

#%%
#Controlling axes and ading diagonals
g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50, linewidth=0.5,edgecolor='black')
g = g.map(plt.scatter,'CriticRating','AudienceRating',**kws)

g.set(xlim=(0,100),ylim=(0,100))

for ax in g.axes.flat:
    ax.plot((0,100),(0,100),c='red',ls='--')

g.add_legend()

#Chart number 5 to include in our raport




















