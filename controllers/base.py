from models.tournament import Tournament
from models.players import Player


class Controller:
    def __init__(self, view):
        self.players = []
        self.tournaments = []
        self.view = view
        
    def launch_program(self):
        while True:
            option = self.view.main_menu()
            if option == str(1):
                self.tournament_menu()   
            elif option == str(2):
                self.players_menu()
            elif option == str(3):
                self.report_menu()
            elif option == str(0):
                self.quit_program()
            else:
                print("Entrez un choix valide")
        
    def tournament_menu(self):
        while True:
            option = self.view.tournament_menu()
            if option == str(1):
                self.start_tournament()
            elif option  == str(2):
                self.launch_program()
            else:
                print("Entrez un choix valide")
            
    
    def players_menu(self):
        pass
    
    def report_menu(self):
        pass
    
    def quit_program(self):
        pass
    
    def start_tournament(self):
        tournament_name = self.view.input_tournament()
        place = self.view.input_tournament()
        start_date = self.view.input_tournament()
        end_date = self.view.input_tournament()
        description = self.view.input_tournament()
        tournament = Tournament(tournament_name, place, start_date, end_date, description)
        self.tournaments.append(tournament)
        self.add_players()
        
    def add_players(self):
        MAX_NUM_PLAYERS = 8
        while len(self.players) < MAX_NUM_PLAYERS:
            data = self.view.input_player()
            player = Player(data["last_name"], data["first_name"], data["birth_date"], data["gender"], data["rank"])
            self.players.append(player)
        
    def generate_pairs_1(self):
        sorted_list = sorted(self.players, key=lambda x: x.rank)
        players_id = {
            "Player_01": sorted_list[0],
            "Player_02": sorted_list[1],
            "Player_03": sorted_list[2],
            "Player_04": sorted_list[3],
            "Player_05": sorted_list[4],
            "Player_06": sorted_list[5],
            "Player_07": sorted_list[6],
            "Player_08": sorted_list[7],
        }
        pairs_list = [
            ("Player_01", "Player_05"),
            ("Player_02", "Player_06"),
            ("Player_03", "Player_07"),
            ("Player_04", "Player_08")
        ]
        return pairs_list
    
    
    def run(self):
           
        self.launch_program()
        
    
        
        #self.generate_pairs_1()
            
        
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
            
        