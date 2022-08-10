

class Player():
    
    score = 0
    
    def __init__(self, first_name, last_name, birth_date, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank

    

    def __repr__(self):
        return f"({self.last_name}, {self.rank})"
    