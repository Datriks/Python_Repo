# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:00:02 2020

@author: Juvette
"""
#function-advanced-creation-advanced function design
def myplot(playerlist):
    Col = {"KobeBryant":'black',"JoeJohnson":'red',"LeBronJames":'green',"CarmeloAnthony":'blue',"DwightHoward":'magenta',"ChrisBosh":'black',"ChrisPaul":'red',"KevinDurant":'green',"DerrickRose":'blue',"DwayneWade":'magenta'}
    Mark = {"KobeBryant":'s',"JoeJohnson":'o',"LeBronJames":'v',"CarmeloAnthony":'^',"DwightHoward":'D',"ChrisBosh":'<',"ChrisPaul":'>',"KevinDurant":'p',"DerrickRose":'*',"DwayneWade":'h'}
    for name in playerlist:
        plt.plot(Games[Pdict[name]],c=Col[name],ls='--',marker=Mark[name],ms=7,label=name)
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
  
myplot(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward",
        "ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])

#%%
#fix up the inputs
def myplot(data,playerlist):
    Col = {"KobeBryant":'black',"JoeJohnson":'red',"LeBronJames":'green',"CarmeloAnthony":'blue',"DwightHoward":'magenta',"ChrisBosh":'black',"ChrisPaul":'red',"KevinDurant":'green',"DerrickRose":'blue',"DwayneWade":'magenta'}
    Mark = {"KobeBryant":'s',"JoeJohnson":'o',"LeBronJames":'v',"CarmeloAnthony":'^',"DwightHoward":'D',"ChrisBosh":'<',"ChrisPaul":'>',"KevinDurant":'p',"DerrickRose":'*',"DwayneWade":'h'}
    for name in playerlist:
        plt.plot(data[Pdict[name]],c=Col[name],ls='--',marker=Mark[name],ms=7,label=name)
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
  
myplot(Salary,["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward",
        "ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
#Salary,Games,MinutesPlayed,FieldGoals,FieldGoalAttempts

#%%
print(Players)


#%%
#fix up the inputs
def myplot(data,playerlist = Players):
    Col = {"KobeBryant":'black',"JoeJohnson":'red',"LeBronJames":'green',"CarmeloAnthony":'blue',"DwightHoward":'magenta',"ChrisBosh":'black',"ChrisPaul":'red',"KevinDurant":'green',"DerrickRose":'blue',"DwayneWade":'magenta'}
    Mark = {"KobeBryant":'s',"JoeJohnson":'o',"LeBronJames":'v',"CarmeloAnthony":'^',"DwightHoward":'D',"ChrisBosh":'<',"ChrisPaul":'>',"KevinDurant":'p',"DerrickRose":'*',"DwayneWade":'h'}
    for name in playerlist:
        plt.plot(data[Pdict[name]],c=Col[name],ls='--',marker=Mark[name],ms=7,label=name)
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
  
myplot(Salary)
