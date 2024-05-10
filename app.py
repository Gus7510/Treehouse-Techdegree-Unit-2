# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:56:32 2024

@author: gus_a
"""

from constants import PLAYERS, TEAMS
import copy
from sys import exit

my_players_copy = copy.deepcopy((PLAYERS)) 
my_teams_copy = copy.deepcopy((TEAMS))

cleaned_players = []

def clean_data(my_players_copy):
    
    
    for player in my_players_copy:
        
        
        player["height"] = int(player["height"].split(" ")[0])
        
        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False
            
        cleaned_players.append(player)
        
    #print(cleaned_players)



panthers_players = []
bandits_players = []
warriors_players = []



def balance_teams():
    
    num_players_team = len(my_players_copy) / len(my_teams_copy)
    
    while len(cleaned_players) > 0:
        
        
        for player in cleaned_players:
            if len(panthers_players) < num_players_team:
                panthers_players.append(cleaned_players.pop(0))
            
            if len(bandits_players) < num_players_team:
                bandits_players.append(cleaned_players.pop(0))
            
            if len(warriors_players) < num_players_team:
                warriors_players.append(cleaned_players.pop(0))
            
            
    #print(panthers_players)
    #print(len(panthers_players))
    #print(bandits_players)
    #print(len(bandits_players))
    #print(warriors_players)
    #print(len(warriors_players))


def panthers_data():
    print("\nTeam: Panthers Stats ")
    print("---------------------")
    
    print(f"Total Players: {len(panthers_players)}")
    
    print("Players on Team: \n")
    
    panthers_player_name = []
    
    for player in panthers_players:
        
        panthers_player = player.get("name")
        panthers_player_name.append(panthers_player)
        
        
    panthers_players_names = ", ".join(panthers_player_name)
    print(panthers_players_names)
    
    
def bandits_data():
    print("\nTeam: Bandits Stats ")
    print("---------------------")
    
    print(f"Total Players: {len(bandits_players)}")
    
    print("Players on Team: \n")
    
    bandits_player_name = []
    
    for player in bandits_players:
        
        bandits_player = player.get("name")
        bandits_player_name.append(bandits_player)
        
        
    bandits_players_names = ", ".join(bandits_player_name)
    print(bandits_players_names)
    
    
def warriors_data():
    print("\nTeam: Warriors Stats ")
    print("---------------------")
    
    print(f"Total Players: {len(warriors_players)}")
    
    print("Players on Team: \n")
    
    warriors_player_name = []
    
    for player in warriors_players:
        
        warriors_player = player.get("name")
        warriors_player_name.append(warriors_player)
        
        
    warriors_players_names = ", ".join(warriors_player_name)
    print(warriors_players_names)
    
    
    



def run_program():
    
    while True:
        
        print("""
              BASKETBALL TEAM STATS TOOL

---- MENU----

 Here are your choices:
  A) Display Team Stats
  B) Quit
              """)
        
        try:
            user_response_one = input("Enter an option: (a/b) ")
            
            if user_response_one.lower() == "a":
                print("""
A) Panthers
B) Bandits
C) Warriors
                      """)
                
                user_response_two = input("Enter an option (a/b/c) ")
                
                if user_response_two.lower() == "a":
                    panthers_data()
                    print("Press ENTER to continue")
                    continue
                    
                elif user_response_two.lower() == "b":
                    bandits_data()
                    print("Press ENTER to continue")
                    continue
                    
                elif user_response_two.lower() == "c":
                    warriors_data()
                    print("Press ENTER to continue")
                    continue
                
                else:
                    print(" Please enter only any of the following letters: (a/b/c)")
                    continue
                
                
                
            elif user_response_one.lower() == "b":
                exit(0)
        
        except ValueError:
            print(" Please only enter a or b ")
            continue
    
    
    return
    






if __name__ == "__main__":
    clean_data(my_players_copy)
    balance_teams()
    run_program()
    










"""
Code from websites
https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings

"""


