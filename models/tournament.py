

class Tournament():
    
    def __init__(self, name, place, start_date, end_date, description, number_round=4):
        self.name = name
        self.place = place
        self.start_date  = start_date
        self.end_date = end_date
        self.players = []
        self.description = description
        self.rounds = []
        self.number_round = number_round

    def __repr__(self):
        return f"(Nom: {self.name}, Nombre de tours: {self.number_round})"

    
