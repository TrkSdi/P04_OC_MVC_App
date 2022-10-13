from pathlib import Path
import json


def players_per_tournament_rank(i):
    file = Path("/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Joueurs.json")
    data_players = open(file)
    isempty = file.stat().st_size == 0
    if isempty:
        print("")
        print("le fichier est vide")
        print("")
    else:
        file = Path("/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Tournoi.json")
        data_tournament = open(file)
        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("le fichier est vide")
            print("")
        else:
            data_tournament = json.load(data_tournament)
            list_tournament = []
            for key in data_tournament:
                for value in data_tournament[key]:
                    list_tournament.append(data_tournament[key][value])

            data_players = json.load(data_players)
            list_players = []
            for key in data_players:
                for value in data_players[key]:
                    list_players.append(data_players[key][value])

            new_list = []
            j = i - 1
            print("")
            print(list_tournament[j]["name"])
            print("-" * len(list_tournament[j]["name"]))
            print("Liste des joueurs: (triés par ordre alpha-numérique) ")
            print("")
            for player in list_tournament[j]["players"]:
                for sub in list_players:
                    if player["id"] in sub["id"]:
                        new_player = {'last_name': sub["last_name"], 'first_name': sub["first_name"], 'birth_date': sub["birth_date"], 'gender': sub["gender"], 'rank': sub["rank"]}
                        new_list.append(new_player)
            sorted_list_alpha = sorted(new_list, key=lambda d: int(d['rank']))
            for player in sorted_list_alpha:
                print("Nom:               ", player["last_name"])
                print("Prénom:            ", player["first_name"])
                print("Date de naissance: ", player["birth_date"])
                print("Genre:             ", player["gender"])
                print("Classement:        ", player["rank"])
                print("-" * 30)
