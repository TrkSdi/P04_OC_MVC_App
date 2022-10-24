from tinydb import TinyDB

db_players = TinyDB("data/Joueurs.json", indent=4)


for element in db_players:
    
    print(len(element))