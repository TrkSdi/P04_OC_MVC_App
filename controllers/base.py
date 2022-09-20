
from models.tournament import Tournament
from models.players import Player
from models.round import Round
from datetime import datetime
from tinydb import TinyDB
from pathlib import Path
import sys


class Controller:
    
    db_players = TinyDB(Path(__file__).resolve().parent / "Joueurs.json", indent=4)
    db_tournament = TinyDB(Path(__file__).resolve().parent / "Tournoi.json", indent=4, default=str)
    
    
    
    
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
        while self.current_tournament.number_round != len(self.current_tournament.rounds):
            self.start_round()
        self.save_players()
        self.save_tournament()    
        self.display__final_score()
        self.end_message()
        self.launch_program()
            
        
    def start_round(self):
        
        paired_list = []
        if len(self.current_tournament.rounds) == 0:
            # First round 
            self.current_round = Round("Round 1", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("-----------------------------")
            print(self.current_round)
            print("-----------------------------")
            paired_list = self.generate_pairs_round_1()
            
            
        elif len(self.current_tournament.rounds) < self.current_tournament.number_round:
            # Remains rounds
            self.current_round = Round(f"Round {len(self.current_tournament.rounds) + 1}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("-----------------------------")
            print(self.current_round)
            print("-----------------------------")
            paired_list = self.generate_pairs_remains_round()
        
         
        match = ()
        already_match = ()
        match_score = 0.0
        
        for pair in paired_list:
            match = ([pair[0], match_score], [pair[1], match_score]) # pair[] + score / score a stocker dans match 
            print(f"\nJoueur: {pair[0].last_name}\nVS\nJoueur: {pair[1].last_name}")
            self.add_score(match)
            already_match = (pair[0], pair[1])
            self.current_tournament.previous_match.append(already_match)
            self.current_round.matchs.append(match)
            
        
        self.current_tournament.rounds.append(self.current_round)
        

    def add_players(self):
        MAX_NUM_PLAYERS = 8
        while len(self.current_tournament.players) < MAX_NUM_PLAYERS:
            data = self.view.input_player(self.current_tournament)
            player = Player(data["last_name"], data["first_name"], data["birth_date"], data["gender"], data["rank"])
            self.current_tournament.players.append(player)

    
    def save_tournament(self):
        tournament_table = self.db_tournament.table("Tournament")
        
        serialized_tournament = {
            "name": self.current_tournament.name,
            "place": self.current_tournament.place,
            "start_date": self.current_tournament.start_date,
            "end_date": self.current_tournament.end_date,
            "description": self.current_tournament.description,
            "number_round": self.current_tournament.number_round,
            "rounds" : []  
        }
        
        for round in self.current_tournament.rounds:
            serialized_round = {
                            "name": round.name, 
                            "start_date": round.start_date,
                            "end_date": round.end_date,
                            "matchs": []
                                }
            
            for match in round.matchs:
                serialized_round["matchs"].append(([match[0][0].id, match[0][1]],[match[1][0].id, match[1][1]]))
        
            serialized_tournament["rounds"].append(serialized_round)
        
        tournament_table.insert(serialized_tournament)
        
    def save_players(self):
        serialized_players = []
        for player in self.current_tournament.players:
            serialized_player = {
                "last_name": player.last_name,
                "first_name":player.first_name,
                "birth_date": player.birth_date,
                "gender": player.gender,
                "rank": player.rank,
                "score": player.score,
                "id" : str(player.id)
            }
            serialized_players.append(serialized_player)
        self.db_players.insert_multiple(serialized_players)
        
        
    def generate_pairs_round_1(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: x.rank)
        paired_list = [
                        (sorted_list[0], sorted_list[4]),
                        (sorted_list[1], sorted_list[5]),
                        (sorted_list[2], sorted_list[6]),
                        (sorted_list[3], sorted_list[7]),
                        
                    ]
        return paired_list
    
    def generate_pairs_remains_round(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: (-x.score, x.rank))
        paired_list = []
        already_selected = []
        
        for players in sorted_list:
            print(players)
        
        for i in range(len(sorted_list)):
            if sorted_list[i].id in already_selected:
                continue
            else:
                player_1 = sorted_list[i]
                already_selected.append(player_1.id)
                j = i + 1
                for j in range(len(sorted_list)):
                    if sorted_list[j].id in already_selected or (player_1, sorted_list[j]) in self.current_tournament.previous_match or (sorted_list[j], player_1) in self.current_tournament.previous_match:
                        continue
                    else:
                        player_2 = sorted_list[j]
                        already_selected.append(player_2.id)
                        pair = (player_1, player_2)
                        paired_list.append(pair)
                        break
            
        return paired_list
            
    def add_score(self, match):
            for element in match:
                data = self.view.input_score(element[0])
                element[0].score += float(data) 
                element[1] += float(data)
    
    def display__final_score(self):
        print("")
        print("SCORE FINAL")
        print("===========")
        player_list = []
        for player in self.current_tournament.players:
            player_list.append(player)
        sorted_list = sorted(player_list, key=lambda x: (-x.score, x.rank))
        for player in sorted_list:
            print(player)
            
            
    @staticmethod          
    def end_message():
        return print("\n=====================================\nFELICITATIONS, LE TOURNOI EST TERMINE\n=====================================")
                
