# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:57:01 2020

@author: Juvette
"""
#Stacked Histograms
import numpy as np
import pandas as pd
np.random.seed(0)
import seaborn as sns
sns.set(style='white',color_codes=True)
import warnings
warnings.simplefilter('ignore')
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize']= 10,4

#%%
sns.set(style='darkgrid',color_codes=True)

#%%
movies = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Movie-Ratings.csv')
movies.columns=['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']
movies.Genre = movies.Genre.astype('category')
movies.Film = movies.Film.astype('category')
movies.Year = movies.Year.astype('category')

#%% Select data on drama criterion
movies.Genre =='Drama'
print(movies.Genre == 'Drama')

#%%
#create the filter drama for the budget in millions

print(movies[movies.Genre=='Drama'].BudgetMillions)

#%%
h1 = plt.hist(movies.BudgetMillions)

#%%
h1 = plt.hist(movies[movies.Genre=='Action'].BudgetMillions,color='b',bins=15)
h1 = plt.hist(movies[movies.Genre=='Drama'].BudgetMillions,color='r',bins=15)
h1 = plt.hist(movies[movies.Genre=='Thriller'].BudgetMillions,color='g',bins=15)

#%%----we want to be stacked

h2 = plt.hist([movies[movies.Genre=='Action'].BudgetMillions,
               movies[movies.Genre=='Drama'].BudgetMillions,
               movies[movies.Genre=='Thriller'].BudgetMillions,
               movies[movies.Genre=='Comedy'].BudgetMillions],
              bins=15,stacked=True)

#%%---chart number 4

list1= list()
mylabels=list()

for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)  
           
h = plt.hist(list1,bins=15,stacked=True,rwidth=1,label=mylabels)
plt.legend()



































































