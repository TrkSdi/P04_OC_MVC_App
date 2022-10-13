from pathlib import Path
import json


def players_list_alpha():
    file = Path("/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Joueurs.json")
    data = open(file)
    isempty = file.stat().st_size == 0
    if isempty:
        print("")
        print("le fichier est vide")
        print("")
    else:
        data = json.load(data)
        list_players = []

        for key in data:
            for value in data[key]:
                list_players.append(data[key][value])

            sorted_list_alpha = sorted(list_players, key=lambda d: d['last_name'])
            print("")
            print("Liste de tous les acteurs:")
            print("-" * len("Liste de tous les acteurs:"))
            print("")
            for dictionnary in sorted_list_alpha:
                print("Nom:               ", dictionnary["last_name"])
                print("Prénom:            ", dictionnary["first_name"])
                print("Date de naissance: ", dictionnary["birth_date"])
                print("Genre:             ", dictionnary["gender"])
                print("Classement:        ", dictionnary["rank"])
                print("-" * 30)


def players_list_rank():
    file = Path("/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Joueurs.json")
    data = open(file)

    isempty = file.stat().st_size == 0
    if isempty:
        print("")
        print("le fichier est vide")
        print("")
    else:
        data = json.load(data)
        list_players = []

        for key in data:
            for value in data[key]:
                list_players.append(data[key][value])

        sorted_list_rank = sorted(list_players, key=lambda d: int(d['rank']))
        print("")
        print("Liste de tous les acteurs:")
        print("-" * len("Liste de tous les acteurs:"))
        print("")
        for dictionnary in sorted_list_rank:
            print("Nom:               ", dictionnary["last_name"])
            print("Prénom:            ", dictionnary["first_name"])
            print("Date de naissance: ", dictionnary["birth_date"])
            print("Genre:             ", dictionnary["gender"])
            print("Classement:        ", dictionnary["rank"])
            print("-" * 30)
