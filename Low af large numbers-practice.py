
#%%
#Low af large numbers-practice
import numpy as np
from numpy.random import rundn
#%%
N = 100
counter = 0
randn(N)

for i in randn(N):
    if (i > -1 and i < 1):
        counter = counter + 1
        answer = counter/N
print(answer)

#%%
N = 1000
counter = 0
randn(N)

for i in randn(N):
    if (i > -1 and i < 1):
        counter = counter + 1
        answer = counter/N
print(answer)
#%%
N = 10000
counter = 0
randn(N)

for i in randn(N):
    if (i > -1 and i < 1):
        counter = counter + 1
        answer = counter/N
print(answer)
#%%
N = 1000000
counter = 0
randn(N)

for i in randn(N):
    if (i > -1 and i < 1):
        counter = counter + 1
        answer = counter/N
print(answer)