from config import config_helper  # noqa
from run_data import campfire  # noqa
from individual_runs import store_run_lists


def all_runs_section(current_run, parsed, config_item_print_all):
    config = config_helper.read_config('config\\report_config.ini')

    overview_option = config_helper.string_to_bool(config['PRINT_ALL_RUNS']['OverviewAll'])

    if overview_option is True:
        current_run.victory = parsed.get('victory')
        store_run_lists.max_hp_per_floor_all(current_run, parsed)
        store_run_lists.gold_per_floor_all(current_run, parsed)
        store_run_lists.potions_floor_spawned(current_run, parsed)
        store_run_lists.potions_floor_usage(current_run, parsed)
        store_run_lists.potions_obtained(current_run, parsed)
        store_run_lists.damage_taken(current_run, parsed)
        current_run.score = parsed.get('score')
        current_run.floor_reached = parsed.get('floor_reached')
        store_run_lists.card_choices(current_run, parsed)

    for config_item in config_item_print_all:
        # Check to see if the OverviewAll option is set to False
        if overview_option is False:
            if 'WinLostRecords' == config_item.config_item_name:
                current_run.victory = parsed.get('victory')

            if 'CampfireStats' == config_item.config_item_name or \
                    'TotalCampfiresVisited' == config_item.config_item_name or \
                    'AvgCampfiresVisited' == config_item.config_item_name:

                current_run.campfire_rested = parsed.get('campfire_rested')
                current_run.campfire_upgraded = parsed.get('campfire_upgraded')

            if 'HighestMaxHP' == config_item.config_item_name or \
                    'LowestMaxHP' == config_item.config_item_name:
                store_run_lists.max_hp_per_floor_all(current_run, parsed)

            if 'MostGold' == config_item.config_item_name:
                store_run_lists.gold_per_floor_all(current_run, parsed)

            if 'PotionsDataSpawned' == config_item.config_item_name:
                store_run_lists.potions_floor_spawned(current_run, parsed)

            if 'PotionsDataUsed' == config_item.config_item_name:
                store_run_lists.potions_floor_usage(current_run, parsed)

            if 'PotionsDataObtained' == config_item.config_item_name:
                store_run_lists.potions_obtained(current_run, parsed)

            if 'EnemyEncounterCount' == config_item.config_item_name or \
                    'EnemiesEncounteredPerFloor' == config_item.config_item_name or \
                    'CumulativeDamagePerEnemy' == config_item.config_item_name:
                store_run_lists.damage_taken(current_run, parsed)

            if 'HighestScore' == config_item.config_item_name or \
                    'LowestScore' == config_item.config_item_name or \
                    'AvgScore' == config_item.config_item_name:
                current_run.score = parsed.get('score')

            if 'AvgFloorReached' == config_item.config_item_name:
                current_run.floor_reached = parsed.get('floor_reached')

            if 'CardsPickedPerFloor' == config_item.config_item_name:
                store_run_lists.card_choices(current_run, parsed)

            # Check to see if boss relic information should be stored
            if 'BossRelicPickedActOne' == config_item.config_item_name or \
                    'BossRelicNotPickedActOne' == config_item.config_item_name or \
                    'BossRelicPickedActTwo' == config_item.config_item_name or \
                    'BossRelicNotPickedActTwo' == config_item.config_item_name:
                store_run_lists.boss_relic_info(current_run, parsed)

            if 'TotalCampfiresRested' == config_item.config_item_name or \
                    'AvgCampfiresRested' == config_item.config_item_name:
                current_run.campfire_rested = parsed.get('campfire_rested')

            if 'TotalCampfiresUpgraded' == config_item.config_item_name or \
                    'AvgCampfiresUpgraded' == config_item.config_item_name:
                current_run.campfire_upgraded = parsed.get('campfire_upgraded')

            if 'CampfireRestPerFloor' == config_item.config_item_name or \
                    'CampfireUpgradedPerFloor':
                current_run.campfire_rested = parsed.get('campfire_rested')
                campfire.store_campfire_choices(current_run, parsed)

            if 'ItemsPurchasedCount' == config_item.config_item_name:
                store_run_lists.items_purchased_all(current_run, parsed)

            if 'RelicCount' == config_item.config_item_name:
                store_run_lists.relics(current_run, parsed)

            if 'EventChoicesPerFloor' == config_item.config_item_name:
                store_run_lists.event_choices(current_run, parsed)

            '''
            if section_dict['Overview'] is True:
                print_all_runs.details(character_run_set)
    
            if section_dict['ItemsPurchasedCount'] is True:
                print_all_runs.items_purchased_count(character_run_set)
            '''

    return config_item_print_all
