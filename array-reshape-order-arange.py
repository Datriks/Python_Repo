# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:29:45 2020

@author: Juvette
"""
import numpy as np
#%%
mydata = np.arange(0,20)
print(mydata)
mydata1 = np.arange(1,15)
print(mydata1)
mydata2 = np.arange(2,21)
print(mydata2)
#%%-----default is opposite to R
mydata5 = np.reshape(mydata,(5,4))
print(mydata5)

#%%
matr1 = np.reshape(mydata,(5,4),order='C')
print(matr1)

#%%
print(matr1[2,2])
#%%
matr2 = np.reshape(mydata,(5,4),order = 'F')
print(matr2)
print(matr2[0,2])
#%%
#this is object oriented programming

print(mydata.reshape((5,4)))
#%%
r1 = ["I","am","happy"]
r2 = ["What","a","day"]
r3 = [1,2,3]

print([r1,r2,r3])

comb = np.array([r1,r2,r3])
print(comb)

#%%


















