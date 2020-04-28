# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 08:03:45 2020

@author: Juvette
"""
#Visualising-with-Seaborn

#https://seaborn.pydata.org/examples/index.html

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.simplefilter('ignore')
plt.rcParams["figure.figsize"] = 10,4

stats = pd.read_csv('D:\\OneDrive - office365hubs.com\\.Python for data science\\Demographic-Data.csv')
stats.columns = ['CountryName','CountryCode','BirthRate','InternetUsers','IncomeGroup']

#%%

vis3 = sns.lmplot(data=stats,x='InternetUsers',y='BirthRate')

#%%
vis3 = sns.lmplot(data=stats,x='InternetUsers',y='BirthRate', fit_reg=False)

#%%--adding color-hue

vis3 = sns.lmplot(data=stats,x='InternetUsers',y='BirthRate', fit_reg=False,
                  hue='IncomeGroup',size=10,aspect=1.5)

#%% Increase the size of markers
#keyword arguments isn python

vis3 = sns.lmplot(data=stats,x='InternetUsers',y='BirthRate', fit_reg=False,
                  hue='IncomeGroup',size=10,aspect=1.5,scatter_kws={'s':200})










