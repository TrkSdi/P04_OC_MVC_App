

class Player():
    
    def __init__(self, first_name, last_name, birth_date, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = 0

    

    def __repr__(self):
        return f"(Nom: {self.last_name}, Classement: {self.rank}, Score: {self.score})"
    