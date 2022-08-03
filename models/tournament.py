from models.players import Players

class Tournament(Players):
    rounds = 4
    time = 1
    
    def __init__(self, name, place, description, start_date, end_date=None):
        self.name = name
        self.place = place
        self.start_date  = start_date
        self.end_date = end_date
        self.players = []
        self.description = description

    
    def create_tournament(self):
        pass    # Instanciation directe ? 
    
    @staticmethod
    def add_players():
        pass
    
    @staticmethod
    def generate_pairs_1(players):
        pass
   
    @staticmethod
    def generate_pairs_2(players):
        pass
    
    @classmethod
    def add_result(cls):
        pass
    
    @staticmethod
    def save_result():
        pass
    
tournament_1 = Tournament("Le grand tournoi", "Paris", "Bonne ambiance", "22/10/2022")
