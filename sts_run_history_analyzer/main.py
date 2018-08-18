import json
import os

import sts_run_data
import store_json
import print_single_run
import print_all_runs
from config_helper import read_config, read_target_path, read_config_boolean, config_option_to_list


# TODO: Seperate each of these out into their own function to provided better unit test coverage
def print_all_summary(config, character_run_set):
    config_section = 'PRINT_ALL_RUNS'

    if config.getboolean(config_section, 'WinLostRecords') is True:
        print_all_runs.win_lost_records(character_run_set)

    if config.getboolean(config_section, 'CampfireStats') is True:
        print_all_runs.campfire_stats(character_run_set)

    if config.getboolean(config_section, 'TotalCampfiresVisited') is True:
        print_all_runs.total_campfires_visited(character_run_set)

    if config.getboolean(config_section, 'AvgCampfiresVisited') is True:
        print_all_runs.avg_campfires_visited(character_run_set)

    if config.getboolean(config_section, 'TotalCampfiresRested') is True:
        print_all_runs.total_campfires_rested(character_run_set)

    if config.getboolean(config_section, 'AvgCampfiresRested') is True:
        print_all_runs.avg_campfires_rested(character_run_set)

    if config.getboolean(config_section, 'TotalCampfiresUpgraded') is True:
        print_all_runs.total_campfires_upgraded(character_run_set)

    if config.getboolean(config_section, 'AvgCampfiresUpgraded') is True:
        print_all_runs.avg_campfires_upgraded(character_run_set)

    if config.getboolean(config_section, 'CampfireRestPerFloor') is True:
        print_all_runs.campfire_choices_rest(character_run_set)

    if config.getboolean(config_section, 'CampfireUpgradedPerFloor') is True:
        print_all_runs.campfire_choices_upgraded(character_run_set)

    if config.getboolean(config_section, 'HighestMaxHP') is True:
        print_all_runs.highest_max_hp(character_run_set)

    if config.getboolean(config_section, 'HighestScore') is True:
        print_all_runs.highest_score(character_run_set)

    if config.getboolean(config_section, 'LowestMaxHP') is True:
        print_all_runs.lowest_max_hp(character_run_set)

    if config.getboolean(config_section, 'LowestScore') is True:
        print_all_runs.lowest_score(character_run_set)

    if config.getboolean(config_section, 'MostGold') is True:
        print_all_runs.most_gold(character_run_set)

    if config.getboolean(config_section, 'ItemsPurchasedCount') is True:
        print_all_runs.items_purchased_count(character_run_set)

    if config.getboolean(config_section, 'RelicCount') is True:
        print_all_runs.relic_count(character_run_set)

    if config.getboolean(config_section, 'PotionsDataSpawned') is True:
        print_all_runs.potions_data_spawned(character_run_set)

    if config.getboolean(config_section, 'PotionsDataUsed') is True:
        print_all_runs.potions_data_used(character_run_set)

    if config.getboolean(config_section, 'PotionsDataObtained') is True:
        print_all_runs.potions_data_obtained(character_run_set)

    if config.getboolean(config_section, 'EnemyEncounterCount') is True:
        print_all_runs.enemy_encounter_count(character_run_set)

    if config.getboolean(config_section, 'EnemiesEncounteredPerFloor') is True:
        print_all_runs.enemies_per_floor(character_run_set)

    if config.getboolean(config_section, 'CumulativeDamagePerEnemy') is True:
        print_all_runs.cumulative_dmg_enemy(character_run_set)

    if config.getboolean(config_section, 'EventChoicesPerFloor') is True:
        print_all_runs.event_choices_per_floor(character_run_set)

    if config.getboolean(config_section, 'AvgFloorReached') is True:
        print_all_runs.avg_floor_reached(character_run_set)

    if config.getboolean(config_section, 'AvgScore') is True:
        print_all_runs.avg_score(character_run_set)

    if config.getboolean(config_section, 'CardsPickedPerFloor') is True:
        print_all_runs.cards_picked_per_floor(character_run_set)

    if config.getboolean(config_section, 'Overview') is True:
        print_all_runs.details(character_run_set)


# TODO: Seperate each of these out into their own function to provided better unit test coverage
def print_individual_summary(config, parsed, current_run):
    single_run_config = 'PRINT_SINGLE_RUN'

    # Print: non-list json information
    if config.getboolean(single_run_config, 'FileName') is True:
        print_single_run.file_name(current_run)

    if config.getboolean(single_run_config, 'BuildVersion') is True:
        print_single_run.build_version(current_run)

    if config.getboolean(single_run_config, 'Timestamp') is True:
        print_single_run.timestamp(current_run)

    if config.getboolean(single_run_config, 'SpecialSeed') is True:
        print_single_run.special_seed(current_run)

    if config.getboolean(single_run_config, 'SeedPlayed') is True:
        print_single_run.seed_played(current_run)

    if config.getboolean(single_run_config, 'Overview') is True:
        print_single_run.details(current_run)

    if config.getboolean(single_run_config, 'CharacterChosen') is True:
        print_single_run.character_chosen(current_run)

    if config.getboolean(single_run_config, 'Ascension') is True:
        print_single_run.ascension(current_run)

    if config.getboolean(single_run_config, 'Victory') is True:
        print_single_run.victory(current_run)

    if config.getboolean(single_run_config, 'WinRate') is True:
        print_single_run.win_rate(current_run)

    if config.getboolean(single_run_config, 'FloorReached') is True:
        print_single_run.floor_reached(current_run)

    if config.getboolean(single_run_config, 'Score') is True:
        print_single_run.score(current_run)

    if config.getboolean(single_run_config, 'NeowBonus') is True:
        print_single_run.neow_bonus(current_run)

    if config.getboolean(single_run_config, 'NeowCost') is True:
        print_single_run.neow_cost(current_run)

    if config.getboolean(single_run_config, 'CampfireRested') is True:
        print_single_run.campfire_rested(current_run)

    if config.getboolean(single_run_config, 'CampfireUpgraded') is True:
        print_single_run.campfire_upgraded(current_run)

    if config.getboolean(single_run_config, 'ChosenSeed') is True:
        print_single_run.chosen_seed(current_run)

    if config.getboolean(single_run_config, 'CircletCount') is True:
        print_single_run.circlet_count(current_run)

    if config.getboolean(single_run_config, 'Gold') is True:
        print_single_run.gold(current_run)

    if config.getboolean(single_run_config, 'IsAscensionMode') is True:
        print_single_run.is_ascension_mode(current_run)

    if config.getboolean(single_run_config, 'IsDaily') is True:
        print_single_run.is_daily(current_run)

    if config.getboolean(single_run_config, 'IsEndless') is True:
        print_single_run.is_endless(current_run)

    if config.getboolean(single_run_config, 'IsProd') is True:
        print_single_run.is_prod(current_run)

    if config.getboolean(single_run_config, 'IsTrial') is True:
        print_single_run.is_trial(current_run)

    if config.getboolean(single_run_config, 'PlayId') is True:
        print_single_run.play_id(current_run)

    if config.getboolean(single_run_config, 'PlayerExperience') is True:
        print_single_run.player_experience(current_run)

    if config.getboolean(single_run_config, 'Playtime') is True:
        print_single_run.playtime(current_run)

    if config.getboolean(single_run_config, 'PurchasedPurges') is True:
        print_single_run.purchased_purges(current_run)

    if config.getboolean(single_run_config, 'SeedSourceTimestamp') is True:
        print_single_run.seed_source_timestamp(current_run)

    # Print: list json information
    if config.getboolean(single_run_config, 'BossRelicPickedActOne') is True:
        print_single_run.boss_relic_picked_act1(current_run)

    if config.getboolean(single_run_config, 'BossRelicNotPickedActOne') is True:
        print_single_run.boss_relic_not_picked_act1(current_run)

    if config.getboolean(single_run_config, 'BossRelicPickedActTwo') is True:
        print_single_run.boss_relic_picked_act2(current_run)

    if config.getboolean(single_run_config, 'BossRelicNotPickedActTwo') is True:
        print_single_run.boss_relic_not_picked_act2(current_run)

    if config.getboolean(single_run_config, 'CampfireChoices') is True:
        print_single_run.campfire_choices(current_run)

    if config.getboolean(single_run_config, 'CardChoices') is True:
        print_single_run.card_choices(current_run)

    if config.getboolean(single_run_config, 'CurrentHpPerFloor') is True:
        print_single_run.current_hp_per_floor(current_run)

    if config.getboolean(single_run_config, 'DamageTaken') is True:
        print_single_run.damage_taken(current_run)

    if config.getboolean(single_run_config, 'EventChoices') is True:
        print_single_run.event_choices(current_run)

    if config.getboolean(single_run_config, 'GoldPerFloor') is True:
        print_single_run.gold_per_floor(parsed, current_run)

    if config.getboolean(single_run_config, 'ItemsPurchased') is True:
        print_single_run.items_purchased(current_run)

    if config.getboolean(single_run_config, 'MasterDeck') is True:
        print_single_run.master_deck(current_run)

    if config.getboolean(single_run_config, 'MaxHpPerFloor') is True:
        print_single_run.max_hp_per_floor(current_run)

    if config.getboolean(single_run_config, 'PathPerFloor') is True:
        print_single_run.path_per_floor(current_run)

    if config.getboolean(single_run_config, 'PathTakenPerFloor') is True:
        print_single_run.path_taken_per_floor(current_run)

    if config.getboolean(single_run_config, 'PotionsFloorSpawned') is True:
        print_single_run.potions_floor_spawned(current_run)

    if config.getboolean(single_run_config, 'PotionsFloorUsage') is True:
        print_single_run.potions_floor_usage(current_run)

    if config.getboolean(single_run_config, 'PotionsObtained') is True:
        print_single_run.potions_obtained(current_run)

    if config.getboolean(single_run_config, 'Relics') is True:
        print_single_run.relics(current_run)

    if config.getboolean(single_run_config, 'RelicsObtained') is True:
        print_single_run.relics_obtained(current_run)


def character_folder_name(path):
    return path.rsplit('\\', 1)[-1]


# Key will be character and the value is blank and will be populated with sts_run_data objects
def create_run_set_dict(include_characters):
    config_section_dict_x = {}
    for character in include_characters:
        config_section_dict_x.update({character.upper(): []})
    return config_section_dict_x


# Responsible for populating the sts_run_data objects for the value
def add_to_run_set(run_set_dict, current_run, character_name_from_path):
    for character in run_set_dict.keys():
        if character == character_name_from_path:
            run_set_dict[character].append(current_run)
    return run_set_dict


def create_character_paths(target_path, include_characters):
    return [target_path + '\\' + character for character in os.listdir(target_path)
            if character in include_characters]


# TODO: Seperate each of these out into their own function to provided better unit test coverage
def store_nonlist_json(parsed, current_run):
    current_run.ascension = parsed.get('ascension_level')
    current_run.build_version = parsed.get('build_version')
    current_run.campfire_rested = parsed.get('campfire_rested')
    current_run.campfire_upgraded = parsed.get('campfire_upgraded')
    current_run.character_chosen = parsed.get('character_chosen')
    current_run.chosen_seed = parsed.get('chose_seed')
    current_run.circlet_count = parsed.get('circlet_count')
    current_run.floor_reached = parsed.get('floor_reached')
    current_run.gold = parsed.get('gold')
    current_run.is_ascension_mode = parsed.get('is_ascension_mode')
    current_run.is_daily = parsed.get('is_daily')
    current_run.is_endless = parsed.get('is_endless')
    current_run.is_prod = parsed.get('is_prod')
    current_run.is_trial = parsed.get('is_trial')
    current_run.neow_bonus = parsed.get('neow_bonus')
    current_run.neow_cost = parsed.get('neow_cost')
    current_run.play_id = parsed.get('played_id')
    current_run.player_experience = parsed.get('player_experience')
    current_run.playtime = parsed.get('playtime')
    current_run.purchased_purges = parsed.get('purchased_purges')
    current_run.score = parsed.get('score')
    current_run.seed_played = parsed.get('seed_played')
    current_run.seed_source_timestamp = parsed.get('seed_source_timestamp')
    current_run.special_seed = parsed.get('special_seed')
    current_run.timestamp = parsed.get('timestamp')
    current_run.victory = parsed.get('victory')
    current_run.win_rate = parsed.get('win_rate')


def store_list_json(parsed, current_run):
    store_json.boss_relic_info(parsed, current_run)
    store_json.campfire_choice(parsed, current_run)
    store_json.card_choices(parsed, current_run)
    store_json.current_hp_per_floor(parsed, current_run)
    store_json.damage_taken(parsed, current_run)
    store_json.event_choices(parsed, current_run)
    store_json.gold_per_floor_all(parsed, current_run)
    store_json.items_purchased_all(parsed, current_run)
    store_json.master_deck_all(parsed, current_run)
    store_json.max_hp_per_floor_all(parsed, current_run)
    store_json.path_per_floor(parsed, current_run)
    store_json.path_taken(parsed, current_run)
    store_json.potions_floor_spawned(parsed, current_run)
    store_json.potions_floor_usage(parsed, current_run)
    store_json.potions_obtained(parsed, current_run)
    store_json.relics(parsed, current_run)
    store_json.relics_obtained(parsed, current_run)


def main():

    # Declarations
    config = read_config('config.ini')
    target_path = read_target_path(config)
    print_overview = read_config_boolean(config, 'PRINT_ALL_RUNS', 'Overview')
    include_characters = config_option_to_list(config, 'DIRECTORIES', 'CharactersToInclude')
    character_paths = create_character_paths(target_path, include_characters)
    run_set_dict = create_run_set_dict(include_characters)

    # Holds a collection of all Slay the Spire runs
    run_set = set([])

    # Cycle through all the characters to include in the report
    for path in character_paths:
        # Retrieve the folder name for the character from the full_path
        character_name_from_path = character_folder_name(path)
        print('\n')
        print('***** %s Data: *****' % character_name_from_path)

        # Cycle through all the files in each character folder
        if len(os.listdir(path)) > 0:
            for file in os.listdir(path):
                current_run = sts_run_data.STSRunData(file)

                with open(str(path) + '\\' + str(file), 'r') as f:
                    parsed = json.load(f)

                    # Store parsed non-list json information for a single STS playthrough
                    store_nonlist_json(parsed, current_run)

                    # Store parsed list json information for a single STS playthrough
                    store_list_json(parsed, current_run)

                    # Print information about an individual run based on config settings
                    print_individual_summary(config, parsed, current_run)

                    # Add each current_run object to its respective character set
                    add_to_run_set(run_set_dict, current_run, character_name_from_path)
                    run_set.add(current_run)
        else:
            print("There are no .run files for character %s" % character_name_from_path)

        # Print information about all runs based on config
        for character, current_run_set in run_set_dict.items():
            if character == character_name_from_path:
                print_all_summary(config, current_run_set)

    # Condensed summary of all runs for all characters
    if print_overview is True:
        print('\n')
        print('***** Overview All Included Characters: *****')
        print_all_runs.details(run_set)

    print('\n')


main()
