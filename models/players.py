import uuid

class Player():
    
    
    
    def __init__(self, first_name, last_name, birth_date, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = 0.0
        self.id = uuid.uuid4()
        
        
    def __str__(self):
        return f"\nNom: {self.last_name}\nClassement: {self.rank}\nScore: {self.score}"
    
