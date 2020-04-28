# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 08:42:48 2020

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
list1 = list()
mylabels = list()

for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
    mylabels.append(gen)
#Styling   
sns.set_style('whitegrid')  
fig,ax=plt.subplots()
fig.set_size_inches(11.7,8.27)#size A4 paper

h = plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)

plt.title('Movie Budget Distribution',fontsize=35,
          color='darkBlue',fontname='Consolas')
plt.ylabel('Number of Movies',fontsize=25,color='Red')
plt.xlabel('BudgetMillions',fontsize=25,color='Green')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(frameon=True,fancybox=True,shadow=True,
           framealpha=1,prop={'size':15})
#L = ax.legend()
#plt.setp(L.texts, family='Consolas')
plt.show()

















