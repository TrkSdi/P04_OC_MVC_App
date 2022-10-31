from models.tournament import Tournament
from models.players import Player
from models.round import Round
from datetime import datetime
from tinydb import TinyDB, Query
from pathlib import Path
from models.constant import (OP_CHANGE_RANK, OP_CONTINUE_TOURNAMENT, OP_LAUNCH_MENU, OP_LIST_MATCH_PER_TOURNAMENT,
                             OP_LIST_PLAYER_PER_TOURNALENT_ALPHA, OP_LIST_PLAYER_PER_TOURNALENT_RANK,
                             OP_LIST_PLAYERS_ALPHA, OP_LIST_PLAYERS_RANK, OP_LIST_ROUND_PER_TOURNAMENT,
                             OP_LIST_TOURNAMENT, OP_MAIN_MENU, OP_QUIT_PROGRAM, OP_REPORT_MENU, OP_START_TOURNAMENT,
                             OP_TOURNAMENT_MENU, LISTED_PLAYERS_NO, LISTED_PLAYERS_YES, MAX_NUM_PLAYERS)
import json
import sys


class Controller:

    db_players = TinyDB("data/Joueurs.json", indent=4)
    db_tournament = TinyDB("data/Tournoi.json", indent=4, default=str)

    def __init__(self, view):
        self.players = []
        self.tournaments = []
        self.view = view

    def launch_program(self):
        while True:
            option = self.view.main_menu()
            if option == OP_TOURNAMENT_MENU:
                self.tournament_program()
            elif option == OP_CHANGE_RANK:
                self.players_menu()
            elif option == OP_REPORT_MENU:
                self.report_menu()
            elif option == OP_QUIT_PROGRAM:
                self.quit_program()
            else:
                print("!! Choix non valide !!")

    def tournament_program(self):
        while True:
            option = self.view.tournament_menu()
            if option == OP_START_TOURNAMENT:
                self.start_tournament()
            elif option == OP_CONTINUE_TOURNAMENT:
                self.continue_tournament()
            elif option == OP_LAUNCH_MENU:
                self.launch_program()
            else:
                print("!! Choix non valide !!")

    def players_menu(self):
        while True:
            self.player_change_rank()
            self.launch_program()

    def report_menu(self):
        while True:
            option = self.view.input_report()
            if option == OP_LIST_PLAYERS_ALPHA:
                Player.players_list_alpha()
            elif option == OP_LIST_PLAYERS_RANK:
                Player.players_list_rank()
            elif option == OP_LIST_TOURNAMENT:
                Tournament.list_tournament()
            elif option == OP_LIST_PLAYER_PER_TOURNALENT_ALPHA:
                Tournament.list_tournament()
                data = self.view.input_choice()
                Player.players_per_tournament_alpha(int(data))
            elif option == OP_LIST_PLAYER_PER_TOURNALENT_RANK:
                Tournament.list_tournament()
                data = self.view.input_choice()
                Player.players_per_tournament_rank(int(data))
            elif option == OP_LIST_ROUND_PER_TOURNAMENT:
                Tournament.list_tournament()
                data = self.view.input_choice()
                Round.rounds_per_tournament(int(data))
            elif option == OP_LIST_MATCH_PER_TOURNAMENT:
                Tournament.list_tournament()
                data = self.view.input_choice()
                Tournament.matchs_per_tournament(int(data))
            elif option == OP_MAIN_MENU:
                self.launch_program()
            else:
                print("!! Choix non valide !!")

    def quit_program(self):
        return sys.exit()

    def continue_tournament(self):
        tournament_table = self.db_tournament.table("Tournament")
        to_continue_tournament_list = []

        if len(tournament_table) == 0:
            print("")
            print("!! Aucun tournoi à continuer !!")
            print("")
        else:
            # Selecting mode for tournament to continue
            print("")
            print("Liste des tournois incomplets :")
            print("-" * len("Liste des tournois incomplets :"))
            i = 0
            for tournament in tournament_table:
                if len(tournament["rounds"]) < tournament["number_round"]:
                    i += 1
                    print(i, "-", tournament["name"])
                    to_continue_tournament_list.append(tournament)

            if len(tournament["rounds"]) == tournament["number_round"]:
                print("!! Auncun tournoi à compléter !!")
                self.launch_program()

            print("")
            data = input("Votre choix: ")

            j = (int(data) - 1)

            tournament = to_continue_tournament_list[j]

            # Retrieve the tournament
            self.current_tournament = Tournament(tournament["name"],
                                                 tournament["place"],
                                                 tournament["start_date"],
                                                 tournament["end_date"],
                                                 tournament["description"])
            self.current_tournament.id = tournament["id"]
            self.current_tournament.number_round = tournament["number_round"]

            # Player object
            players_list = []
            score_liste = []
            for rounds in tournament["rounds"]:
                for matchs in rounds["matchs"]:
                    for players in matchs:
                        score_liste.append(players)
            for player_id in tournament["players"]:
                for players in self.db_players:
                    if players["id"] in player_id["id"]:
                        player = Player(players["first_name"],
                                        players["last_name"],
                                        players["birth_date"],
                                        players["gender"],
                                        players["rank"])
                        player.id = str(players["id"])
                        player.score = sum(x[1] if str(player.id) == x[0] else 0
                                           for x in score_liste)
                        players_list.append(player)
            self.current_tournament.players = players_list

            # Round object
            rounds_list = []
            matchs_list = []
            for sub in tournament["rounds"]:
                rnd = Round(sub["name"], sub["start_date"])
                for match in sub["matchs"]:
                    matchs_list.append(match)
                rnd.matchs = matchs_list
                rounds_list.append(rnd)
            tournament["rounds"] = rounds_list
            self.current_tournament.rounds = tournament["rounds"]
            self.start_round()

    def start_tournament(self):
        data = self.view.input_tournament()
        self.current_tournament = Tournament(data["tournament_name"],
                                             data["place"],
                                             data["start_date"],
                                             data["end_date"],
                                             data["description"],
                                             data["number_round"])
        print(self.current_tournament)
        self.save_tournament()
        self.add_listed_players()
        self.add_players()
        self.save_players()
        self.save_tournament_players()
        self.start_round()

    def start_round(self):
        while self.current_tournament.number_round != len(self.current_tournament.rounds):
            match = ()
            already_match = ()
            match_score = 0.0
            paired_list = []

            self.current_round = Round("Round " +
                                       str(len(self.current_tournament.rounds)+1),
                                       datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("")
            print("-----------------------------")
            print(self.current_round)
            print("-----------------------------")
            if len(self.current_tournament.rounds) == 0:
                paired_list = self.generate_pairs_round_1()
            elif len(self.current_tournament.rounds) <= self.current_tournament.number_round:
                paired_list = self.generate_pairs_remains_round()

            for pair in paired_list:
                match = ([pair[0], match_score], [pair[1], match_score])
                print(f"\nJoueur: {pair[0].last_name}\nVS\nJoueur: {pair[1].last_name}")
                self.add_score(match)
                already_match = (pair[0].id, pair[1].id)
                self.current_tournament.previous_match.append(already_match)
                self.current_round.matchs.append(match)

            self.current_tournament.rounds.append(self.current_round)
            self.save_update()

        self.display__final_score()
        self.end_message()
        self.launch_program()

    def add_players(self):
        while len(self.current_tournament.players) < MAX_NUM_PLAYERS:
            data = self.view.input_player(self.current_tournament)
            player = Player(data["last_name"], data["first_name"], data["birth_date"], data["gender"], data["rank"])
            self.current_tournament.players.append(player)

    def add_listed_players(self):
        if len(self.db_players) == 0:
            pass
        else:
            while True:
                print("")
                print("Voulez vous rajouter un joueur existant ?")
                print("1 - Oui")
                print("2 - Non")
                print("")
                data = input("Votre choix: ")
                print("")
                if data == LISTED_PLAYERS_YES:
                    self.listed_players()
                elif data == LISTED_PLAYERS_NO:
                    break
                else:
                    print("!! Choix non valide !!")

    def listed_players(self):
        db_players = TinyDB("data/Joueurs.json", indent=4)

        i = 1
        print("Liste des joueurs: ")
        print("-" * len("Liste des joueurs: "))

        for sub in db_players:
            print(f"{i} - Nom: {sub['last_name']} / Classement: {sub['rank']}")
            i += 1

        print("")
        data = input("Choix du joueur: ")
        element = db_players.get(doc_id=data)
        try:
            player = Player(element["first_name"],
                            element["last_name"],
                            element["birth_date"],
                            element["gender"],
                            element["rank"])
            player.id = element["id"]
            self.current_tournament.players.append(player)
            print("")
            print("Le joueur a été ajouté avec succès")
        except ValueError:
            print("")
            print("!! Choix non valide !!")

    def save_tournament(self):
        tournament_table = self.db_tournament.table("Tournament")

        serialized_tournament = {
            "name": self.current_tournament.name,
            "place": self.current_tournament.place,
            "start_date": self.current_tournament.start_date,
            "end_date": self.current_tournament.end_date,
            "description": self.current_tournament.description,
            "number_round": self.current_tournament.number_round,
            "id": self.current_tournament.id,
            "players": [],
            "rounds": []
        }

        for player in self.current_tournament.players:
            serialized_player = {
                "id": str(player.id)
            }
            serialized_tournament["players"].append(serialized_player)

        tournament_table.insert(serialized_tournament)

    def save_update(self):
        tournament_table = self.db_tournament.table("Tournament")
        q = Query()

        result = tournament_table.search(q.id == str(self.current_tournament.id))

        if len(result) == 1:
            tournament = result[0]

        for round in self.current_tournament.rounds:
            serialized_round = {
                            "name": round.name,
                            "start_date": round.start_date,
                            "matchs": []
                                }
            for match in round.matchs:
                serialized_round["matchs"].append(([match[0][0], match[0][1]], [match[1][0], match[1][1]]))

        tournament["rounds"].append(serialized_round)
        tournament_table.update(tournament, q.id == str(self.current_tournament.id))

    def save_tournament_players(self):
        tournament_table = self.db_tournament.table("Tournament")
        for player in self.current_tournament.players:
            serialized_player = {
                "id": str(player.id)
            }
            for sub in tournament_table:
                sub["players"].append(serialized_player)
            tournament_table.update({"players": sub["players"]})

    def save_players(self):
        serialized_players_list = []
        for player in self.current_tournament.players:
            for sub in self.db_players:
                if str(player.id) in sub["id"]:
                    break
            else:
                serialized_player = {
                    "last_name": player.last_name,
                    "first_name": player.first_name,
                    "birth_date": player.birth_date,
                    "gender": player.gender,
                    "rank": player.rank,
                    "id": str(player.id)
                }
                serialized_players_list.append(serialized_player)

        self.db_players.insert_multiple(serialized_players_list)

    def generate_pairs_round_1(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: int(x.rank))
        paired_list = [
                        (sorted_list[0], sorted_list[4]),
                        (sorted_list[1], sorted_list[5]),
                        (sorted_list[2], sorted_list[6]),
                        (sorted_list[3], sorted_list[7]),
                    ]
        return paired_list

    def generate_pairs_remains_round(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: (-x.score, x.rank))
        paired_list = []
        already_selected = []

        for i in range(len(sorted_list)):
            if sorted_list[i].id in already_selected:
                continue
            else:
                player_1 = sorted_list[i]
                already_selected.append(player_1.id)
                found_pair = False
                for j in range(i+1, len(sorted_list)):

                    if ((sorted_list[j].id in already_selected)
                            or ((player_1.id, sorted_list[j].id) in self.current_tournament.previous_match)
                            or ((sorted_list[j].id, player_1.id) in self.current_tournament.previous_match)):
                        continue
                    else:
                        player_2 = sorted_list[j]
                        already_selected.append(player_2.id)
                        pair = (player_1, player_2)
                        paired_list.append(pair)
                        found_pair = True
                        break
                if not found_pair:
                    player_2 = sorted_list[i+1]
                    already_selected.append(player_2.id)
                    pair = (player_1, player_2)
                    paired_list.append(pair)

        return paired_list

    def add_score(self, match):
        element_1 = match[0]
        data_1 = float(self.view.input_score(element_1[0]))
        element_1[0].score += data_1
        element_1[1] += data_1
        element_2 = match[1]
        data_2 = float(self.view.input_score(element_2[0]))
        while ((data_1 == 0.5 and data_2 != 0.5) or
               (data_1 == 0.5 and data_2 == 0) or
               (data_1 == 0.5 and data_2 == 1) or
               (data_1 == 0 and data_2 == 0) or
               (data_1 == 0 and data_2 == 0.5) or
               (data_1 == 1 and data_2 == 0.5) or
               (data_1 == 1 and data_2 == 1)):
            print("Valeur incorrecte")
            data_2 = float(self.view.input_score(element_2[0]))
        element_2[0].score += data_2
        element_2[1] += data_2

    def display__final_score(self):
        print("")
        print("SCORE FINAL")
        print("===========")

        sorted_list = sorted(self.current_tournament.players, key=lambda x: (-x.score, x.rank))
        for player in sorted_list:
            print(f"Nom: {player.last_name} / Score: {player.score}")

    def player_change_rank(self):
        file = Path("data/Joueurs.json")
        data = open(file)
        isempty = file.stat().st_size == 0
        if isempty:
            print("")
            print("Il n'y a aucune données de joueur")
            print("")
        else:
            data_obj = json.load(data)

            list_players = []
            for key in data_obj:
                for value in data_obj[key]:
                    list_players.append(data_obj[key][value])

                i = 1
                print("")
                sorted_list = sorted(list_players, key=lambda x:  int(x["rank"]))
                for player in sorted_list:
                    print((i), "- Nom:", player["last_name"], "\nClassement:", player["rank"])
                    print("-----------------")
                    i += 1

            print("")
            option = self.view.select_player()
            j = (int(option)-1)
            print("")
            print("Nom:", sorted_list[j]["last_name"], "/ Classement:", sorted_list[j]["rank"])
            rank = self.view.change_rank()
            print("")
            sorted_list[j].update({"rank": rank})
            print("Le classement du joueur a été mis à jour avec succès")
            print("")
            data = open(file, "w")
            json.dump(data_obj, data, indent=4)

    @staticmethod
    def end_message():
        message = ("=====================================\nFELICITATIONS, LE TOURNOI EST TERMINE\n====================\
=================")
        return print(message)
