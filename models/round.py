
class Round:
    def __init__(self, name, start_date, end_date=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matchs = []
        