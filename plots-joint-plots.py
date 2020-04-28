# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:01:20 2020

@author: Juvette
"""
from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.simplefilter('ignore')
plt.rcParams['figure.figsize']= 10,4
sns.set(style='white',color_codes=True)

#%%
movies = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Movie-Ratings.csv')
movies.columns=['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']
movies.Genre = movies.Genre.astype('category')
movies.Film = movies.Film.astype('category')
movies.Year = movies.Year.astype('category')

#%%----Joint Plots

j = sns.jointplot(data=movies,x='CriticRating',y='AudienceRating')

#%%

j = sns.jointplot(data=movies,x='CriticRating',y='AudienceRating',
                  color='red',marginal_kws=dict(bins=15, rug=True))

#%%
j = sns.jointplot(data=movies,x='CriticRating',y='AudienceRating',
                  color='red',height=5, ratio=3,
                  marginal_kws=dict(bins=15, rug=True))

#%%--Cgart number 1 for the report

j = sns.jointplot(data=movies,x='CriticRating',y='AudienceRating',kind='hex',
                  color='red',marginal_kws=dict(bins=15, rug=True),space=0.2)


#%%

j = sns.jointplot(data=movies,x='CriticRating',y='AudienceRating',kind='kde',
                  color='red',marginal_kws=dict(bins=15, rug=True),space=0.2)


















