# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:29:30 2020

@author: Juvette
"""
import numpy as np
import pandas as pd
np.random.seed(0)
import seaborn as sns
sns.set(style='white',color_codes=True)


tips = sns.load_dataset('tips')

#%%
print(tips.head())

#%%
g = sns.jointplot(data=tips,x='total_bill',y='tip',color='red')

#%%

g = sns.jointplot(data=tips,x='total_bill',y='tip',color='red',kind='reg')

#%%

g = sns.jointplot(data=tips,x='total_bill',y='tip',color='red',kind='hex')










