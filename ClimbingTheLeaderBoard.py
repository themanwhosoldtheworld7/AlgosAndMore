# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:38:06 2020

@author: win10
"""

def CreateLeaderBoard(Scores):
    # Write your code here
    LeaderBoard = dict()    
    i = 1        
    for S in Scores:
        LeaderBoard[S]=i
        i+=1           
    return LeaderBoard 
    
def UniqueList(SortedList):
    UniqueList =[]
    E = None
    for element in SortedList:
        if element == E:
            continue
        else:
            UniqueList.append(element)
            E = element
    return UniqueList
    

def climbingLeaderboard(ranked, player):
    
    P_Ranks = []
    ranked_U = UniqueList(ranked)
    player_U = UniqueList(player)
    player_U.sort(reverse = True)
    LeaderBoard = CreateLeaderBoard(ranked_U)
    PlayerAdj = CreateLeaderBoard(player_U)
    
    NewRanks = ranked_U + player_U
    NewRanks.sort(reverse = True)
    NewRanks_U = UniqueList(NewRanks)
    New_LeaderBoard = CreateLeaderBoard(NewRanks_U)
    
    i = 0
    for Score in PlayerAdj:
        #Check if exists in leaderboard
        try:
            LeaderBoard[Score]
            PlayerAdj[Score] = i
        except:
            LeaderBoard[Score] = '-999'
            PlayerAdj[Score] = i
            i+=1
    
    for Score in player:
        R = New_LeaderBoard[Score] - PlayerAdj[Score]
        P_Ranks.append(R)  
    
    return P_Ranks





   
ranked = [100,50,40,25,20,10]
player = [5,5,5,5,5,25,50,50,50,120]
Climb  = climbingLeaderboard(ranked, player)
print(Climb)



