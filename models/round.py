from pathlib import Path
import json


class Round:
    def __init__(self, name, start_date):
        self.name = name
        self.start_date = start_date
        self.matchs = []

    def __str__(self):
        return f"{self.name} / {self.start_date}"

    @staticmethod
    def rounds_per_tournament(i):
        """_summary_
        Generate list of rounds by tournament

        Args:
            i : _select tournament_
        """
        file = Path("data/Tournoi.json")
        data = open(file)
        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("!! Aucun tournoi dans la base de données !!")
            print("")
        else:
            data = json.load(data)

            file = Path("data/Joueurs.json")
            data_player = open(file)
            isempty = file.stat().st_size == 0
            if isempty:
                print("")
                print("!! Aucun joueur dans la base de données !!")
                print("")
            else:
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
                    new_list.append(element)

                for element in new_list:
                    print(element["name"])
                    print("_" * len(element["name"]))
                    print("")
                    print(element["start_date"])
                    print("")
                    print("matchs:")
                    print("")
                    for match in element["matchs"]:
                        print(match)
                    print("")
