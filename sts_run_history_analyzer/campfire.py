# Stores choices made at Campfire


class Campfire:

    def __init__(self):
        self.data = ''
        self.floor = ''
        self.key = ''

    def add_data(self, data):
        self.data = data

    def add_floor(self, floor):
        self.floor = floor

    def add_key(self, key):
        self.key = key
