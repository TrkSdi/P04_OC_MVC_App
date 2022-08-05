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
        last_name = self.view.display_player()
        first_name = self.view.display_player()
        birth_date = self.view.display_player()
        gender = self.view.display_player()
        rank = self.view.display_player()        
    
        player = Player(last_name, first_name, birth_date, gender, rank)
        return player
    
    def add_players_to_list(self, player):
        return self.players.append(player)
        
        
    
    
    def run(self):
        MAX_NUM_PLAYERS = 2
        self.view.display_tournament()
              
        while len(self.players) < MAX_NUM_PLAYERS:    
            self.view.display_player()
            self.players.append(Player)
            print(self.players)
        
        #def generate_pairs_methode_1():
        # for player in self.players
        
        
        #while round < 4
        
        #def generate_match():
        
        
        #def add_scores():
        
        #def new_ranking
        
        #round -= 1
        
        #def generate_pairs_method_2()
            
        