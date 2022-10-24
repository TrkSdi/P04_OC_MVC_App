from pathlib import Path
import uuid
import json


class Tournament():

    def __init__(self, name, place, start_date, end_date, description, number_round=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_round = number_round
        self.players = []
        self.rounds = []
        self.previous_match = []
        self.rank_list = []
        self.paired_list = []
        self.id = uuid.uuid4()

    def __str__(self):
        return f"""\nNom du tournoi: {self.name}
                    \nNombre de rounds: {self.number_round}
                    \nDescription: {self.description}\n"""

    @staticmethod
    def list_tournament():
        file = Path("data/Tournoi.json")
        data = open(file)
        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("le fichier est vide")
            print("")
        else:
            data = json.load(data)
            list_all_tournament = []
            list_per_tournament = []

            for key in data:
                for value in data[key]:
                    list_all_tournament.append(data[key][value])

            i = 0
            for dictionnary in list_all_tournament:
                i += 1
                tournament = str(i) + " - " + dictionnary["name"]
                list_per_tournament.append(tournament)

            print("")
            print("Liste des tournois: ")
            print("-" * len("Liste des tournois:"))
            print("")
            for tournament in list_per_tournament:
                print(tournament)
            print("")

    @staticmethod
    def matchs_per_tournament(i):
        file = Path("data/Tournoi.json")
        data = open(file)
        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("le fichier est vide")
            print("")
        else:
            data = json.load(data)

            file = "data/Joueurs.json"
            data_player = open(file)
            data_player = json.load(data_player)

            list_players = []
            list_tournament = []
            new_list = []

            for key in data:
                for value in data[key]:
                    list_tournament.append(data[key][value])

            for key in data_player:
                for value in data_player[key]:
                    player = [data_player[key][value]["last_name"], data_player[key][value]["id"]]
                    list_players.append(player)

            j = i - 1
            print("")
            print(list_tournament[j]["name"])
            print("-" * len(list_tournament[j]["name"]))
            print(list_tournament[j]["start_date"])
            print("-" * len(list_tournament[j]["name"]))
            print("")
            for element in list_tournament[j]["rounds"]:
                for match in element["matchs"]:
                    for sub in list_players:
                        if match[0][0] in sub[1]:
                            match[0][0] = sub[0]
                        elif match[1][0] in sub[1]:
                            match[1][0] = sub[0]
                    new_match = [[match[0][0], match[0][1]], [match[1][0], match[1][1]]]
                    new_list.append(new_match)
            print("Liste des matchs:")
            print("-" * len("Liste des matchs:"))
            print("")

            for match in new_list:
                print(match)
            print("")
