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

#%%
#Building dashbords
sns.set_style('darkgrid')
f,axes = plt.subplots(2,2,figsize=(12,15),sharex=False,sharey=False)

k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0,0])
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0,1])


w = sns.boxplot(data=movies[movies.Genre=='Drama'],x='Year',
                y='CriticRating',ax=axes[1,0])
#these two need to stay togheteher to m
k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,
                 shade_lowest=False,cmap='Reds',ax=axes[1,1])
k1b = sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='Reds',ax=axes[1,1])

k1.set(xlim=(-40,160))
k2.set(xlim=(-40,160))


#%%

sns.set_style('darkgrid')
f,axes = plt.subplots(2,2,figsize=(12,15),sharex=False,sharey=False)

k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0,0])
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0,1])


w = sns.boxplot(data=movies[movies.Genre=='Drama'],x='Year',
                y='CriticRating',ax=axes[1,0])
#these two need to stay togheteher to m
#k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,
                 #shade_lowest=False,cmap='Reds',ax=axes[1,1])
#k1b = sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='Reds',ax=axes[1,1])

#axes is an pyplot object; seaborn is on top is an add on of pyplot
n1=axes[1,1].hist(movies.CriticRating, bins=15,color='red')

k1.set(xlim=(-40,160))
k2.set(xlim=(-40,160))


#%%
#Styling Tips
sns.set_style('dark',{"axes.facecolor":"black"})
f,axes = plt.subplots(2,2,figsize=(12,15),sharex=False,sharey=False)
#Plot [0,0]
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,
                 shade=True,shade_lowest=True,cmap='inferno',ax=axes[0,0])
k1b = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,
                 cmap='cool',ax=axes[0,0])
#Plot [0,1]
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,
                 shade=True,shade_lowest=True,cmap='inferno',ax=axes[0,1])
k2b = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,
                 cmap='cool',ax=axes[0,1])
#plot [1,0]
w = sns.violinplot(data=movies,x='Year',y='BudgetMillions',ax=axes[1,0],
                   palette='YlOrRd')
#these two need to stay togheteher to m
#Plopt[1,1]
z1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,
                 shade_lowest=False,cmap='Blues_r',ax=axes[1,1])
z1b = sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='gist_gray_r',ax=axes[1,1])

k1.set(xlim=(-40,160))
k2.set(xlim=(-40,160))
plt.show()
















