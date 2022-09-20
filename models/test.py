import json
 
# opening the JSON file
data = open('Joueurs.json',)
 
print("Datatype before deserialization : "
      + str(type(data)))
    
# deserializing the data
data = json.load(data)
 
print("Datatype after deserialization : "
      + str(type(data)))