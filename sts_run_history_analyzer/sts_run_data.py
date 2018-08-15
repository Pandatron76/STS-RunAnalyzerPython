# Holds information pertaining to a single Slay the Spire playthrough


class STSRunData:

    def __init__(self, id):
        # UD values derived from json
        self.id = id
        self.starting_gold = 99
        self.boss_relic_picked_act1 = ''
        self.boss_relic_not_picked_act1 = []
        self.boss_relic_picked_act2 = ''
        self.boss_relic_not_picked_act2 = []
        self.gold_diff_per_floor = []
        self.total_gold_gained = 0
        self.total_gold_lost = 0

        # Values part of the json
        self.ascension = ''
        self.build_version = ''
        self.campfire_choices = []
        self.campfire_rested = 0
        self.campfire_upgraded = 0
        self.card_choices = []
        self.character_chosen = ''
        self.chosen_seed = ''
        self.circlet_count = 0
        self.current_hp_per_floor = []
        self.damage_taken = []
        self.event_choices = []
        self.floor_reached = 0
        self.gold = 0
        self.gold_per_floor = []
        self.is_ascension_mode = False
        self.is_daily = False
        self.is_endless = False
        self.is_prod = False
        self.is_trial = False
        self.items_purchased_floor = []
        self.items_purchased = []
        self.items_purged = []
        self.items_purged_floor = []
        self.local_time = ''
        self.killed_by = ''
        self.master_deck = []
        self.max_hp_per_floor = []
        self.neow_bonus = ''
        self.neow_cost = ''
        self.path_per_floor = []
        self.path_taken = []
        self.play_id = ''
        self.player_experience = ''
        self.playtime = 0
        self.potions_floor_spawned = []
        self.potions_floor_usage = []
        self.potions_obtained = []
        self.purchased_purges = 0
        self.relics = []
        self.relics_obtained = []
        self.score = 0
        self.seed_played = ''
        self.seed_source_timestamp = 0
        self.special_seed = 0
        self.timestamp = 0
        self.victory = False
        self.win_rate = 0

    def add_gold_diff_per_floor(self, diff):
        self.gold_diff_per_floor.append(diff)

    def add_total_gold_gained(self, total_gold_gained):
        self.total_gold_gained = total_gold_gained

    def add_total_gold_lost(self, total_gold_lost):
        self.total_gold_lost = total_gold_lost

    def add_boss_relic_picked_act1(self, relic):
        self.boss_relic_picked_act1 = relic

    def add_boss_relic_not_picked_act1(self, relic):
        self.boss_relic_not_picked_act1.append(relic)

    def add_boss_relic_picked_act2(self, relic):
        self.boss_relic_picked_act2 = relic

    def add_boss_relic_not_picked_act2(self, relic):
        self.boss_relic_not_picked_act2.append(relic)

    def add_campfire_choices(self, campfire_choices):
        self.campfire_choices.append(campfire_choices)

    def add_card_choices(self, card_choices):
        self.card_choices.append(card_choices)

    def add_current_hp_for_floor(self, current_hp):
        self.current_hp_per_floor.append(current_hp)

    def add_damage_taken(self, damage_taken):
        self.damage_taken.append(damage_taken)

    def add_event_choices(self, event_choices):
        self.event_choices.append(event_choices)

    def add_gold_for_floor(self, gold):
        self.gold_per_floor.append(gold)

    def add_items_purchased(self, items_purchased):
        self.items_purchased.append(items_purchased)

    def add_master_deck(self, master_deck):
        self.master_deck.append(master_deck)

    def add_max_hp_per_floor(self, max_hp_per_floor):
        self.max_hp_per_floor.append(max_hp_per_floor)

    def add_path_per_floor(self, path):
        self.path_per_floor.append(path)

    def add_path_taken(self, taken):
        self.path_taken.append(taken)

    def add_potions_floor_spawned(self, potion):
        self.potions_floor_spawned.append(potion)

    def add_potions_floor_usage(self, potion):
        self.potions_floor_usage.append(potion)

    def add_potions_obtained(self, potion):
        self.potions_obtained.append(potion)

    def add_relics(self, relic):
        self.relics.append(relic)

    def add_relics_obtained(self, relic):
        self.relics_obtained.append(relic)

    def sort_master_deck(self):
        self.master_deck.sort()

    def highest_max_hp_per_floor(self):
        max(self.max_hp_per_floor(), key=lambda item: item[1])
