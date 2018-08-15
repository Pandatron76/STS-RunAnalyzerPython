# Store when the player took damage on each floor


class DamageTaken:

    def __init__(self):
        self.damage = 0
        self.enemies = ''
        self.floor = 0
        self.turns = 0

    def add_damage(self, damage):
        self.damage = damage

    def add_enemies(self, enemies):
        self.enemies = enemies

    def add_floor(self, floor):
        self.floor = floor

    def add_turns(self, turns):
        self.turns = turns
