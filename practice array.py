# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:44:05 2020

@author: Juvette
"""
#crdeate an array of rank 2
import numpy as np

my_arr = np.array([[1,2,3,4],[5,6,7,8]])
print(my_arr)
#%%
print(my_arr[1,2])

print(my_arr.ndim)

print(my_arr.shape)

print(my_arr.size)

print(type(my_arr))