from helpers import math_funcs, calculate_average
from report import report_summary
from run_data import campfire
from all_runs import shared_console_messages


def store_console_messages(run_set, sorted_print_all_runs):
    for config_item in sorted_print_all_runs:

        if len(config_item.console_message) > 0:
            config_item.console_message = ''

        if 'OverviewAll' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("HUD Data")
            shared_console_messages.store_winlost_message(config_item, run_set)
            shared_console_messages.store_campfire_message(config_item, run_set)
            shared_console_messages.store_highestmaxhp_message(config_item, run_set)
            shared_console_messages.store_lowestmaxhp_message(config_item, run_set)
            shared_console_messages.store_mostgold_message(config_item, run_set)
            shared_console_messages.store_score_message(config_item, run_set)
            shared_console_messages.store_potion_message(config_item, run_set)
            shared_console_messages.store_enemy_message(config_item, run_set)
            shared_console_messages.store_cards_picked_per_floor(config_item, run_set)

        if 'WinLostRecords' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("Win / Lost Record:")
            shared_console_messages.store_winlost_message(config_item, run_set)

        if 'CampfireStats' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("Campfire Data:")
            shared_console_messages.store_campfire_message(config_item, run_set)

        if 'TotalCampfiresVisited' == config_item.config_item_name:
            config_item.console_message += \
                "Total campfires visited: %s" % campfire.total_campfires_visited(run_set)

        if 'AvgCampfiresVisited' == config_item.config_item_name:
            config_item.console_message += \
                "Average number of campfires visited: %s" % campfire.avg_campfires_visited(run_set)

        if 'TotalCampfiresRested' == config_item.config_item_name:
            config_item.console_message += \
                "Total campfires rested at: %s" % campfire.total_campfires_rested(run_set)

        if 'AvgCampfiresRested' == config_item.config_item_name:
            config_item.console_message += \
                "Average number of campfires rested: %s" % campfire.avg_campfires_rested(run_set)

        if 'TotalCampfiresUpgraded' == config_item.config_item_name:
            config_item.console_message += \
                "Total campfires upgraded at: %s" % campfire.total_campfires_upgraded(run_set)

        if 'AvgCampfiresUpgraded' == config_item.config_item_name:
            config_item.console_message += \
                "Average number of campfires upgraded: %s" % campfire.avg_campfires_upgraded(run_set)

        if 'CampfireRestPerFloor' == config_item.config_item_name:
            rests_per_floor = campfire.campfire_rested_per_floor(run_set)
            config_item.console_message += report_summary.create_title_header("Campfire Rested Choice per Floor:")
            for floor, rest_count in sorted(rests_per_floor.items()):
                config_item.console_message += \
                    "Floor: %s || Rested: %s\n" % (floor, rest_count)

        if 'CampfireUpgradedPerFloor' == config_item.config_item_name:
            floor_pick_dict = campfire.campfire_upgrades_per_floor(run_set)

            config_item.console_message += report_summary.create_title_header("Campfire Upgrade Choice per Floor:")
            for floor, upgrades in sorted(floor_pick_dict.items()):
                card_type_count = {i: upgrades.count(i) for i in upgrades}
                config_item.console_message += "Floor: %s\n" % floor
                for card, upgrade_count in card_type_count.items():
                    config_item.console_message += \
                        "  Card: %s || Upgrade Count: %s\n" % (card, upgrade_count)

        if 'HighestMaxHP' == config_item.config_item_name:
            shared_console_messages.store_highestmaxhp_message(config_item, run_set)

        if 'HighestScore' == config_item.config_item_name:
            (highest_score_all, highest_score_file_name) = math_funcs.highest_score(run_set)
            config_item.console_message += \
                "Highest Score: %s || File Name: %s" % (highest_score_all, highest_score_file_name)

        if 'LowestMaxHP' == config_item.config_item_name:
            shared_console_messages.store_lowestmaxhp_message(config_item, run_set)

        if 'LowestScore' == config_item.config_item_name:
            (lowest_score_all, lowest_score_file_name) = math_funcs.lowest_score(run_set)
            config_item.console_message += \
                "Lowest Score: %s || File Name: %s" % (lowest_score_all, lowest_score_file_name)

        if 'MostGold' == config_item.config_item_name:
            shared_console_messages.store_mostgold_message(config_item, run_set)

        if 'ItemsPurchasedCount' == config_item.config_item_name:
            item_purchased_dict = math_funcs.items_purchased_count(run_set)
            sorted_item_purchase = sorted(item_purchased_dict.items(), key=lambda kv: kv[1], reverse=True)
            total_items_purchased = sum(item_purchased_dict.values())
            config_item.console_message += report_summary.create_title_header("Item Purchase Count")

            item_count = 1

            for item_count_tuple in sorted_item_purchase:
                (item, count) = item_count_tuple
                percentage = round((count / total_items_purchased), 2)
                config_item.console_message += \
                    "%s. %s || %s (Percentage: %s)\n" % (item_count, item, count, percentage)
                # report("%s. %s || %s (Percentage: %s)" % (item_count, item, count, percentage))
                item_count += 1

            # report('\n')

        if 'RelicCount' == config_item.config_item_name:
            relic_dict = math_funcs.relic_count(run_set)
            sorted_relic = sorted(relic_dict.items(), key=lambda kv: kv[1], reverse=True)
            total_relics = sum(relic_dict.values())
            rank = 1
            config_item.console_message += report_summary.create_title_header("Relic Count")

            for relic_count_tuple in sorted_relic:
                (relic, count) = relic_count_tuple
                percentage = round((count / total_relics), 2)
                config_item.console_message += \
                    "%s. %s || %s (Percentage: %s)\n" % (rank, relic, count, percentage)
                rank += 1

        if 'PotionsDataSpawned' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("Potions Data, Spawned")
            shared_console_messages.store_potion_message(config_item, run_set)

        if 'PotionsDataUsed' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("Potions Data, Used")
            shared_console_messages.store_potion_message(config_item, run_set)

        if 'PotionsDataObtained' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("Potions Obtained Per Floor")
            shared_console_messages.store_potion_message(config_item, run_set)

        if 'EnemyEncounterCount' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("Enemy Encounter Count")
            shared_console_messages.store_enemy_message(config_item, run_set)

        if 'EnemiesEncounteredPerFloor' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("Enemy Encountered per Floor")
            shared_console_messages.store_enemy_message(config_item, run_set)

        if 'CumulativeDamagePerEnemy' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("Cumulative Damage Per Enemy")
            shared_console_messages.store_enemy_message(config_item, run_set)

        if 'EventChoicesPerFloor' == config_item.config_item_name:
            # TODO: Update to including what specific decisions they chose
            floor_event_dict = math_funcs.events_encountered_per_floor(run_set)

            config_item.console_message += report_summary.create_title_header("Event Choices Per Floor")

            for event_choice, choices in sorted(floor_event_dict.items()):
                event_count = {i: choices.count(i) for i in choices}
                config_item.console_message += "Event Choice: %s\n" % event_choice
                for event, choice in event_count.items():
                    config_item.console_message += "  Event: %s || Count: %s\n" % (event, choice)

        if 'AvgFloorReached' == config_item.config_item_name:
            average = (round(calculate_average.floor_reached(run_set)), calculate_average.floor_reached(run_set))
            raw, rounded = average
            if raw > 0:
                config_item.console_message += "Average floor reached: %s (%s)" % (raw, average)
            else:
                config_item.console_message += "There was an issue calculating the avg_floor_reached"

        if 'AvgScore' == config_item.config_item_name:
            average = calculate_average.score(run_set)
            if average > 0:
                config_item.console_message += "Average Score: %s\n" % average
            else:
                config_item.console_message += "There was an issue calculating the avg_score\n"

        if 'CardsPickedPerFloor' == config_item.config_item_name:
            floor_pick_dict = math_funcs.cards_picked_per_floor(run_set)
            config_item.console_message += report_summary.create_title_header("Cards Picked per Floor")

            for floor, picks in sorted(floor_pick_dict.items()):
                card_type_count = {i: picks.count(i) for i in picks}
                config_item.console_message += "Floor: %s\n" % floor
                for card, picked_count in card_type_count.items():
                    config_item.console_message += "  Card: %s || Picked: %s\n" % (card, picked_count)
