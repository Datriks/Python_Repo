# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:43:34 2020

@author: Juvette
"""

import numpy as np
import pandas as pd
np.random.seed(0)
import seaborn as sns
sns.set(style='white',color_codes=True)

diamond = sns.load_dataset('diamonds')

#%%

print(diamond.head(10))

#%%

flight = sns.load_dataset('flights')

#%%

print(flight.head(10))


#%%

mpgs = sns.load_dataset('mpg')

print(mpgs.head(10))
#%%




