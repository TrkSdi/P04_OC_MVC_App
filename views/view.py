

class View:
    
    def display_tournament(self):
        print("Bienvenue dans le tournoi d'échecs")
        tournament_name = input("Entrez le nom du tournoi: ")
        place = input("Indiquez le lieu: ")
        start_date = input("Indiquez la date de début: ")
        end_date = input("Indiquez la date de fin: ")
        description = input("Entrez une description: ")
        return tournament_name, place, start_date, end_date, description
    
    
    def input_player(self):
        last_name = input("Entrez le prénom du joueur: ")
        first_name = input("Entrez le nom du joueur: ")
        birth_date = input("Entrez la date de naissance du jouer: ")
        gender = input("Entrez le sexe du joueur: ")
        rank = input("Entrez son classement: ")
        return {
            "Last Name": last_name,
            "First Name": first_name,
            "Birth Date": birth_date,
            "Gender": gender,
            "Rank": rank
        }