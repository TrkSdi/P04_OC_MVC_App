from tinydb import TinyDB, Query, where



db_tournament = TinyDB("/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Tournoi.json", indent=4, default=str)
db_players = TinyDB("/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Joueurs.json", indent=4)


tournament_table = db_tournament.table("Tournament")

to_continue_tournament_list = []

i = 0
for tournament in tournament_table:
    if len(tournament["rounds"]) != tournament["number_round"]:
        i += 1
        print(i, "-", tournament["name"])
        to_continue_tournament_list.append(tournament)
    

data = input("Entrez un nombre: ")
        
j = (int(data) - 1)
        
print(to_continue_tournament_list[j])

       