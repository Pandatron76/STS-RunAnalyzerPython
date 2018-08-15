# Prints information for a all runs in a human readable format
import calculate_average
import calculate_total
import math_funcs


def details(run_set):
    win_lost_records(run_set)
    campfire_stats(run_set)

    print('\n')
    print('***************')
    print('** HUD Data: **')
    print('***************')

    highest_max_hp(run_set)
    lowest_max_hp(run_set)
    most_gold(run_set)
    potions_data_spawned(run_set)
    potions_data_used(run_set)
    potions_data_obtained(run_set)
    enemy_encounter_count(run_set)
    cumulative_dmg_enemy(run_set)
    misc(run_set)
    cards_picked_per_floor(run_set)


def avg_campfires_rested(run_set):
    average = calculate_average.campfire_rested(run_set)
    if average > 0:
        print('Average number of campfires rested: %s' % average)
    else:
        print("There was an issue calculating the avg_campfires_rested")


def avg_campfires_visited(run_set):
    average = calculate_average.campfires_visited(run_set)
    if average > 0:
        print('Average number of campfires visited per playthrough: %s' % average)
    else:
        print("There was an issue calculating the avg_campfires_visited")


def avg_floor_reached(run_set):
    average = (round(calculate_average.floor_reached(run_set)), calculate_average.floor_reached(run_set))
    raw, rounded = average
    if raw > 0:
        print("Average floor reached: %s (%s)" % (raw, average))
    else:
        print("There was an issue calculating the avg_floor_reached")


def avg_score(run_set):
    average = calculate_average.score(run_set)
    if average > 0:
        print("Average Score: %s" % average)
    else:
        print("There was an issue calculating the avg_score")


def avg_campfires_upgraded(run_set):
    average = calculate_average.campfire_upgraded(run_set)
    if average > 0:
        print('Average number of upgrades at campfires: %s' % average)
    else:
        print("There was an issue calculating the avg_campfires_upgraded")


def campfire_choices_rest(run_set):
    rests_per_floor = math_funcs.campfire_rested_per_floor(run_set)

    print('\n')
    print('****************************************')
    print('** Campfire Rested Choice per Floor: **')
    print('****************************************')
    print('\n')

    for floor, rest_count in sorted(rests_per_floor.items()):
        print("Floor: %s || Rested: %s" % (floor, rest_count))


def campfire_choices_upgraded(run_set):
    floor_pick_dict = math_funcs.campfire_upgrades_per_floor(run_set)

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


def campfire_stats(run_set):

    print('\n')
    print('********************')
    print('** Campfire Data: **')
    print('********************')

    total_campfires_visited(run_set)
    avg_campfires_rested(run_set)
    total_campfires_rested(run_set)
    avg_campfires_rested(run_set)
    total_campfires_upgraded(run_set)
    avg_campfires_upgraded(run_set)
    print('\n')


def cumulative_dmg_enemy(run_set):
    enemy_dmg_dict = math_funcs.total_damage_per_enemy(run_set)
    sorted_enemy_dmg_list = sorted(enemy_dmg_dict.items(), key=lambda kv: kv[1], reverse=True)
    total_enemy_dmg = sum(enemy_dmg_dict.values())
    enemy_count = 1

    print('\n')
    print('**********************************')
    print('** Cumulative Damage Per Enemy: **')
    print('**********************************')
    print('\n')

    for enemy_damage in sorted_enemy_dmg_list:
        (enemy, damage) = enemy_damage
        percentage = round((damage / total_enemy_dmg), 2)
        print("%s. %s || %s (Percentage: %s)" % (enemy_count, enemy, damage, percentage))
        enemy_count += 1


def cards_picked_per_floor(run_set):
    floor_pick_dict = math_funcs.cards_picked_per_floor(run_set)

    print('\n')
    print('*****************************')
    print('** Cards Picked per Floor: **')
    print('*****************************')
    print('\n')

    for floor, picks in sorted(floor_pick_dict.items()):
        card_type_count = {i: picks.count(i) for i in picks}
        print("Floor: %s" % floor)
        for card, picked_count in card_type_count.items():
            print("  Card: %s || Picked: %s" % (card, picked_count))


def enemy_encounter_count(run_set):
    enemy_count_dict = math_funcs.enemy_encounter_count(run_set)
    sorted_enemy_count_list = sorted(enemy_count_dict.items(), key=lambda kv: kv[1], reverse=True)
    total_enemy_count = sum(enemy_count_dict.values())
    enemy_count = 1

    print('\n')
    print('****************************')
    print('** Enemy Encounter Count: **')
    print('****************************')
    print('\n')

    for enemy_count_tuple in sorted_enemy_count_list:
        (enemy, count) = enemy_count_tuple
        percentage = round((count / total_enemy_count), 2)
        print("%s. %s || %s (Percentage: %s)" % (enemy_count, enemy, count, percentage))
        enemy_count += 1


def enemies_per_floor(run_set):
    floor_enemy_dict = math_funcs.enemies_encountered_per_floor(run_set)

    for floor, enemy_type in sorted(floor_enemy_dict.items()):
        enemy_type_count = {i: enemy_type.count(i) for i in enemy_type}
        print("Floor: %s" % floor)
        for enemy, count in enemy_type_count.items():
            print("  Enemy: %s || Count: %s" % (enemy, count))


def event_choices_per_floor(run_set):
    #TODO: Update to including what specific decisions they chose
    floor_event_dict = math_funcs.events_encountered_per_floor(run_set)

    for event_choice, choices in sorted(floor_event_dict.items()):
        event_count = {i: choices.count(i) for i in choices}
        print("Event Choice: %s" % event_choice)
        for event, choice in event_count.items():
            print("  Event: %s || Count: %s " % (event, choice))


def highest_max_hp(run_set):
    (highest_max_hp_all, highest_hp_file_name) = math_funcs.highest_max_hp(run_set)
    print("Highest Max HP: %s || File Name: %s" % (highest_max_hp_all, highest_hp_file_name))


def highest_score(run_set):
    (highest_score_all, highest_score_file_name) = math_funcs.highest_score(run_set)
    print("Highest Score: %s || File Name: %s" % (highest_score_all, highest_score_file_name))


def items_purchased_count(run_set):
    item_purchased_dict = math_funcs.items_purchased_count(run_set)
    sorted_item_purchase = sorted(item_purchased_dict.items(), key=lambda kv: kv[1], reverse=True)
    total_items_purchased = sum(item_purchased_dict.values())
    item_count = 1

    for item_count_tuple in sorted_item_purchase:
        (item, count) = item_count_tuple
        percentage = round((count / total_items_purchased), 2)
        print("%s. %s || %s (Percentage: %s)" % (item_count, item, count, percentage))
        item_count += 1

    print('\n')


def lowest_score(run_set):
    (lowest_score_all, lowest_score_file_name) = math_funcs.lowest_score(run_set)
    print("Lowest Score: %s || File Name: %s" % (lowest_score_all, lowest_score_file_name))


def lowest_max_hp(run_set):
    (lowest_max_hp_all, lowest_hp_file_name) = math_funcs.lowest_max_hp(run_set)
    print("Lowest Max HP: %s || File Name: %s" % (lowest_max_hp_all, lowest_hp_file_name))


def potions_data_spawned(run_set):
    potions_spawned_dict = math_funcs.potions_spawned_stats(run_set)
    total_potions_spawned = sum(potions_spawned_dict.values())

    print('\n')
    print('****************************')
    print('** Potions Data, Spawned: **')
    print('****************************')
    print('\n')

    print("List of Floors and Number of Potions spawned on each floor across all runs")
    for k, v in sorted(potions_spawned_dict.items()):
        print("Floor: %s || Number of Potions: %s (Percentage: %s)"
              % (k, v, round((v / total_potions_spawned), 2)))


def potions_data_used(run_set):
    potions_used_dict = math_funcs.potions_used_stats(run_set)
    total_potions_used = sum(potions_used_dict.values())

    print('\n')
    print('*************************')
    print('** Potions Data, Used: **')
    print('*************************')
    print('\n')

    print("List of Floors and Number of Potions used on each floor across all runs")
    for k, v in sorted(potions_used_dict.items()):
        print("Floor: %s || Number of Potions: %s (Percentage: %s)"
              % (k, v, round((v / total_potions_used), 2)))


def potions_data_obtained(run_set):
    floor_pick_dict = math_funcs.potions_obtained_stats(run_set)

    print('\n')
    print('********************************')
    print('** Potion Obtained per Floor: **')
    print('********************************')
    print('\n')

    for floor, potions in sorted(floor_pick_dict.items()):
        potion_type_count = {i: potions.count(i) for i in potions}
        print("Floor: %s" % floor)
        for potion, obtained in potion_type_count.items():
            print("  Potion: %s || Obtained Count: %s" % (potion, obtained))


def most_gold(run_set):
    # Gold
    (most_gold_held, most_gold_held_file_name) = math_funcs.most_gold_held(run_set)
    print("Most Gold Held: %s || File Name: %s" % (most_gold_held, most_gold_held_file_name))


def misc(run_set):
    (highest_score_all, highest_score_file_name) = math_funcs.highest_score(run_set)
    (lowest_score_all, lowest_score_file_name) = math_funcs.lowest_score(run_set)

    print('\n')
    print('***********')
    print('** Misc: **')
    print('***********')
    print('\n')

    print("Highest Score: %s || File Name: %s" % (highest_score_all, highest_score_file_name))
    print("Average Score: %s" % calculate_average.score(run_set))
    print("Lowest Score: %s || File Name: %s" % (lowest_score_all, lowest_score_file_name))
    print("Average floor reached: %s (%s)" %
          (round(calculate_average.floor_reached(run_set)), calculate_average.floor_reached(run_set)))


def relic_count(run_set):
    relic_dict = math_funcs.relic_count(run_set)
    sorted_relic = sorted(relic_dict.items(), key=lambda kv: kv[1], reverse=True)
    total_relics = sum(relic_dict.values())
    rank = 1

    for relic_count_tuple in sorted_relic:
        (relic, count) = relic_count_tuple
        percentage = round((count / total_relics), 2)
        print("%s. %s || %s (Percentage: %s)" % (rank, relic, count, percentage))
        rank += 1

    print('\n')


def total_campfires_visited(run_set):
    print('Total campfires visited: ', calculate_total.campfire_visited(run_set))


def total_campfires_rested(run_set):
    print('Total campfires rested at: ', calculate_total.campfire_rested(run_set))


def total_campfires_upgraded(run_set):
    print('Total campfire upgrades: ', calculate_total.campfire_upgraded(run_set))


def win_lost_records(run_set):
    wins, loses = math_funcs.win_lost_record(run_set)
    total_playthroughs = wins + loses

    if total_playthroughs > 0:

        print('\n')
        print('************************')
        print('** Win / Lost Record: **')
        print('************************')
        print('\n')

        print("Total playthroughs: %s" % total_playthroughs)
        print("Wins: %s (%s)" % (wins, round(wins / total_playthroughs, 2)))
        print("Loses: %s (%s)" % (loses, round(loses / total_playthroughs, 2)))
