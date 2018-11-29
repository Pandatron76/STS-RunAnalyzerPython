# Stores choices made at Campfire

from helpers import flatten_helper


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


def avg_campfires_rested(run_set):
    while True:
        try:
            return round(total_campfires_rested(run_set) / len(run_set), 2)
        except ZeroDivisionError:
            print("Cannot divide the total_campfires_rested by 0")
            return 0


def avg_campfires_visited(run_set):
    while True:
        try:
            return round(total_campfires_visited(run_set) / len(run_set), 2)
        except ZeroDivisionError:
            print("Cannot divide the total_campfires_visited by 0")
            return 0


def avg_campfires_upgraded(run_set):
    while True:
        try:
            return round(total_campfires_upgraded(run_set) / len(run_set), 2)
        except ZeroDivisionError:
            print("Cannot divide the total_campfires_upgraded by 0")
            return 0


def store_campfire_choices(current_run, parsed):
    if 'campfire_choices' in parsed:
        for element in parsed['campfire_choices']:
            current_campfire_choice = Campfire()

            current_campfire_choice.add_floor(element.get('floor'))
            current_campfire_choice.add_key(element.get('key'))
            current_campfire_choice.add_data(element.get('data'))
            current_run.add_campfire_choices(current_campfire_choice)

    return current_run


def campfire_choices_rest(run_set):
    rests_per_floor = campfire_rested_per_floor(run_set)

    print('\n')
    print('****************************************')
    print('** Campfire Rested Choice per Floor: **')
    print('****************************************')
    print('\n')

    for floor, rest_count in sorted(rests_per_floor.items()):
        print("Floor: %s || Rested: %s" % (floor, rest_count))


def campfire_choices_upgraded(run_set):
    floor_pick_dict = campfire_upgrades_per_floor(run_set)

    print('\n')
    print('****************************************')
    print('** Campfire Upgrade Choice per Floor: **')
    print('****************************************')
    print('\n')

    for floor, upgrades in sorted(floor_pick_dict.items()):
        card_type_count = {i: upgrades.count(i) for i in upgrades}
        print("Floor: %s" % floor)
        for a, b in card_type_count.items():
            print("  Card: %s || Upgrade Count: %s" % (a, b))


def campfire_rested_per_floor(run_set):
    floor_rest_dict = {}
    campfire_rested_count = 0

    for run in run_set:
        for choice in run.campfire_choices:
            if choice.key == 'REST':
                campfire_rested_count += 1
                if choice.floor not in floor_rest_dict.keys():
                    floor_rest_dict.update({int(round(choice.floor)): 1})
                elif choice.floor in floor_rest_dict.keys():
                    floor_rest_dict[int(round(choice.floor))] += 1
                else:
                    print('Issue with campfire_rested_per_floor inner loop, run_data.campfire_choices')

    return floor_rest_dict


def campfire_upgrades_per_floor(run_set):
    floor_picked_dict = {}
    runids_wo_floors = []
    no_choice_count = 0

    for run in run_set:
        for choice in run.campfire_choices:
            if not choice.key:
                no_choice_count += 1
                runids_wo_floors.append(run.id)
            elif choice.key:
                if choice.key == 'SMITH':
                    current_campfire_choices = []
                    for k, v in floor_picked_dict.items():
                        if int(k) == int(choice.floor):
                            current_campfire_choices.append(v)

                    current_campfire_choices.append(choice.data)
                    flatten_picks = flatten_helper.flatten_word_list(current_campfire_choices)
                    floor_picked_dict.update({int(round(choice.floor)): flatten_picks})
            else:
                print("Issue with math_funcs.campfire_upgrades_per_floor")

    print('\n')
    return floor_picked_dict


def total_campfires_visited(run_set):
    return total_campfires_rested(run_set) + total_campfires_upgraded(run_set)


def total_campfires_rested(run_set):
    return sum(run.campfire_rested for run in run_set)


def total_campfires_upgraded(run_set):
    return sum(run.campfire_upgraded for run in run_set)



