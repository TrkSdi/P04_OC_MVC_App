import json

def matchs_per_tournament(i):
    file = "/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Tournoi.json"
    data = open(file)
    data = json.load(data)
    
    file = "/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Joueurs.json"
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
            new_match = [[match[0][0],match[0][1]],[match[1][0],match[1][1]]]
            new_list.append(new_match)
    
    print("Liste des matchs:")
    print("-" * len("Liste des matchs:"))
    print("")
    for match in new_list:
        print(match)
    print("")
      