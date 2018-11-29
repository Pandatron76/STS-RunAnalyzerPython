from helpers import math_funcs
from run_data import campfire
from helpers import calculate_average


def store_winlost_message(config_item, run_set):
    wins, loses = math_funcs.win_lost_record(run_set)
    total_playthroughs = wins + loses

    if total_playthroughs > 0:
        config_item.console_message += "Total playthroughs: %s\n" % total_playthroughs
        config_item.console_message += "Wins: %s (%s)\n" % (wins, round(wins / total_playthroughs, 2))
        config_item.console_message += "Loses: %s (%s)\n" % (loses, round(loses / total_playthroughs, 2))


def store_campfire_message(config_item, run_set):
    config_item.console_message += \
        "Total campfires visited: %s\n" % campfire.total_campfires_visited(run_set)
    config_item.console_message += \
        "Average campfires rested at: %s\n" % campfire.avg_campfires_rested(run_set)
    config_item.console_message += \
        "Total campfires rested at: %s\n" % campfire.total_campfires_rested(run_set)
    config_item.console_message += \
        "Average campfires upgraded at: %s\n" % campfire.avg_campfires_upgraded(run_set)
    config_item.console_message += \
        "Total campfires upgraded at: %s\n" % campfire.total_campfires_upgraded(run_set)


def store_highestmaxhp_message(config_item, run_set):
    (highest_max_hp_all, highest_hp_file_name) = math_funcs.highest_max_hp(run_set)
    config_item.console_message += \
        "Highest Max HP: %s || File Name: %s\n" % (highest_max_hp_all, highest_hp_file_name)


def store_lowestmaxhp_message(config_item, run_set):
    (lowest_max_hp_all, lowest_hp_file_name) = math_funcs.lowest_max_hp(run_set)
    config_item.console_message += \
        "Lowest Max HP: %s || File Name: %s\n" % (lowest_max_hp_all, lowest_hp_file_name)


def store_mostgold_message(config_item, run_set):
    (most_gold_held, most_gold_held_file_name) = math_funcs.most_gold_held(run_set)
    config_item.console_message += \
        "Most Gold Held: %s || File Name: %s\n" % (most_gold_held, most_gold_held_file_name)


def store_potion_message(config_item, run_set):

    if 'PotionsDataSpawned' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        potions_spawned_dict = math_funcs.potions_spawned_stats(run_set)
        total_potions_spawned = sum(potions_spawned_dict.values())

        config_item.console_message += \
            "\nList of Floors and Number of Potions spawned on each floor across all runs\n\n"
        for k, v in sorted(potions_spawned_dict.items()):
            config_item.console_message += "Floor: %s || Number of Potions: %s (Percentage: %s)\n" \
                                           % (k, v, round((v / total_potions_spawned), 2))

    if 'PotionsDataUsed' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        potions_used_dict = math_funcs.potions_used_stats(run_set)
        total_potions_used = sum(potions_used_dict.values())

        config_item.console_message += \
            "\nList of Floors and Number of Potions used on each floor across all runs\n\n"
        for k, v in sorted(potions_used_dict.items()):
            config_item.console_message += "Floor: %s || Number of Potions: %s (Percentage: %s)\n" \
                                           % (k, v, round((v / total_potions_used), 2))

    if 'PotionsDataObtained' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        floor_pick_dict = math_funcs.potions_obtained_stats(run_set)

        config_item.console_message += \
            "\nList of Floors and Number of Potions obtained on each floor across all runs\n\n"

        for floor, potions in sorted(floor_pick_dict.items()):
            potion_type_count = {i: potions.count(i) for i in potions}
            config_item.console_message += "Floor: %s\n" % floor
            for potion, obtained in potion_type_count.items():
                config_item.console_message += "  Potion: %s || Obtained Count: %s\n" % (potion, obtained)


def store_enemy_message(config_item, run_set):
    if 'EnemyEncounterCount' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        enemy_count_dict = math_funcs.enemy_encounter_count(run_set)
        sorted_enemy_count_list = sorted(enemy_count_dict.items(), key=lambda kv: kv[1], reverse=True)
        total_enemy_count = sum(enemy_count_dict.values())
        enemy_count = 1

        for enemy_count_tuple in sorted_enemy_count_list:
            (enemy, count) = enemy_count_tuple
            percentage = round((count / total_enemy_count), 2)
            config_item.console_message += \
                "%s. %s || %s (Percentage: %s)\n" % (enemy_count, enemy, count, percentage)
            enemy_count += 1

    if 'EnemiesEncounteredPerFloor' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        floor_enemy_dict = math_funcs.enemies_encountered_per_floor(run_set)

        for floor, enemy_type in sorted(floor_enemy_dict.items()):
            enemy_type_count = {i: enemy_type.count(i) for i in enemy_type}
            config_item.console_message += "Floor: %s" % floor
            for enemy, count in enemy_type_count.items():
                config_item.console_message += "  Enemy: %s || Count: %s\n" % (enemy, count)

    if 'CumulativeDamagePerEnemy' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        enemy_dmg_dict = math_funcs.total_damage_per_enemy(run_set)
        sorted_enemy_dmg_list = sorted(enemy_dmg_dict.items(), key=lambda kv: kv[1], reverse=True)
        total_enemy_dmg = sum(enemy_dmg_dict.values())
        enemy_count = 1

        for enemy_damage in sorted_enemy_dmg_list:
            (enemy, damage) = enemy_damage
            percentage = round((damage / total_enemy_dmg), 2)
            config_item.console_message += \
                "%s. %s || %s (Percentage: %s)\n" % (enemy_count, enemy, damage, percentage)
            enemy_count += 1


def store_score_message(config_item, run_set):
    if 'HighestScore' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        (highest_score_all, highest_score_file_name) = math_funcs.highest_score(run_set)
        config_item.console_message += \
            "Highest Score: %s || File Name: %s\n" % (highest_score_all, highest_score_file_name)

    if 'LowestScore' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        (lowest_score_all, lowest_score_file_name) = math_funcs.lowest_score(run_set)
        config_item.console_message += \
            "Lowest Score: %s || File Name: %s\n" % (lowest_score_all, lowest_score_file_name)

    if 'AvgScore' == config_item.config_item_name or 'OverviewAll' == config_item.config_item_name:
        average = calculate_average.score(run_set)
        if average > 0:
            config_item.console_message += "Average Score: %s\n" % average
        else:
            config_item.console_message += "There was an issue calculating the avg_score\n"


def store_cards_picked_per_floor(config_item, run_set):
    if 'CardsPickedPerFloor' == config_item.config_item_name:
        floor_pick_dict = math_funcs.cards_picked_per_floor(run_set)

        for floor, picks in sorted(floor_pick_dict.items()):
            card_type_count = {i: picks.count(i) for i in picks}
            config_item.console_message += "Floor: %s\n" % floor
            for card, picked_count in card_type_count.items():
                config_item.console_message += "  Card: %s || Picked: %s\n" % (card, picked_count)