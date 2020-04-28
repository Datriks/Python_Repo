# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 07:15:44 2020

@author: Juvette
"""
import numpy as np
l = [23245,27,546,215,1234]
a = np.array(l)
print(l)
print(a)
#%%----------------Slicing the list
print(l[:1])
print(l[1:])
print(l[0:2])
print(l[:3])
print(l[::2])
#%%---------------Slicing the array
print(a)
print(a[2:])
print(a[2:4])
#%%-----------values in b will replace the values in a ----be careful
b = a[2:4]
print(b)
print(b[0])
b[:] = 111
print(b)
print(a)
#%%-------------copy an array------------------
c = a.copy()
print(c)


























