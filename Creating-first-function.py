# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:11:28 2020

@author: Juvette
"""
#Creating the first function
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

#%%
#define the function with the name myplot
def myplot(playerlist):
    for name in playerlist:
        plt.plot(Games[Pdict[name]],c="g",ls='--',marker='s',ms=7,label=name)
    plt.legend(loc='upper left', bbox_to_anchor=(0,0))
    plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
  
myplot(['KobeBryant','LeBronJames','DerrickRose'])

#%%
def myplot1(playerlist1):
    for name in playerlist1:
        plt.plot(Salary[Pdict[name]],c='r',ls='--',marker='o',ms=7,label=name)
    
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)),Seasons,rotation='vertical')

myplot1(['KobeBryant','LeBronJames','DerrickRose'])   
    
    
    
    
    
    
    
    
    
    
    
    
    
    

