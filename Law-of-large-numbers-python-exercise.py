# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 08:50:15 2020

@author: Juvette
"""
#%%
#randn,if,logical operators,loop
import numpy as np
from numpy.random import randn
N = 100
counter = 0
for i in randn(N):
    if (i >-1 and i < 1):
        counter = counter +1
answer = counter/N
print(answer)
    
    


