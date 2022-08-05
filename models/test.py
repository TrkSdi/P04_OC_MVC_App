"""    
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
            
            # On crée des nouvelles pairs / Méthode solid / Créer class pairs
            self.create_pairs_tour2() 
            
            round += 1
            
    """   