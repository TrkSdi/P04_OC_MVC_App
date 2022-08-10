from models.tournament import Tournament
from models.players import Player


class Controller:
    def __init__(self, view):
        self.players = []
        self.view = view
        
    
    def start_tournament(self):
        tournament_name = self.view.display_tournament()
        place = self.view.display_tournament()
        start_date = self.view.display_tournament()
        end_date = self.view.display_tournament()
        description = self.view.display_tournament()
        
        tournament = Tournament(tournament_name, place, start_date, end_date, description)
        return tournament
        
    def add_players(self):
        MAX_NUM_PLAYERS = 8
        while len(self.players) < MAX_NUM_PLAYERS:
            data = self.view.input_player()
            player = Player(data["last_name"], data["first_name"], data["birth_date"], data["gender"], data["rank"])
            self.players.append(player)
        
    def generate_pairs_1(self):
        sorted_list = sorted(self.players, key=lambda x: x.rank)
        pairs = [
            (sorted_list[0], sorted_list[4]),
            (sorted_list[1], sorted_list[5]),
            (sorted_list[2], sorted_list[6]),
            (sorted_list[3], sorted_list[7])
        ]
        
        return print(pairs)
    
    
    def run(self):
        
        
        #self.view.display_tournament()
           
        
        self.add_players()
        self.generate_pairs_1()
            
        
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
            
        