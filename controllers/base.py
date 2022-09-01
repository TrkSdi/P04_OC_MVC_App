
from models.tournament import Tournament
from models.players import Player
from models.round import Round
from datetime import datetime
from tinydb import TinyDB
from pathlib import Path
import sys


class Controller:
    
    DB = TinyDB(Path(__file__).resolve().parent / "players.json", indent=4)
    
    def __init__(self, view):
        self.players = []
        self.tournaments = []
        self.view = view
        
    def launch_program(self):
        while True:
            option = self.view.main_menu()
            if option == "1":
                self.tournament_program()   
            elif option == "2":
                self.players_menu()
            elif option == "3":
                self.report_menu()
            elif option == "0":
                self.quit_program()
            else:
                print("Entrez un choix valide")
        
    def tournament_program(self):
        while True:
            option = self.view.tournament_menu()
            if option == "1":
                self.start_tournament()
            elif option  == "2":
                self.launch_program()
            else:
                print("Entrez un choix valide")
            
    
    def players_menu(self):
        pass
    
    def report_menu(self):
        pass
    
    def quit_program(self):
        return sys.exit()
    
    def start_tournament(self):
        data = self.view.input_tournament()
        self.current_tournament = Tournament(data["tournament_name"], data["place"], data["start_date"], data["end_date"], data["description"], data["number_round"]) 
        print(self.current_tournament)
        self.add_players()
        self.save_players()
        while self.current_tournament.number_round != len(self.current_tournament.rounds):
            self.start_round()
        self.end_message()
        self.launch_program()
            
        
    def start_round(self):
        
        paired_list = []
        if len(self.current_tournament.rounds) == 0:
            # First Round 
            self.round = Round("Round 1", datetime.now())
            print("")
            print(self.round)
            paired_list = self.generate_pairs_round_1()
            
        elif len(self.current_tournament.rounds) < self.current_tournament.number_round:
            self.round = Round(f"Round {len(self.current_tournament.rounds) + 1}", datetime.now())
            print("")
            print(self.round)
            # Pour test / à modifier
            paired_list = self.generate_pairs_remains_round()
        else:
            self.display_score(paired_list)
            
        
        match = ()
        for pair in paired_list:
            match = (pair[0][0], pair[1][0])
            print(f"{pair[0][0]} \nVS \n{pair[1][0]}")
            self.add_score(match)
            self.current_tournament.previous_match.append(match)
        
        
        
        self.round.matchs.append(match)
        self.current_tournament.rounds.append(self.round.matchs)
        
        
        '''
        # remains rounds
        elif len(self.current_tournament.rounds) < self.current_tournament.number_round:
            self.round_match = Round(f"Round {len(self.current_tournament.rounds) + 1}", datetime.now())
            print("")
            print(round_match)
            list_pairs = self.generate_pairs_remains_round() 
        else:
            self.end_message() 
            #self.display_score(list_pairs)
        '''
        '''  
        round_match.matchs = []
        for pair in list_pairs:
            match = (pair[0], pair[1])
            print(f"{pair[0]} \nVS {pair[1]}")   
            self.add_score(match)
            self.round.append(match)
            self.current_tournament.rounds.append(self.matchs)
        '''      
            
    def add_players(self):
        MAX_NUM_PLAYERS = 8
        while len(self.current_tournament.players) < MAX_NUM_PLAYERS:
            data = self.view.input_player()
            player = Player(data["last_name"], data["first_name"], data["birth_date"], data["gender"], data["rank"])
            self.current_tournament.players.append(player)
        #Vérification des données des joueurs
        #for player in self.current_tournament.players:
        #    print(player)
    
    def save_players(self):
        serialized_players = []
        for player in self.current_tournament.players:
            serialized_player = {
                "last_name": player.last_name,
                "first_name":player.first_name,
                "birth_date": player.birth_date,
                "gender": player.gender,
                "rank": player.rank,
                "score": player.score
            }
            serialized_players.append(serialized_player)
        return self.DB.insert_multiple(serialized_players)
        

        
    def generate_pairs_round_1(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: x.rank)
        paired_list = [
                        ([sorted_list[0], sorted_list[0].id], [sorted_list[4], sorted_list[4].id]),
                        ([sorted_list[1], sorted_list[1].id], [sorted_list[5], sorted_list[5].id]),
                        ([sorted_list[2], sorted_list[2].id], [sorted_list[6], sorted_list[6].id]),
                        ([sorted_list[3], sorted_list[3].id], [sorted_list[7], sorted_list[7].id])
                    ]
        return paired_list
    
    
    def generate_pairs_remains_round(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: (-x.score, x.rank))
        paired_list = []
        already_selected = []
        
        
        
        for i in range(len(sorted_list)):
            if [sorted_list[i], sorted_list[i].id] in already_selected:
                continue
            else:
                player_1 = [sorted_list[i], sorted_list[i].id]
                already_selected.append(player_1)
                j = i + 1
                for j in range(len(sorted_list)):
                    if [sorted_list[j], sorted_list[j].id] in already_selected or (player_1, [sorted_list[j], sorted_list[j].id]) in self.current_tournament.previous_match or ([sorted_list[j], sorted_list[j].id], player_1) in self.current_tournament.previous_match:
                        continue
                    else:
                        player_2 = [sorted_list[j], sorted_list[j].id]
                        already_selected.append(player_2)
                        pair = (player_1, player_2)
                        paired_list.append(pair)
                        break
        
        
        return paired_list
            
  
    def add_score(self, match):
        for player in match:
            data = self.view.input_score(player)
            player.score += float(data)
        # Vérification des scores
        #for player in self.current_tournament.players:
        #   print(player)
        
    
    def display_score(self, list_pairs):
        print("")
        print("SCORE FINAL")
        print("===========")
        liste = []
        for pair in list_pairs:
            for player in pair:
                liste.append(player)
        sorted_list = sorted(liste, key=lambda x: (-x.score, x.rank))
        for player in sorted_list:
            print(player)
            
            
    @staticmethod          
    def end_message():
        return print("\n=====================================\nFELICITATIONS, LE TOURNOI EST TERMINE\n=====================================")
                
                

        
        

"""
[
(sorted_list[0], sorted_list[4]),
(sorted_list[1], sorted_list[5]),
(sorted_list[2], sorted_list[6]),
(sorted_list[3], sorted_list[7])
]
"""
"""
[
(sorted_list[0], sorted_list[1]),
(sorted_list[2], sorted_list[3]),
(sorted_list[4], sorted_list[5]),
(sorted_list[6], sorted_list[7])
]

"""