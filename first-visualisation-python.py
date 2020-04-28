# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:23:13 2020

@author: Juvette
"""
# Visualisations

import numpy as np
import matplotlib.pyplot as plt

plt.plot(Salary[0])

print(Salary[0])

#%%
plt.plot(Salary[0],c='Black')
plt.plot(Salary[1],c='Red')
plt.plot(Salary[2],c='yellow',ls='--')

#%%----Styling----
#Chanhing the chart-size
plt.rcParams['figure.figsize'] = 10,4
#creating visualisations
plt.plot(Salary[0],c='Black')
plt.plot(Salary[1],c='Red')
#%%
plt.plot(Salary[2],c='yellow',ls='--',marker='s',ms=7)
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')

#%%
plt.plot(Salary[0],c='yellow',ls='--',marker='s',ms=7,label=Players[0])
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')

#%%
plt.plot(Salary[1],c='green',ls='--',marker='s',ms=7,label=Players[1])
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')

#%%
plt.plot(Salary[0],c='yellow',ls='--',marker='s',ms=7,label=Players[0])
plt.plot(Salary[1],c='green',ls='--',marker='s',ms=7,label=Players[1])
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')










