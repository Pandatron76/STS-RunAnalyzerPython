# Holds computational functions that cannot be directly derived from the json
import collections


def cards_picked_per_floor(run_set):
    floor_picked_dict = {}
    runids_wo_floors = []
    no_floor_count = 0

    for run in run_set:
        for card in run.card_choices:
            if not card.floor:
                no_floor_count += 1
                runids_wo_floors.append(run.id)
            elif card.floor:
                flatten_dict_by_floor(card, floor_picked_dict)
            else:
                print("Issue with math_funcs.cards_picked_per_floor")

    print("No floor count (Card Choice): %s" % no_floor_count)

    return floor_picked_dict


def enemies_encountered_per_floor(run_set):
    floor_enemy_dict = {}

    for run in run_set:
        for dt in run.damage_taken:
            current_enemy_list = []
            for k, v in floor_enemy_dict.items():
                if int(k) == int(dt.floor):
                    current_enemy_list.append(v)

            if isinstance(None, type(dt.enemies)) is False:
                current_enemy_list.append(dt.enemies)
            elif isinstance(None, type(dt.enemies)) is True:
                current_enemy_list.append("None")
            else:
                print("Issues with evaluating 'None' in enemies_encountered_per_floor")

            flatten_picks = flatten_word_list(current_enemy_list)
            floor_enemy_dict.update({int(round(dt.floor)): flatten_picks})

    return floor_enemy_dict


def events_encountered_per_floor(run_set):
    floor_event_dict = {}

    for run in run_set:
        for choice in run.event_choices:
            current_event_list = []
            for floor, event_name in floor_event_dict.items():
                if int(floor) == int(choice.floor):
                    current_event_list.append(event_name)

            current_event_list.append(choice.event_name)
            flatten_picks = flatten_word_list(current_event_list)
            floor_event_dict.update({int(round(choice.floor)): flatten_picks})

    print('\n')
    return floor_event_dict


def event_choice_per_event(run_set):
    event_choice_dict = {}
    for run in run_set:
        for choice in run.event_choices:
            current_choice_list = []
            for event_name, player_choice in event_choice_dict.items():
                if event_name == choice.event_name:
                    current_choice_list.append(player_choice)

            current_choice_list.append(choice.player_choice)
            flatten_picks = flatten_word_list(current_choice_list)
            event_choice_dict.update({str(choice.event_name): flatten_picks})

    print('\n')
    return event_choice_dict


def total_damage_per_enemy(run_set):
    enemy_dmg_dict = {}
    for run in run_set:
        for dt in run.damage_taken:
            if dt.enemies not in enemy_dmg_dict.keys():
                enemy_dmg_dict.update({str(dt.enemies): int(dt.damage)})
            elif dt.enemies in enemy_dmg_dict.keys():
                enemy_dmg_dict[str(dt.enemies)] += int(dt.damage)
            else:
                print('Issue with damage_per_enemy func')

    return enemy_dmg_dict


def enemy_encounter_count(run_set):
    enemy_count_dict = {}
    for run in run_set:
        for dt in run.damage_taken:
            if dt.enemies not in enemy_count_dict.keys():
                enemy_count_dict.update({str(dt.enemies): 1})
            elif dt.enemies in enemy_count_dict.keys():
                enemy_count_dict[str(dt.enemies)] += 1
            else:
                print('Issue with damage_per_enemy func')

    return enemy_count_dict


def flatten_dict_by_floor(card, floor_picked_dict):
    current_floor_picks = []
    for k, v in floor_picked_dict.items():
        if int(k) == int(card.floor):
            current_floor_picks.append(v)

    current_floor_picks.append(card.picked)
    flatten_picks = flatten_word_list(current_floor_picks)
    floor_picked_dict.update({int(round(card.floor)): flatten_picks})

    return floor_picked_dict


def flatten_word_list(x):
    result = []
    for el in x:
        if isinstance(x, collections.Iterable) and not isinstance(el, str):
            result.extend(flatten_word_list(el))
        else:
            result.append(el)

    return result


def highest_max_hp(run_set):
    highest_max_hp_all = 0
    file_name = ''
    for run in run_set:
        # An empty set evaluates to 0 if it is empty. At least one value should exist in max_hp_per_floor
        if run.max_hp_per_floor is False:
            if max(run.max_hp_per_floor) > highest_max_hp_all:
                highest_max_hp_all = max(run.max_hp_per_floor)
                file_name = run.id

    return highest_max_hp_all, file_name


def highest_score(run_set):
    highest_score_all = 0
    file_name = ''
    for run in run_set:
        if isinstance(None, type(run.score)) is False:
            if run.score > highest_score_all:
                highest_score_all = run.score
                file_name = run.id

    return highest_score_all, file_name


def items_purchased_count(run_set):
    items_purchased_dict = {}
    for run in run_set:
        for item in run.items_purchased:
            if item not in items_purchased_dict.keys():
                items_purchased_dict.update({str(item): 1})
            elif item in items_purchased_dict.keys():
                items_purchased_dict[str(item)] += 1
            else:
                print('Issue with items_purchased_count func')

    return items_purchased_dict


def lowest_floor_death(run_set):
    lowest_floor = 51
    file_name = ''
    for run in run_set:
        if run.floor_reached < lowest_floor:
            lowest_floor = run.floor_reached
            file_name = run.id

    return lowest_floor, file_name


def lowest_max_hp(run_set):
    lowest_max_hp_all = 99999
    file_name = ''
    for run in run_set:
        # An empty set evaluates to 0 if it is empty. At least one value should exist in max_hp_per_floor
        if run.max_hp_per_floor:
            if min(run.max_hp_per_floor) < lowest_max_hp_all:
                lowest_max_hp_all = min(run.max_hp_per_floor)
                file_name = run.id

    return lowest_max_hp_all, file_name


def lowest_score(run_set):
    lowest_score_all = 99999
    file_name = ''
    for run in run_set:
        if isinstance(None, type(run.score)) is False:
            if run.score < lowest_score_all:
                lowest_score_all = run.score
                file_name = run.id

    return lowest_score_all, file_name


def most_gold_held(run_set):
    gold_spent = 0
    file_name = ''
    for run in run_set:
        if run.gold_per_floor:
            if gold_spent < max(run.gold_per_floor):
                gold_spent = max(run.gold_per_floor)
                file_name = run.id

    return gold_spent, file_name


def potions_spawned_stats(run_set):
    total_potions_spawned = {}
    for run in run_set:
        for floor in run.potions_floor_spawned:
            if floor not in total_potions_spawned.keys():
                total_potions_spawned.update({floor: 1})
            elif floor in total_potions_spawned.keys():
                total_potions_spawned[floor] += 1
            else:
                print("Issue with potions spawned stats")

    return total_potions_spawned


def potions_used_stats(run_set):
    total_potions_used = {}
    for run in run_set:
        for floor in run.potions_floor_usage:
            if floor not in total_potions_used.keys():
                total_potions_used.update({floor: 1})
            elif floor in total_potions_used.keys():
                total_potions_used[floor] += 1
            else:
                print("Issue with potions used stats")

    return total_potions_used


def potions_obtained_stats(run_set):
    potions_obtained_dict = {}
    runids_wo_potions = []
    no_floor_count = 0

    for run in run_set:
        for potion in run.potions_obtained:
            if not potion.floor:
                no_floor_count += 1
                runids_wo_potions.append(run.id)
            elif potion.floor:
                current_obtained_potions = []
                for k, v in potions_obtained_dict.items():
                    if int(k) == int(potion.floor):
                        current_obtained_potions.append(v)

                current_obtained_potions.append(potion.key)
                flatten_picks = flatten_word_list(current_obtained_potions)
                potions_obtained_dict.update({int(round(potion.floor)): flatten_picks})
            else:
                print("Issue with math_funcs.potions_obtained_stats")

    # Debugging purposes. To check for any potions that were not recorded.
    # print("Potions without floor data (Potions Obtained): %s" % no_floor_count)

    return potions_obtained_dict


def relic_count(run_set):
    relic_dict = {}
    for run in run_set:
        for relic in run.relics:
            if relic not in relic_dict.keys():
                relic_dict.update({str(relic): 1})
            elif relic in relic_dict.keys():
                relic_dict[str(relic)] += 1
            else:
                print('Issue with items_purchased_count func')

    return relic_dict


def win_lost_record(run_set):
    total_wins = 0
    total_loses = 0
    for run in run_set:
        if run.victory is True:
            total_wins += 1
        elif run.victory is False:
            total_loses += 1
        else:
            print('No win or lost recorded')

    return total_wins, total_loses
