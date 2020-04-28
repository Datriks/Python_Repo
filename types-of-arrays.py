# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:56:19 2020

@author: Juvette
"""
#types of arrays
import numpy as np

a = np.ones((3,2))
print(a)

#%%
b = np.zeros((3,4))
print(b)

#%%
c = np.random.random(3)
print(c)

#%%
d = np.full((2,2),12)
print(d)
#%%
e = np.full((4,4),11)
print(e)

f = e.copy()
print(f)