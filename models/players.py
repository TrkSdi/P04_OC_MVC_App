import uuid

class Player():
    
    def __init__(self, first_name, last_name, birth_date, gender, rank, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score
        self.id = uuid.uuid4()
        

    

    def __str__(self):
        return f"\nNom: {self.last_name} / {self.id}\nClassement: {self.rank}\nScore: {self.score}"
    