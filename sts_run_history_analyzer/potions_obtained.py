# Stores choice made a Events


class PotionsObtained:

    def __init__(self):
        self.floor = 0
        self.key = ''

    def add_floor(self, floor):
        self.floor = floor

    def add_key(self, key):
        self.key = key
