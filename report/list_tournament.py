import json

def list_tournament(): 
    file = "/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Tournoi.json"
    data = open(file)
    data = json.load(data)
    list_all_tournament = []
    list_per_tournament = []
    
    for key in data:
        for value in data[key]:
    
            list_all_tournament.append(data[key][value])
    
    i = 0
    for dictionnary in list_all_tournament:
            i += 1
            #print("_" * 50)
            tournament = str(i) + " - " + dictionnary["name"]
            list_per_tournament.append(tournament)
    
    print("")
    print("Liste des tournois: ")
    print("-" * len("Liste des tournois:"))
    print("")
    for tournament in list_per_tournament:
        print(tournament) 
    print("")
    