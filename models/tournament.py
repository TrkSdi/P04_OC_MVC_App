from tinydb import TinyDB
from pathlib import Path

class Tournament():
    
    
    def __init__(self, name, place, start_date, end_date, description, number_round=4):
        self.name = name
        self.place = place
        self.start_date  = start_date
        self.end_date = end_date
        self.description = description
        self.number_round = number_round
        self.players = []
        self.rounds = []
        self.previous_match = []

    def __str__(self):
        return f"\nNom du tournoi: {self.name}\nNombre de rounds: {self.number_round}\nDescription: {self.description}\n"

    
    