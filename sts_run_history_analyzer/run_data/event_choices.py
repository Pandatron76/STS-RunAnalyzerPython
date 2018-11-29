# Stores choice made a Events


class EventChoices:

    def __init__(self):
        self.damage_taken = 0
        self.event_name = ''
        self.floor = 0
        self.player_choice = ''

    def add_damage_taken(self, damage_taken):
        self.damage_taken = damage_taken

    def add_event_name(self, event_name):
        self.event_name = event_name

    def add_floor(self, floor):
        self.floor = floor

    def add_player_choice(self, player_choice):
        self.player_choice = player_choice
