

from uuid import uuid4
from tinydb import TinyDB

db_tournament = TinyDB("data/Tournoi.json", indent=4, default=str)

tournament_table = db_tournament.table("Tournament")

print(tournament_table)

liste = ["Tarik", "Mamadou", "George"]

for sub in tournament_table:
    for players in liste:
        sub["players"].append(players)
    
    
    tournament_table.update({"players": sub["players"]})
    


