rank_list = []

for i in range(8):
    
    while i < 8 :
        rank = input("Entrez son classement: ")
        if not rank.isdigit():
            print("Veuillez entrez un choix valide")
        elif rank == "":
            print("Veuillez entrez un choix valide")
        elif rank in str(rank_list):
            print("Classement déjà assigné")   
        else:
            i += 1
            rank_list.append(rank)
            print(rank_list)
            break