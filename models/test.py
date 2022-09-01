import uuid

class Joueur:
    def __init__(self, name, rank, score):
        self.name = name
        self.rank = rank
        self.score = score
        self.id = uuid.uuid4()

    def __str__(self):
        return f"{self.name}, Classement: {self.rank}, Score: {self.score}"

j1 = Joueur("J1", 1, 0)
j2 = Joueur("J2", 2, 0)
j3 = Joueur("J3", 3, 0)
j4 = Joueur("J4", 4, 0)

liste = [j1, j2, j3, j4]
round = []

paires = [(liste[0], liste[1]),(liste[2], liste[3])]

# pour une paire (deux joueurs) dans une liste de paires
#for paire in paires:
#   print(f"{paire[0]} VS {paire[1]}")
#   print(f"{paire[0].id} VS {paire[1].id}")

"""
def test():
    
        if len(round) == 0:
            objet = "Salut"
            print("Test_1")
            round.append(objet)
            
        elif len(round) < 3:
            objet = "Salut"
            print("Test_2")
            round.append(objet)
        else:
            print("Au revoir")
            break
        
        print("Hola")
        print(round)
            
    
test()
"""
'''
def generate_pairs_remains_round(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: (-x.score, x.rank))
        paired_list = []
        already_matched = []
        
        for i in range(len(sorted_list)):
            if sorted_list[i].id in already_matched:
                continue
            else: 
                id1 = sorted_list[i].id
                player1 = sorted_list[i]
                already_matched.append(id1)
                j = i + 1
                for j in range(len(sorted_list)):
                    if sorted_list[j].id in already_matched or (id1, sorted_list[j].id) in self.round.matchs or (sorted_list[j].id, id1) in self.round.matchs:
                        continue
                    else:
                        id2 = sorted_list[j].id
                        player2 = sorted_list[j]
                        already_matched.append(id2)
                        match = (player1, player2)
                        paired_list.append(match)
                        break
        
        return paired_list
'''
