from pathlib import Path
import json
import uuid


class Player():
    def __init__(self, first_name, last_name, birth_date, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = 0.0
        self.id = uuid.uuid4()

    def __str__(self):
        return str(self.id)

    @staticmethod
    def players_list_alpha():
        """_summary_
        Generate list of players sorted alphanumerically
        """
        file = Path("data/Joueurs.json")
        data = open(file)
        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("!! Aucun joueur dans la base de données !!")
            print("")
        else:
            data = json.load(data)
            list_players = []

            for key in data:
                for value in data[key]:
                    list_players.append(data[key][value])

                sorted_list_alpha = sorted(list_players, key=lambda d: d['last_name'])
                print("")
                print("Liste de tous les joueurs:")
                print("-" * len("Liste de tous les joueurs:"))
                print("")
                for dictionnary in sorted_list_alpha:
                    print("Nom:               ", dictionnary["last_name"])
                    print("Prénom:            ", dictionnary["first_name"])
                    print("Date de naissance: ", dictionnary["birth_date"])
                    print("Genre:             ", dictionnary["gender"])
                    print("Classement:        ", dictionnary["rank"])
                    print("-" * 30)

    @staticmethod
    def players_list_rank():
        """_summary_
        Generate list of players sorted by rank
        """
        file = Path("data/Joueurs.json")
        data = open(file)

        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("!! Aucun joueur dans la base de données !!")
            print("")
        else:
            data = json.load(data)
            list_players = []

            for key in data:
                for value in data[key]:
                    list_players.append(data[key][value])

            sorted_list_rank = sorted(list_players, key=lambda d: int(d['rank']))
            print("")
            print("Liste de tous les joueurs:")
            print("-" * len("Liste de tous les joueurs:"))
            print("")
            for dictionnary in sorted_list_rank:
                print("Nom:               ", dictionnary["last_name"])
                print("Prénom:            ", dictionnary["first_name"])
                print("Date de naissance: ", dictionnary["birth_date"])
                print("Genre:             ", dictionnary["gender"])
                print("Classement:        ", dictionnary["rank"])
                print("-" * 30)

    @staticmethod
    def players_per_tournament_alpha(i):
        """_summary_
        Generate list of players sorted alphanumerically by tournament

        Args:
            i : _select tournament_
        """
        file = Path("data/Joueurs.json")
        data_players = open(file)
        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("!! Aucun joueur dans la base de données !!")
            print("")
        else:
            file = Path("data/Tournoi.json")
            data_tournament = open(file)
            isempty = file.stat().st_size == 0
            if isempty:
                print("")
                print("!! Aucun tournoi dans la base de données !!")
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
                            new_player = {'last_name': sub["last_name"],
                                          'first_name': sub["first_name"],
                                          'birth_date': sub["birth_date"],
                                          'gender': sub["gender"],
                                          'rank': sub["rank"]}
                            new_list.append(new_player)
                sorted_list_alpha = sorted(new_list, key=lambda d: d['last_name'])
                for player in sorted_list_alpha:
                    print("Nom:               ", player["last_name"])
                    print("Prénom:            ", player["first_name"])
                    print("Date de naissance: ", player["birth_date"])
                    print("Genre:             ", player["gender"])
                    print("Classement:        ", player["rank"])
                    print("-" * 30)

    @staticmethod
    def players_per_tournament_rank(i):
        """_summary_
        Generate list of players sorted by rank and by tournament

        Args:
            i : _select tournament_
        """
        file = Path("data/Joueurs.json")
        data_players = open(file)
        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("!! Aucun joueur dans la base de données !!")
            print("")
        else:
            file = Path("data/Tournoi.json")
            data_tournament = open(file)
            isempty = file.stat().st_size == 0
            if isempty:
                print("")
                print("!! Aucun tournoi dans la base de données !!")
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
                            new_player = {'last_name': sub["last_name"],
                                          'first_name': sub["first_name"],
                                          'birth_date': sub["birth_date"],
                                          'gender': sub["gender"],
                                          'rank': sub["rank"]}
                            new_list.append(new_player)
                sorted_list_alpha = sorted(new_list, key=lambda d: int(d['rank']))
                for player in sorted_list_alpha:
                    print("Nom:               ", player["last_name"])
                    print("Prénom:            ", player["first_name"])
                    print("Date de naissance: ", player["birth_date"])
                    print("Genre:             ", player["gender"])
                    print("Classement:        ", player["rank"])
                    print("-" * 30)
