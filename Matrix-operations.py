# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 07:44:47 2020

@author: Juvette
"""
#Matrix-operations
print(Salary)
#how er get teh info on a specific player
#Salary[][]
print(Pdict["LeBronJames"])
print(Sdict["2009"])

print(Salary[Pdict["LeBronJames"]][Sdict["2009"]])

#%%
import warnings
warnings.simplefilter('ignore')

print(FieldGoals)
print(Games)
#Dividing operation
print(FieldGoals/Games)
#%% ----rounding
print(np.matrix.round(FieldGoals/Games))

#%%
FieldGoalsPerGame = np.matrix.round(FieldGoals/Games)
print(FieldGoalsPerGame)

#%%---using dictionaries to find a specific value
print(FieldGoalsPerGame[Pdict["LeBronJames"]][Sdict["2009"]])
print(FieldGoalsPerGame[Pdict['DerrickRose']][Sdict["2009"]])

#%%
print(np.matrix.round(MinutesPlayed/Games))

#%%
print(np.matrix.round(FieldGoals / FieldGoalAttempts))
FGAC =  np.matrix.round(FieldGoals/FieldGoalAttempts)
print(FGAC[Pdict['LeBronJames']][Sdict['2009']])























