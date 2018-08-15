# Stores choices made after each pack of cards


class CardChoices:

    def __init__(self):
        self.floor = ''
        self.not_picked = []
        self.picked = ''

    def add_floor(self, floor):
        self.floor = floor

    def add_not_picked(self, not_picked):
        self.not_picked.extend(not_picked)

    def add_picked(self, picked):
        self.picked = picked
