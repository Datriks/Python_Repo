# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 08:33:55 2020

@author: Juvette
"""
#%%
#Chained Statement
import numpy as np
from numpy.random import randn

#Nested-statements
answer = None
x = randn()

if x > 1 :
    answer = "Greater than 1"
elif x >= -1:
    answer = "Between -1 and 1" 
else:
    answer = "Less than -1"
print("This is the answer")
print(x)
print(answer)

