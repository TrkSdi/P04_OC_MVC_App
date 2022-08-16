from models.tournament import Tournament
from models.players import Player
from models.round import Round
from datetime import datetime
import sys


class Controller:
    def __init__(self, view):
        self.players = []
        self.tournaments = []
        self.view = view
        
    def launch_program(self):
        while True:
            option = self.view.main_menu()
            if option == str(1):
                self.tournament_program()   
            elif option == str(2):
                self.players_menu()
            elif option == str(3):
                self.report_menu()
            elif option == str(0):
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
        while self.current_tournament.number_round == len(self.current_tournament.rounds):
            self.start_round()
            
        
    def start_round(self):
        if len(self.current_tournament.rounds) == 0:
            # c'est le premier round
            round = Round("Round 1", datetime.now())
            matchs = self.generate_pairs_round_1()
            for match in matchs:
                print(match)
            self.current_tournament.rounds.append(round)
        else:
            # Autres rounds
            
            pass
            
        
    def add_players(self):
        MAX_NUM_PLAYERS = 8
        while len(self.current_tournament.players) < MAX_NUM_PLAYERS:
            data = self.view.input_player()
            player = Player(data["last_name"], data["first_name"], data["birth_date"], data["gender"], data["rank"])
            self.current_tournament.players.append(player)
        print(self.current_tournament.players)
        
        
    def generate_pairs_round_1(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: x.rank)
        paired_list = [(sorted_list[0], sorted_list[4]),
                       (sorted_list[1], sorted_list[5]),
                       (sorted_list[2], sorted_list[6]),
                       (sorted_list[3], sorted_list[7])]
        return paired_list
    
    
    def run(self):
           
        self.launch_program()
        
        
    
        
        #while round < 4
        # def generate pairs
        # assigner des id à chaque joueurs 
        # trier en fonction de l'id 
        #for player in self.players:
        #   print(player)
        
        
        
        
        #def generate_match():
        
        
        #def add_scores():
        
        #def new_ranking
        
        #round -= 1
        
        #def generate_pairs_method_2()
            
        