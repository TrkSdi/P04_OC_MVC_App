from curses import def_shell_mode
from email.policy import default
from pathlib import Path
from tinydb import TinyDB
import json



db = TinyDB("/Users/dev/Desktop/En cours/Projet_04/Chess_Project_V2/data/Test.json", indent=2, default=str)
tournament_table = db.table("Tournament")


    
updt_dict = {"joueur_1": 
                {
                "nom": "Tarik",
                "age": "38",
                "tour": 
                    {
                    "score": 1,
                    "rang": 1,
                    "liste": []
                    }
                },
             "joueur_2": 
                {
                "nom": "Marie",
                "age": "40",
                "tour": 
                    {
                    "score": 2,
                    "rang": 2,
                    "liste": []
                    }
                },
            }



valeur = ["a", "b", "c", "d", "e", "f"]


#for dictionnaires in db:
#    for joueur in dictionnaires:
#        #print(dictionnaires[joueur]["tour"]["liste"])
#        dictionnaires[joueur]["tour"]["liste"].append(valeur)
#        print(dictionnaires[joueur]["tour"]["liste"])
#    updt_dict.update(dictionnaires)       
#        
#
#print(updt_dict)


for dictionnaires in tournament_table:
    dictionnaires["rounds"].append(valeur)

    tournament_table.update(dictionnaires)
   
try: 
    json.dumps(db)
except:
    pass