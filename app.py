# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:56:32 2024

@author: gus_a
"""

from constants import PLAYERS, TEAMS
import copy


my_players_copy = copy.deepcopy((PLAYERS)) 
my_teams_copy = copy.deepcopy((TEAMS))

cleaned_players = []

def clean_data(my_players_copy):
    
    
    for player in PLAYERS:
        
        fixed= {}
        
        fixed["height"] = int(player["height"].split(" ")[0])
        
        
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
            
        cleaned_players.append(fixed)
    


all_players_list = []




def balance_teams():
    
    num_players_team = len(my_players_copy) / len(my_teams_copy)
    
    
    players_list = []
    
    for player in range(0,num_players_team):
        players_list.append(.pop(0))
    
    
    return


def run_program():
    
    return






if __name__ == "__main__":
    clean_data()
    balance_teams()
    run_program()
    



"""
Balance Teams Function
Now that the player data has been cleaned, create a balance_teams function to
 balance the players across the three teams: Panthers, Bandits, and Warriors.
 Make sure the teams have the same number of total players on them when your 
 team balancing function has finished.

"""





