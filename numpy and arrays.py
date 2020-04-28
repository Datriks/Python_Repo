# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:04:34 2020

@author: Juvette
"""
l = [23245,27,546,215,-1234]
print(l)
l.pop()
print(l)
#%%
import numpy as np
a = np.array(l)
print(a)

#%%

print(a.mean())
#%%
m = (23245+27+546+215)/4
print(l)
b = np.array(l)
print(b)
#%%
print(b.mean())
print(m)
#%%
print(b.mean(),b.max(),b.min())


