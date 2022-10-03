from tinydb import TinyDB, Query, where


db_test = TinyDB("test.json", indent=4)
new_table = db_test.table("NEW")


dict_new = {'name': 'Le tournoi de Montpellier', 
            'place': 'Montpellier', 
            'start_date': '05/06/2022', 
            'end_date': '05/06/2022', 
            'description': 'International', 
            'number_round': 4, 
            'id': '272db3d4-15e8-4a44-9680-cad95304864b', 
            'players': [{'id': '7f49102a-b4b4-4ac1-a1e4-0bf98afa9868'}, 
                        {'id': '580deb6c-1b5e-4a6f-abb9-5534de748bf9'}, 
                        {'id': 'd066d38d-63bc-48d6-acc5-6c389efadbdc'}, 
                        {'id': '85ed8e05-01d6-44ca-abcf-b099e67a7af6'}, 
                        {'id': 'cf9e0e03-4258-4218-b2ea-6079e7d05604'}, 
                        {'id': '8491fe94-6403-46ae-9e6d-a58e8179c63c'}, 
                        {'id': '5f0812ca-9398-46ea-841d-e3ac56b36dcc'}, 
                        {'id': 'bc13661c-2427-4fca-83dd-469384c9af0e'}], 
            'rounds': []
            }
            
            
new_table.truncate()
new_table.insert(dict_new)

Q = Query()

#result = new_table.search(Q.id == '272db3d4-15e8-4a44-9680-cad95304864b')



dict_new_1 = {'name': 'Le tournoi de Montpellier', 
            'place': 'Montpellier', 
            'start_date': '05/06/2022', 
            'end_date': '05/06/2022', 
            'description': 'International', 
            'number_round': 4, 
            'id': '272db3d4-15e8-4a44-9680-cad95304864b', 
            'players': [{'id': '1'}, 
                        {'id': '2'}, 
                        {'id': '3'}, 
                        {'id': '4'}, 
                        {'id': '5'}, 
                        {'id': '6'}, 
                        {'id': '7'}, 
                        {'id': '8'}], 
            'rounds': []
            }


liste = ["1", "2", "3"]

for element in liste:
    dict_new_1["rounds"].append(element)
    
    
new_table.update(dict_new_1)
print(new_table)