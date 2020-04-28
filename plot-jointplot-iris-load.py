# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:58:11 2020

@author: Juvette
"""
import numpy as np
import pandas as pd
np.random.seed(0)
import seaborn as sns
sns.set(style='white',color_codes=True)

iris = sns.load_dataset('iris')

#%%

k = sns.jointplot(data=iris,x='sepal_width',y='petal_length',
                  kind='kde',space=0,color='g')
#%%

k = (sns.jointplot(data=iris,x='sepal_length',y='sepal_width',
                   color='k').plot_joint(sns.kdeplot,zorder=0,n_levels=6))

#%%

k = sns.jointplot(data=iris,x="petal_length", y="sepal_length",
                   marginal_kws=dict(bins=15, rug=True),
                   annot_kws=dict(stat="r"),
                   s=40, edgecolor="red", linewidth=1)
