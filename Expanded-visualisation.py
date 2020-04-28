# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 07:18:17 2020

@author: Juvette
"""
import numpy as np
import matplotlib.pyplot as plt

#Expanded-visualisation
plt.rcParams['figure.figsize'] = 10,4
plt.plot(Salary[0],c="green",ls='--',marker='s',ms=7,label=Players[0])
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
#%%
plt.rcParams['figure.figsize'] = 10,4
plt.plot(Salary[0],c="green",ls='--',marker='s',ms=7,label=Players[0])
plt.plot(Salary[1],c="red",ls='--',marker='o',ms=7,label=Players[1])
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')

#%%
plt.plot(Salary[0],c="g",ls='--',marker='s',ms=7,label=Players[0])
plt.plot(Salary[1],c="r",ls='--',marker='o',ms=7,label=Players[1])
plt.plot(Salary[2],c="m",ls=':',marker='^',ms=7,label=Players[2])
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
#%%
plt.plot(Salary[0],c="g",ls='--',marker='s',ms=7,label=Players[0])
plt.plot(Salary[1],c="r",ls='--',marker='o',ms=7,label=Players[1])
plt.plot(Salary[2],c="m",ls=':',marker='^',ms=7,label=Players[2])
plt.plot(Salary[3],c='b',ls='--',marker='D',ms=7,label=Players[3])
plt.plot(Salary[4],c='black',ls='--',marker='D',ms=7,label=Players[4])
plt.plot(Salary[5],c='y',ls='--',marker='<',ms=7,label=Players[5])
plt.plot(Salary[6],c="g",ls='--',marker='s',ms=7,label=Players[6])
plt.plot(Salary[7],c="r",ls='--',marker='o',ms=7,label=Players[7])
plt.plot(Salary[8],c="m",ls=':',marker='^',ms=7,label=Players[8])
plt.plot(Salary[9],c='b',ls='--',marker='D',ms=7,label=Players[9])
#adding a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')

#%%
plt.plot(Games[0],c="g",ls='--',marker='s',ms=7,label=Players[0])
plt.plot(Games[1],c="r",ls='--',marker='o',ms=7,label=Players[1])
plt.plot(Games[2],c="m",ls=':',marker='^',ms=7,label=Players[2])
plt.plot(Games[3],c='b',ls='--',marker='D',ms=7,label=Players[3])
plt.plot(Games[4],c='black',ls='--',marker='D',ms=7,label=Players[4])
plt.plot(Games[5],c='y',ls='--',marker='<',ms=7,label=Players[5])
plt.plot(Games[6],c="g",ls='--',marker='s',ms=7,label=Players[6])
plt.plot(Games[7],c="r",ls='--',marker='o',ms=7,label=Players[7])
plt.plot(Games[8],c="m",ls=':',marker='^',ms=7,label=Players[8])
plt.plot(Games[9],c='b',ls='--',marker='D',ms=7,label=Players[9])
#adding a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')

#%%
plt.plot(MinutesPlayed[0],c="g",ls='--',marker='s',ms=7,label=Players[0])
plt.plot(MinutesPlayed[1],c="r",ls='--',marker='o',ms=7,label=Players[1])
plt.plot(MinutesPlayed[2],c="m",ls=':',marker='^',ms=7,label=Players[2])
plt.plot(MinutesPlayed[3],c='b',ls='--',marker='D',ms=7,label=Players[3])
plt.plot(MinutesPlayed[4],c='black',ls='--',marker='D',ms=7,label=Players[4])
plt.plot(MinutesPlayed[5],c='y',ls='--',marker='<',ms=7,label=Players[5])
plt.plot(MinutesPlayed[6],c="g",ls='--',marker='s',ms=7,label=Players[6])
plt.plot(MinutesPlayed[7],c="r",ls='--',marker='o',ms=7,label=Players[7])
plt.plot(MinutesPlayed[8],c="m",ls=':',marker='^',ms=7,label=Players[8])
plt.plot(MinutesPlayed[9],c='b',ls='--',marker='D',ms=7,label=Players[9])
#adding a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')







#
