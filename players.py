

class Players():
    
    
    score = 0
    
    def __init__(self, f_name, l_name, birth_date, gender, rank=0):
        self.f_name = f_name
        self.l_name = l_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        
    def get_f_name(self):
        return self.f_name
    
   
    
    
    
    def add_score(self):
        pass
    
    def __str__(self):
        return f"{self.f_name} {self.l_name} \n{self.birth_date} - {self.gender} \nRank = {self.rank}"
    
    
    

p1 = Players("Tarik", "Sadkhi", "19/05/1983", "Male")
p2 = Players("Fanny", "Pezet", "19/12/1994", "Female")
