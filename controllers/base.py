from models.players import Player


class Controller:
    
    def __init__(self):
        self.players = []
     
    def add_player(self):    
        while len(self.players) < 8:
                f_name = self.view.prompt_for_player()
                l_name = self.view.prompt_for_player()
                birth_date = self.view.prompt_for_player()
                gender = self.view.prompt_for_player()
                rank = self.view.prompt_for_player()
                
                player = Player(f_name, l_name, birth_date, gender, rank)
                self.players.append(player)
    
    

    
    
    
    
    
    
    def run(self):
        # On rajoute les joueurs
        self.add_player()
        
        # On commence le jeu et définissons les pairs
        self.start_game()
            for player in self.players:
                self.view.create_pairs()
        
        round = 0 
        while round < 4:
            # On entre les résultat
            self.enter_result()

            # On rajoute le score 
            self.add_score()
            
            # On crée des nouvelles pairs
            self.create_pairs_tour2()
            
            round += 1
            
        