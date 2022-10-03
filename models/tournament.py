from textwrap import indent
from tinydb import TinyDB, Query
from pathlib import Path
from models.round import Round
import uuid

class Tournament():
 
    def __init__(self, name, place, start_date, end_date, description, number_round):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_round = 4
        self.players = []
        self.rounds = []
        self.previous_match = []
        self.rank_list = []
        self.paired_list = []
        self.id = uuid.uuid4()
        

    def __str__(self):
        return f"\nNom du tournoi: {self.name}\nNombre de rounds: {self.number_round}\nDescription: {self.description}\n"

    
    