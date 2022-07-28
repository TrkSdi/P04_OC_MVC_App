
from players import Players



class Tournament(Players):
    rounds = 4
    tours = 7
    time = 1
    
    
    def __init__(self, name, place, start_date, end_date, description):
        self.name = name
        self.place = place
        self.start_date  = start_date
        self.end_date = end_date
        self.players = []
        self.description = description
        
    
    def __str__(self):
        return (f"Welcome to chess tournament : '{self.name}'")
        
        
    


    
tournoi_1 = Tournament("Le grand tournoi", "Paris", "20/03/2022", "22/03/2022", "Bonne ambiance, beaucoup de spectateurs")
print(tournoi_1)
