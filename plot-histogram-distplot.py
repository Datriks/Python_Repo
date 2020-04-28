# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:15:49 2020

@author: Juvette
"""
#--Histograms

from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.simplefilter('ignore')
plt.rcParams['figure.figsize']= 10,4
sns.set(style='white',color_codes=True)

#%%
sns.set(style='darkgrid',color_codes=True)

#%%
movies = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Movie-Ratings.csv')
movies.columns=['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']
movies.Genre = movies.Genre.astype('category')
movies.Film = movies.Film.astype('category')
movies.Year = movies.Year.astype('category')

#%%

m1 = sns.distplot(movies.AudienceRating,bins=15)

#%%

m2 = sns.distplot(movies.CriticRating,bins=15,color='red')

#%%

n1 = plt.hist(movies.AudienceRating,bins=15)

#%%

n2= plt.hist(movies.CriticRating,bins=15)

#%%

































