
from curses.ascii import isdigit
from models.players import Player





class View:
    
    def main_menu(self):
        print("")
        print("Bienvenue au tournoi d'échecs")
        print("")
        print("1 - Tournois")
        print("2 - Joueurs")
        print("3 - Rapports")
        print("0 - Quitter")
        print("")
        return input("Faites votre choix: ")
    
    def tournament_menu(self):
        print("")
        print("1 - Commencer un nouveau tournoi")
        print("2 - Menu principal")
        print("")
        return input("Faites votre choix: ")
    
    def input_tournament(self):
        print("")
        tournament_name = input("Entrez le nom du tournoi: ")
        place = input("Indiquez le lieu: ")
        start_date = input("Indiquez la date de début: ")
        end_date = input("Indiquez la date de fin (appuyez sur entrée si même date): ")
        if end_date == "":
            start_date = end_date
        description = input("Entrez une description: ")
        number_round = input("Entre le nombre de tours, sinon 4 par défaut: ")
        if number_round == "":
            number_round = 4
        else:
            number_round = int(number_round)
        return {
            "tournament_name": tournament_name,
            "place": place,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "number_round": number_round       
        }
    
    
    def input_player(self, current_tournament):
        
        last_name = input("Entrez le nom du joueur: ")
        while last_name == "":
            print("Le nom du joueur est obligatoire")
            last_name = input("Entrez le nom du joueur: ")
        first_name = input("Entrez le prénom du joueur: ")
        birth_date = input("Entrez la date de naissance du joueur: ")
        gender = input("Entrez le sexe du joueur: ")
        while True:  
            rank = input("Entrez son classement: ")
            if not rank.isdigit():
                print("Veuillez entrez un choix valide")
                continue
            elif rank == "":
                print("Veuillez entrez un choix valide")
                continue
            elif rank in current_tournament.rank_list:
                print("Classement déjà assigné")
                continue   
            else:
                current_tournament.rank_list.append(rank)
                break
       
        
        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "gender": gender,
            "rank": rank
        }
        
        
    def input_score(self, player):
        print("")
        valid_score = ["1", "0.5", "0"]
        while True:
            already_score = []
            score = input(f"Entrez le score du joueur {player.last_name}: ")
            if score == "":
                print("L'ajout du score est nécessaire")
            elif not score.replace('.','',1).isdigit():
                print("Le format saisi n'est pas valide")
            elif not score in valid_score:
                print("Le score n'est pas valide") 
                if score == "0.5":
                    continue
                elif score == "1" or score == "0":
                    already_score.append(score)
            elif score in already_score:
                print("Le score est déjà utilisé")
            else:
                break
        return score
    
    def input_rank(self, player):
        print("")
        rank = input(f"Entrez le classement du joueur {player.last_name}: ")
        return rank

    def input_report(self):
        print("")
        print("1 - Liste des joueurs")
        print("2 - Liste des tournois")
        